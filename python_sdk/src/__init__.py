"""
VizQL Data Service Python SDK

This module provides a Python client library for interacting with VizQL Data Service.
It includes all necessary model classes and API clients for:
- Querying data sources
- Reading metadata
- Building and executing queries
- Handling filters and aggregations
- Error handling

Main components:
- VizQLDataServiceClient: Main client class
- Server: Server configuration class
- Various data model classes (e.g., Query, Filter, Field, etc.)
"""

import os

# Check if we're running in development mode by checking if we're in the source directory
is_development = os.path.exists(
    os.path.join(os.path.dirname(__file__), "..", "src", "__init__.py")
)

if is_development:
    # In development, use relative imports
    from openapi_client.client import AuthenticatedClient, Client
    from openapi_client.errors import UnexpectedStatus
    from openapi_client.types import UNSET, Unset
    from openapi_client.models.aggregated_field import AggregatedField
    from openapi_client.models.aggregated_filter_field import AggregatedFilterField
    from openapi_client.models.calculated_field import CalculatedField
    from openapi_client.models.calculated_filter_field import CalculatedFilterField
    from openapi_client.models.connection import Connection
    from openapi_client.models.datasource import Datasource
    from openapi_client.models.field_metadata import FieldMetadata
    from openapi_client.models.field_metadata_data_type import FieldMetadataDataType
    from openapi_client.models.filter_ import Filter
    from openapi_client.models.filter_filter_type import FilterFilterType
    from openapi_client.models.function import Function
    from openapi_client.models.match_filter import MatchFilter
    from openapi_client.models.metadata_output import MetadataOutput
    from openapi_client.models.quantitative_date_filter import QuantitativeDateFilter
    from openapi_client.models.quantitative_filter_base import QuantitativeFilterBase
    from openapi_client.models.quantitative_filter_base_quantitative_filter_type import (
        QuantitativeFilterBaseQuantitativeFilterType,
    )
    from openapi_client.models.quantitative_numerical_filter import (
        QuantitativeNumericalFilter,
    )
    from openapi_client.models.query import Query
    from openapi_client.models.query_datasource_options import QueryDatasourceOptions
    from openapi_client.models.query_options import QueryOptions
    from openapi_client.models.query_output import QueryOutput
    from openapi_client.models.query_request import QueryRequest
    from openapi_client.models.read_metadata_request import ReadMetadataRequest
    from openapi_client.models.relative_date_filter import RelativeDateFilter
    from openapi_client.models.relative_date_filter_date_range_type import (
        RelativeDateFilterDateRangeType,
    )
    from openapi_client.models.relative_date_filter_period_type import (
        RelativeDateFilterPeriodType,
    )
    from openapi_client.models.return_format import ReturnFormat
    from openapi_client.models.set_filter import SetFilter
    from openapi_client.models.simple_field import SimpleField
    from openapi_client.models.simple_filter_field import SimpleFilterField
    from openapi_client.models.sort_direction import SortDirection
    from openapi_client.models.tableau_error import TableauError
    from openapi_client.models.tableau_error_debug import TableauErrorDebug
    from openapi_client.models.top_n_filter import TopNFilter
    from openapi_client.models.top_n_filter_direction import TopNFilterDirection
    from openapi_client.api.default import query_datasource, read_metadata
