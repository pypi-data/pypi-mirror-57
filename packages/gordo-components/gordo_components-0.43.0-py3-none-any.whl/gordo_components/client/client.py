# -*- coding: utf-8 -*-

import sys  # noqa
import copy
import requests
import logging
import itertools
import typing
from time import sleep
from threading import Lock
from typing import Dict, Any, List, Callable, Optional
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


import pandas as pd
from sklearn.base import BaseEstimator
from werkzeug.exceptions import BadRequest

from gordo_components import serializer
from gordo_components.client.io import _handle_response
from gordo_components.client.io import HttpUnprocessableEntity
from gordo_components.client.utils import EndpointMetadata, PredictionResult
from gordo_components.dataset.datasets import TimeSeriesDataset
from gordo_components.data_provider.base import GordoBaseDataProvider
from gordo_components.server import utils as server_utils


logger = logging.getLogger(__name__)


class Client:
    """
    Basic client shipped with Gordo

    Enables some basic communication with a deployed Gordo project
    """

    _mutex = Lock()
    endpoints: List[EndpointMetadata] = []

    def __init__(
        self,
        project: str,
        target: typing.Optional[str] = None,
        host: str = "localhost",
        port: int = 443,
        scheme: str = "https",
        gordo_version: str = "v0",
        metadata: typing.Optional[dict] = None,
        data_provider: typing.Optional[GordoBaseDataProvider] = None,
        prediction_forwarder: typing.Optional[
            Callable[[pd.DataFrame, EndpointMetadata, dict, pd.DataFrame], None]
        ] = None,
        batch_size: int = 100000,
        parallelism: int = 10,
        forward_resampled_sensors: bool = False,
        ignore_unhealthy_targets: bool = False,
        n_retries: int = 5,
        use_parquet: bool = False,
        session: requests.Session = requests.Session(),
    ):
        """

        Parameters
        ----------
        project: str
            Name of the project.
        target: Optional[str]
            Target name if desired to only make predictions against one target.
            Leave as None to run predictions against all targets in Watchman.
        host: str
            Host of where to find watchman and other services.
        port: int
            Port to communicate on.
        scheme: str
            The request scheme to use, ie 'https'.
        gordo_version: str
            The version of major gordo the services are using, ie. 'v0'.
        metadata: Optional[dict]
            Arbitrary mapping of key-value pairs to save to influx with
            prediction runs in 'tags' property
        data_provider: Optional[GordoBaseDataProvider]
            The data provider to use for the dataset. If not set, the client
            will fall back to using the GET /prediction endpoint
        prediction_forwarder: Optional[Callable[[pd.DataFrame, EndpointMetadata, dict, pd.DataFrame], None]]
            callable which will take a dataframe of predictions,
            ``EndpointMetadata``, the metadata, and the dataframe of resampled sensor
            values and forward them somewhere.
        batch_size: int
            How many samples to send to the server, only applicable when data
            provider is supplied.
        parallelism: int
            The maximum number of tasks to run at a given time when
            running predictions
        forward_resampled_sensors: bool
            If true then forward resampled sensor values to the prediction_forwarder
        ignore_unhealthy_targets: bool
            Ignore any targets which are unhealthy. Will raise a ``ValueError``
            if the client encounters any unhealthy endpoints, warnings emitted otherwise
        n_retries: int
            Number of times the client should attempt to retry a failed prediction request. Each time the client
            retires the time it sleeps before retrying is exponentially calculated.
        use_parquet: bool
            Pass the data to the server using the parquet protocol. Default is True
            and recommended as it's more efficient for larger batch sizes. If False JSON
            is used for sending the data back and forth.
        session: requests.Session
            The http session object to use for making requests.
        """

        self.base_url = f"{scheme}://{host}:{port}"
        self.watchman_endpoint = f"{self.base_url}/gordo/{gordo_version}/{project}/"
        self.metadata = metadata if metadata is not None else dict()
        self.prediction_forwarder = prediction_forwarder
        self.data_provider = data_provider
        self.use_parquet = use_parquet
        self.session = session

        # Default, failing back to /prediction on http code 422
        self.prediction_path = "/anomaly/prediction"
        self.batch_size = batch_size
        self.parallelism = parallelism
        self.forward_resampled_sensors = forward_resampled_sensors
        self.n_retries = n_retries
        self.query = f"?format={'parquet' if use_parquet else 'json'}"
        self.target = target
        self.ignore_unhealthy_targets = ignore_unhealthy_targets
        self.endpoints = self.get_endpoints()

    def get_endpoints(self) -> List[EndpointMetadata]:
        # Thread safe single access and updating of endpoints.
        with self._mutex:
            endpoints = self._endpoints_from_watchman(self.watchman_endpoint)
            return self._filter_endpoints(
                endpoints=endpoints,
                target=self.target,
                ignore_unhealthy_targets=self.ignore_unhealthy_targets,
            )

    @staticmethod
    def _filter_endpoints(
        endpoints: typing.List[EndpointMetadata],
        target: typing.Optional[str] = None,
        ignore_unhealthy_targets: typing.Optional[bool] = False,
    ) -> typing.List[EndpointMetadata]:
        """
        Based on the current configuration, filter out endpoints which the client
        should not care about.

        Parameters
        ----------
        endpoints: List[EndpointMetadata]
            List of EndpointMetadata objs
        target: Optional[str] (None)
            Name of the target/machine/endpoint we should filter down to
        ignore_unhealthy_targets: Optional[bool] (False)
            Should the client ignore any unhealthy endpoints?

        Returns
        -------
        List[EndpointMetadata]
            The filtered ``EndpointMetadata``s
        """

        original_endpoints = copy.copy(endpoints)

        # Raise an error if we got some unhealty endpoints and weren't suppose to ignore them.
        # otherwise filter out any unhealthy endpoints
        if (
            not target
            and not ignore_unhealthy_targets
            and not all(e.healthy for e in endpoints)
        ):
            raise ValueError(
                f"Flag 'ignore_unhealthy_targets' is set to False and we encountered some "
                f"unhealthy ones: {[ep for ep in endpoints if ep.healthy is False]}"
            )
        else:
            endpoints = [ep for ep in endpoints if ep.healthy]

        # Filter down to single endpoint if requested
        if target:
            endpoints = [ep for ep in endpoints if ep.name == target]

            # And check for single result and that it's healthy
            if len(endpoints) != 1:
                raise ValueError(
                    f"Found {'multiple' if len(endpoints) else 'no'} endpoints matching "
                    f"target name '{target}' in {original_endpoints}"
                )
            if not endpoints[0].healthy:
                raise ValueError(
                    f"The targeted endpoint: '{endpoints[0]}' is unhealthy"
                )

        # finally, raise an error if all this left us without any endpoints
        if not endpoints:
            raise ValueError(
                f"Found no endpoints out of supplied endpoints: {original_endpoints} after filtering"
            )
        return endpoints

    def _endpoints_from_watchman(self, endpoint: str) -> typing.List[EndpointMetadata]:
        """
        Get a list of endpoints by querying Watchman
        """
        resp = self.session.get(endpoint)
        if not resp.ok:
            raise IOError(f"Failed to get endpoints: {repr(resp.content)}")
        return [EndpointMetadata(data) for data in resp.json()["endpoints"]]

    def download_model(self) -> typing.Dict[str, BaseEstimator]:
        """
        Download the actual model(s) from the ML server /download-model

        Returns
        -------
        Dict[str, BaseEstimator]
            Mapping of target name to the model
        """
        models = dict()
        for endpoint in self.endpoints:
            resp = self.session.get(
                f"{self.base_url + endpoint.endpoint}/download-model"
            )
            if resp.ok:
                models[endpoint.name] = serializer.loads(resp.content)
            else:
                raise IOError(f"Failed to download model: '{repr(resp.content)}'")
        return models

    def get_metadata(self, force_refresh: bool = False) -> typing.Dict[str, dict]:
        """
        Get the metadata for each target

        Parameters
        ----------
        force_refresh : bool
            Even if the previous request was cached, make a new request for metadata.

        Returns
        -------
        Dict[str, dict]
            Mapping of target names to their metadata
        """
        if hasattr(self, "metadata_") and not force_refresh:
            return self.metadata_.copy()

        if force_refresh:
            self.endpoints = self.get_endpoints()  # Forced refresh if
        self.metadata_: Dict[str, dict] = {
            ep.name: ep.raw_metadata() for ep in self.endpoints
        }
        return self.metadata_.copy()

    def predict(
        self,
        start: datetime,
        end: datetime,
        refresh_endpoints: bool = False,
        endpoint_names: Optional[List[str]] = None,
    ) -> typing.Iterable[typing.Tuple[str, pd.DataFrame, typing.List[str]]]:
        """
        Start the prediction process.

        Parameters
        ----------
        start: datetime
        end: datetime
        refresh_endpoints : bool
            Before running predictions, refresh the current endpoints. Default
            ``False`` and will use the endpoints obtained during initialization.
        endpoint_names: Optional[List[str]]
            Optionally only target certain endpoints, referring to them by name.

        Returns
        -------
        List[Tuple[str, pandas.core.DataFrame, List[str]]
            A list of tuples, where:
              0th element is the target name
              1st element is the dataframe of the predictions; complete with a DateTime index.
              2nd element is a list of error messages (if any) for running the predictions
        """
        if refresh_endpoints:
            self.endpoints = self.get_endpoints()

        # Select endpoints if the endpoint_names were provided.
        if endpoint_names:
            endpoints = [ep for ep in self.endpoints if ep.name in endpoint_names]
        else:
            endpoints = self.endpoints

        # For every endpoint, start making predictions for the time range
        with ThreadPoolExecutor(max_workers=self.parallelism) as executor:
            jobs = executor.map(
                lambda ep: self.predict_single_endpoint(ep, start, end), endpoints
            )
            return [(j.name, j.predictions, j.error_messages) for j in jobs]

    def predict_single_endpoint(
        self, endpoint: EndpointMetadata, start: datetime, end: datetime
    ) -> PredictionResult:
        """
        Get predictions based on the /prediction POST endpoint of Gordo ML Servers

        Parameters
        ----------
        endpoint: EndpointMetadata
            Named tuple which has 'endpoint' specifying the full url to the base ml server
        start: datetime
        end: datetime

        Returns
        -------
        dict
            Prediction response from /prediction GET
        """

        # Fetch all of the raw data
        X, y = self._raw_data(endpoint, start, end)

        # Forward sensor data
        if self.prediction_forwarder is not None and self.forward_resampled_sensors:
            self.prediction_forwarder(resampled_sensor_data=X)  # type: ignore

        max_indx = len(X.index) - 1  # Maximum allowable index values

        # Start making batch predictions
        with ThreadPoolExecutor(max_workers=self.parallelism) as executor:
            jobs = executor.map(
                lambda i: self._send_prediction_request(
                    X,
                    y,
                    chunk=slice(i, i + self.batch_size),
                    endpoint=endpoint,
                    start=X.index[i],
                    end=X.index[
                        i + self.batch_size
                        if i + self.batch_size <= max_indx
                        else max_indx
                    ],
                ),
                range(0, X.shape[0], self.batch_size),
            )

            # Accumulate the batched predictions
            prediction_dfs = list()
            error_messages: List[str] = list()
            for prediction_result in jobs:
                if prediction_result.predictions is not None:
                    prediction_dfs.append(prediction_result.predictions)
                error_messages.extend(prediction_result.error_messages)

            predictions = (
                pd.concat(prediction_dfs).sort_index()
                if prediction_dfs
                else pd.DataFrame()
            )
        return PredictionResult(
            name=endpoint.name, predictions=predictions, error_messages=error_messages
        )

    def _send_prediction_request(
        self,
        X: pd.DataFrame,
        y: typing.Optional[pd.DataFrame],
        chunk: slice,
        endpoint: EndpointMetadata,
        start: datetime,
        end: datetime,
    ):
        """
        Post a slice of data to the endpoint

        Parameters
        ----------
        X: pandas.core.DataFrame
            The data for the model, in pandas representation
        chunk: slice
            The slice to take from DataFrame.iloc for the batch size
        endpoint: EndpointMetadata
        start: datetime
        end: datetime

        Notes
        -----
        PredictionResult.predictions may be None if the prediction process fails

        Returns
        -------
        PredictionResult
        """

        kwargs: Dict[str, Any] = dict(
            url=f"{self.base_url + endpoint.endpoint}{self.prediction_path}{self.query}"
        )

        # We're going to serialize the data as either JSON or Arrow
        if self.use_parquet:
            kwargs["files"] = {
                "X": server_utils.dataframe_into_parquet_bytes(X.iloc[chunk]),
                "y": server_utils.dataframe_into_parquet_bytes(y.iloc[chunk])
                if y is not None
                else None,
            }
        else:
            kwargs["json"] = {
                "X": server_utils.dataframe_to_dict(X.iloc[chunk]),
                "y": server_utils.dataframe_to_dict(y.iloc[chunk])
                if y is not None
                else None,
            }

        # Start attempting to get predictions for this batch
        for current_attempt in itertools.count(start=1):
            try:
                try:
                    resp = _handle_response(self.session.post(**kwargs))
                except HttpUnprocessableEntity:
                    self.prediction_path = "/prediction"
                    kwargs[
                        "url"
                    ] = f"{self.base_url + endpoint.endpoint}{self.prediction_path}{self.query}"
                    resp = _handle_response(self.session.post(**kwargs))
            # If it was an IO or TimeoutError, we can retry
            except (
                IOError,
                TimeoutError,
                BadRequest,
                requests.ConnectionError,
                requests.HTTPError,
            ) as exc:
                if current_attempt <= self.n_retries:
                    time_to_sleep = min(2 ** (current_attempt + 2), 300)
                    logger.warning(
                        f"Failed to get response on attempt {current_attempt} out of {self.n_retries} attempts."
                    )
                    sleep(time_to_sleep)
                    continue
                else:
                    msg = (
                        f"Failed to get predictions for dates {start} -> {end} "
                        f"for target: '{endpoint.name}' Error: {exc}"
                    )
                    logger.error(msg)

                    return PredictionResult(
                        name=endpoint.name, predictions=None, error_messages=[msg]
                    )

            # No point in retrying a BadRequest
            except BadRequest as exc:
                msg = (
                    f"Failed with BadRequest error for dates {start} -> {end} "
                    f"for target: '{endpoint.name}' Error: {exc}"
                )
                logger.error(msg)
                return PredictionResult(
                    name=endpoint.name, predictions=None, error_messages=[msg]
                )

            # Process response and return if no exception
            else:

                predictions = self.dataframe_from_response(resp)

                # Forward predictions to any other consumer if registered.
                if self.prediction_forwarder is not None:
                    self.prediction_forwarder(  # type: ignore
                        predictions=predictions,
                        endpoint=endpoint,
                        metadata=self.metadata,
                    )
                return PredictionResult(
                    name=endpoint.name, predictions=predictions, error_messages=[]
                )

    def _raw_data(
        self, endpoint: EndpointMetadata, start: datetime, end: datetime
    ) -> pd.DataFrame:
        """
        Fetch the required raw data in this time range which would
        satisfy this endpoint's /prediction POST

        Parameters
        ----------
        endpoint: EndpointMetadata
            Named tuple representing the endpoint info from Watchman
        start: datetime
        end: datetime

        Returns
        -------
        pandas.core.DataFrame
            Dataframe of required tags and index reflecting the datetime point
        """

        # We want to adjust for any model offset. If the model outputs less than it got in, it requires
        # extra data than what we're being asked to get predictions for.
        # just to give us some buffer zone.
        start = self._adjust_for_offset(
            dt=start,
            resolution=endpoint.resolution,
            n_intervals=endpoint.model_offset + 5,
        )
        dataset = TimeSeriesDataset(
            data_provider=self.data_provider,  # type: ignore
            from_ts=start,
            to_ts=end,
            resolution=endpoint.resolution,
            tag_list=endpoint.tag_list,
            target_tag_list=endpoint.target_tag_list,
        )
        return dataset.get_data()

    @staticmethod
    def _adjust_for_offset(dt: datetime, resolution: str, n_intervals: int = 100):
        """
        Adjust the given date by multiplying ``n_intervals`` by ``resolution``. Such that
        a date of 12:00:00 with ``n_intervals=2`` and ``resolution='10m'`` (10 minutes)
        would result in 11:40

        Parameters
        ----------
        dt: datetime
            Initial datetime to adjust.
        resolution: str
            A string code capable of being parsed by :meth::`pandas.Timedelta`.
        n_intervals: int
            Number of resolution steps to take earlier than the given date.

        Returns
        -------
        datetime
            The new offset datetime object.

        Examples
        --------
        >>> import dateutil
        >>> date = dateutil.parser.isoparse("2019-01-01T12:00:00+00:00")
        >>> offset_date = Client._adjust_for_offset(dt=date, resolution='15m', n_intervals=5)
        >>> str(offset_date)
        '2019-01-01 10:45:00+00:00'
        """
        return dt - (pd.Timedelta(resolution) * n_intervals)

    @staticmethod
    def dataframe_from_response(response: typing.Union[dict, bytes]) -> pd.DataFrame:
        """
        The response from the server, parsed as either JSON / dict or raw bytes,
        of which would be expected to be loadable from :func:`server.utils.dataframe_from_parquet_bytes`

        Parameters
        ----------
        response: Union[dict, bytes]
            The parsed response from the ML server.

        Returns
        -------
        pandas.DataFrame
        """
        if isinstance(response, dict):
            predictions = server_utils.dataframe_from_dict(response["data"])
        else:
            predictions = server_utils.dataframe_from_parquet_bytes(response)
        return predictions


def make_date_ranges(
    start: datetime, end: datetime, max_interval_days: int, freq: str = "H"
):
    """
    Split start and end datetimes into a list of datetime intervals.
    If the interval between start and end is less than ``max_interval_days`` then
    the resulting list will contain the original start & end. ie. [(start, end)]

    Otherwise it will split the intervals by ``freq``, parse-able by pandas.

    Parameters
    ----------
    start: datetime
    end: datetime
    max_interval_days: int
        Maximum days between start and end before splitting into intervals
    freq: str
        String frequency parse-able by Pandas

    Returns
    -------
    List[Tuple[datetime, datetime]]
    """
    if (end - start).days >= max_interval_days:
        # Split into 1hr data ranges
        date_range = pd.date_range(start, end, freq=freq)
        return [
            (date_range[i], date_range[i + 1]) for i in range(0, len(date_range) - 1)
        ]
    else:
        return [(start, end)]