else:
    # In installed package, use absolute imports
    from vizqldataservicepythonsdk.openapi_client.client import (  # type: ignore
        AuthenticatedClient,
        Client,
    )
    from vizqldataservicepythonsdk.openapi_client.errors import UnexpectedStatus  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.types import UNSET, Unset  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.aggregated_field import (  # type: ignore
        AggregatedField,
    )
    from vizqldataservicepythonsdk.openapi_client.models.aggregated_filter_field import (  # type: ignore
        AggregatedFilterField,
    )
    from vizqldataservicepythonsdk.openapi_client.models.calculated_field import (  # type: ignore
        CalculatedField,
    )
    from vizqldataservicepythonsdk.openapi_client.models.calculated_filter_field import (  # type: ignore
        CalculatedFilterField,
    )
    from vizqldataservicepythonsdk.openapi_client.models.connection import Connection  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.datasource import Datasource  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.field_metadata import (  # type: ignore
        FieldMetadata,
    )
    from vizqldataservicepythonsdk.openapi_client.models.field_metadata_data_type import (  # type: ignore
        FieldMetadataDataType,
    )
    from vizqldataservicepythonsdk.openapi_client.models.filter_ import Filter  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.filter_filter_type import (  # type: ignore
        FilterFilterType,
    )
    from vizqldataservicepythonsdk.openapi_client.models.function import Function  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.match_filter import MatchFilter  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.metadata_output import (  # type: ignore
        MetadataOutput,
    )
    from vizqldataservicepythonsdk.openapi_client.models.quantitative_date_filter import (  # type: ignore
        QuantitativeDateFilter,
    )
    from vizqldataservicepythonsdk.openapi_client.models.quantitative_filter_base import (  # type: ignore
        QuantitativeFilterBase,
    )
    from vizqldataservicepythonsdk.openapi_client.models.quantitative_filter_base_quantitative_filter_type import (  # type: ignore
        QuantitativeFilterBaseQuantitativeFilterType,
    )
    from vizqldataservicepythonsdk.openapi_client.models.quantitative_numerical_filter import (  # type: ignore
        QuantitativeNumericalFilter,
    )
    from vizqldataservicepythonsdk.openapi_client.models.query import Query  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.query_datasource_options import (  # type: ignore
        QueryDatasourceOptions,
    )
    from vizqldataservicepythonsdk.openapi_client.models.query_options import (  # type: ignore
        QueryOptions,
    )
    from vizqldataservicepythonsdk.openapi_client.models.query_output import QueryOutput  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.query_request import (  # type: ignore
        QueryRequest,
    )
    from vizqldataservicepythonsdk.openapi_client.models.read_metadata_request import (  # type: ignore
        ReadMetadataRequest,
    )
    from vizqldataservicepythonsdk.openapi_client.models.relative_date_filter import (  # type: ignore
        RelativeDateFilter,
    )
    from vizqldataservicepythonsdk.openapi_client.models.relative_date_filter_date_range_type import (  # type: ignore
        RelativeDateFilterDateRangeType,
    )
    from vizqldataservicepythonsdk.openapi_client.models.relative_date_filter_period_type import (  # type: ignore
        RelativeDateFilterPeriodType,
    )
    from vizqldataservicepythonsdk.openapi_client.models.return_format import (  # type: ignore
        ReturnFormat,
    )
    from vizqldataservicepythonsdk.openapi_client.models.set_filter import SetFilter  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.simple_field import SimpleField  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.simple_filter_field import (  # type: ignore
        SimpleFilterField,
    )
    from vizqldataservicepythonsdk.openapi_client.models.sort_direction import (  # type: ignore
        SortDirection,
    )
    from vizqldataservicepythonsdk.openapi_client.models.tableau_error import (  # type: ignore
        TableauError,
    )
    from vizqldataservicepythonsdk.openapi_client.models.tableau_error_debug import (  # type: ignore
        TableauErrorDebug,
    )
    from vizqldataservicepythonsdk.openapi_client.models.top_n_filter import TopNFilter  # type: ignore
    from vizqldataservicepythonsdk.openapi_client.models.top_n_filter_direction import (  # type: ignore
        TopNFilterDirection,
    )
    from vizqldataservicepythonsdk.openapi_client.api.default import (  # type: ignore
        query_datasource,
        read_metadata,
    )

from .server import Server
from .client import Client as VizQLDataServiceClient

__all__ = [
    "Server",
    "VizQLDataServiceClient",
    "AuthenticatedClient",
    "Client",
    "UnexpectedStatus",
    "UNSET",
    "Unset",
    "query_datasource",
    "read_metadata",
    "AggregatedField",
    "AggregatedFilterField",
    "CalculatedField",
    "CalculatedFilterField",
    "Connection",
    "Datasource",
    "FieldMetadata",
    "FieldMetadataDataType",
    "Filter",
    "FilterFilterType",
    "Function",
    "MatchFilter",
    "MetadataOutput",
    "QuantitativeDateFilter",
    "QuantitativeFilterBase",
    "QuantitativeFilterBaseQuantitativeFilterType",
    "QuantitativeNumericalFilter",
    "Query",
    "QueryDatasourceOptions",
    "QueryOptions",
    "QueryOutput",
    "QueryRequest",
    "ReadMetadataRequest",
    "RelativeDateFilter",
    "RelativeDateFilterDateRangeType",
    "RelativeDateFilterPeriodType",
    "ReturnFormat",
    "SetFilter",
    "SimpleField",
    "SimpleFilterField",
    "SortDirection",
    "TableauError",
    "TableauErrorDebug",
    "TopNFilter",
    "TopNFilterDirection",
]
