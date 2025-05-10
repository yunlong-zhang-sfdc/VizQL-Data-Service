# Table of Contents

* [client](#client)
  * [Client](#client.Client)
    * [with\_headers](#client.Client.with_headers)
    * [with\_cookies](#client.Client.with_cookies)
    * [with\_timeout](#client.Client.with_timeout)
    * [set\_httpx\_client](#client.Client.set_httpx_client)
    * [get\_httpx\_client](#client.Client.get_httpx_client)
    * [set\_async\_httpx\_client](#client.Client.set_async_httpx_client)
    * [get\_async\_httpx\_client](#client.Client.get_async_httpx_client)
  * [AuthenticatedClient](#client.AuthenticatedClient)
    * [with\_headers](#client.AuthenticatedClient.with_headers)
    * [with\_cookies](#client.AuthenticatedClient.with_cookies)
    * [with\_timeout](#client.AuthenticatedClient.with_timeout)
    * [set\_httpx\_client](#client.AuthenticatedClient.set_httpx_client)
    * [get\_httpx\_client](#client.AuthenticatedClient.get_httpx_client)
    * [set\_async\_httpx\_client](#client.AuthenticatedClient.set_async_httpx_client)
    * [get\_async\_httpx\_client](#client.AuthenticatedClient.get_async_httpx_client)
* [errors](#errors)
  * [UnexpectedStatus](#errors.UnexpectedStatus)
* [types](#types)
  * [File](#types.File)
    * [to\_tuple](#types.File.to_tuple)
  * [Response](#types.Response)
* [api.default.query\_datasource](#api.default.query_datasource)
  * [sync\_detailed](#api.default.query_datasource.sync_detailed)
  * [sync](#api.default.query_datasource.sync)
  * [asyncio\_detailed](#api.default.query_datasource.asyncio_detailed)
  * [asyncio](#api.default.query_datasource.asyncio)
* [api.default.read\_metadata](#api.default.read_metadata)
  * [sync\_detailed](#api.default.read_metadata.sync_detailed)
  * [sync](#api.default.read_metadata.sync)
  * [asyncio\_detailed](#api.default.read_metadata.asyncio_detailed)
  * [asyncio](#api.default.read_metadata.asyncio)
* [models.aggregated\_field](#models.aggregated_field)
  * [AggregatedField](#models.aggregated_field.AggregatedField)
* [models.aggregated\_filter\_field](#models.aggregated_filter_field)
  * [AggregatedFilterField](#models.aggregated_filter_field.AggregatedFilterField)
* [models.calculated\_field](#models.calculated_field)
  * [CalculatedField](#models.calculated_field.CalculatedField)
* [models.calculated\_filter\_field](#models.calculated_filter_field)
  * [CalculatedFilterField](#models.calculated_filter_field.CalculatedFilterField)
* [models.connection](#models.connection)
  * [Connection](#models.connection.Connection)
* [models.datasource](#models.datasource)
  * [Datasource](#models.datasource.Datasource)
* [models.field\_metadata](#models.field_metadata)
  * [FieldMetadata](#models.field_metadata.FieldMetadata)
* [models.field\_metadata\_data\_type](#models.field_metadata_data_type)
  * [FieldMetadataDataType](#models.field_metadata_data_type.FieldMetadataDataType)
* [models.filter\_](#models.filter_)
  * [Filter](#models.filter_.Filter)
* [models.filter\_filter\_type](#models.filter_filter_type)
  * [FilterFilterType](#models.filter_filter_type.FilterFilterType)
* [models.function](#models.function)
  * [Function](#models.function.Function)
* [models.match\_filter](#models.match_filter)
  * [MatchFilter](#models.match_filter.MatchFilter)
* [models.metadata\_output](#models.metadata_output)
  * [MetadataOutput](#models.metadata_output.MetadataOutput)
* [models.quantitative\_date\_filter](#models.quantitative_date_filter)
  * [QuantitativeDateFilter](#models.quantitative_date_filter.QuantitativeDateFilter)
* [models.quantitative\_filter\_base](#models.quantitative_filter_base)
  * [QuantitativeFilterBase](#models.quantitative_filter_base.QuantitativeFilterBase)
* [models.quantitative\_filter\_base\_quantitative\_filter\_type](#models.quantitative_filter_base_quantitative_filter_type)
  * [QuantitativeFilterBaseQuantitativeFilterType](#models.quantitative_filter_base_quantitative_filter_type.QuantitativeFilterBaseQuantitativeFilterType)
* [models.quantitative\_numerical\_filter](#models.quantitative_numerical_filter)
  * [QuantitativeNumericalFilter](#models.quantitative_numerical_filter.QuantitativeNumericalFilter)
* [models.query](#models.query)
  * [Query](#models.query.Query)
* [models.query\_datasource\_options](#models.query_datasource_options)
  * [QueryDatasourceOptions](#models.query_datasource_options.QueryDatasourceOptions)
* [models.query\_options](#models.query_options)
  * [QueryOptions](#models.query_options.QueryOptions)
* [models.query\_output](#models.query_output)
  * [QueryOutput](#models.query_output.QueryOutput)
* [models.query\_request](#models.query_request)
  * [QueryRequest](#models.query_request.QueryRequest)
* [models.read\_metadata\_request](#models.read_metadata_request)
  * [ReadMetadataRequest](#models.read_metadata_request.ReadMetadataRequest)
* [models.relative\_date\_filter](#models.relative_date_filter)
  * [RelativeDateFilter](#models.relative_date_filter.RelativeDateFilter)
* [models.relative\_date\_filter\_date\_range\_type](#models.relative_date_filter_date_range_type)
  * [RelativeDateFilterDateRangeType](#models.relative_date_filter_date_range_type.RelativeDateFilterDateRangeType)
* [models.relative\_date\_filter\_period\_type](#models.relative_date_filter_period_type)
  * [RelativeDateFilterPeriodType](#models.relative_date_filter_period_type.RelativeDateFilterPeriodType)
* [models.return\_format](#models.return_format)
  * [ReturnFormat](#models.return_format.ReturnFormat)
* [models.set\_filter](#models.set_filter)
  * [SetFilter](#models.set_filter.SetFilter)
* [models.simple\_field](#models.simple_field)
  * [SimpleField](#models.simple_field.SimpleField)
* [models.simple\_filter\_field](#models.simple_filter_field)
  * [SimpleFilterField](#models.simple_filter_field.SimpleFilterField)
* [models.sort\_direction](#models.sort_direction)
  * [SortDirection](#models.sort_direction.SortDirection)
* [models.tableau\_error](#models.tableau_error)
  * [TableauError](#models.tableau_error.TableauError)
* [models.tableau\_error\_debug](#models.tableau_error_debug)
  * [TableauErrorDebug](#models.tableau_error_debug.TableauErrorDebug)
* [models.top\_n\_filter](#models.top_n_filter)
  * [TopNFilter](#models.top_n_filter.TopNFilter)
* [models.top\_n\_filter\_direction](#models.top_n_filter_direction)
  * [TopNFilterDirection](#models.top_n_filter_direction.TopNFilterDirection)

<a id="client"></a>

# client

<a id="client.Client"></a>

## Client Objects

```python
@define
class Client()
```

A class for keeping track of data related to the API

The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

``base_url``: The base URL for the API, all requests are made to a relative path to this URL

``cookies``: A dictionary of cookies to be sent with every request

``headers``: A dictionary of headers to be sent with every request

``timeout``: The maximum amount of a time a request can take. API functions will raise
httpx.TimeoutException if this is exceeded.

``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
but can be set to False for testing purposes.

``follow_redirects``: Whether or not to follow redirects. Default value is False.

``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


**Attributes**:

- `raise_on_unexpected_status` - Whether or not to raise an errors.UnexpectedStatus if the API returns a
  status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
  argument to the constructor.

<a id="client.Client.with_headers"></a>

#### with\_headers

```python
def with_headers(headers: dict[str, str]) -> "Client"
```

Get a new client matching this one with additional headers

<a id="client.Client.with_cookies"></a>

#### with\_cookies

```python
def with_cookies(cookies: dict[str, str]) -> "Client"
```

Get a new client matching this one with additional cookies

<a id="client.Client.with_timeout"></a>

#### with\_timeout

```python
def with_timeout(timeout: httpx.Timeout) -> "Client"
```

Get a new client matching this one with a new timeout (in seconds)

<a id="client.Client.set_httpx_client"></a>

#### set\_httpx\_client

```python
def set_httpx_client(client: httpx.Client) -> "Client"
```

Manually set the underlying httpx.Client

**NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.

<a id="client.Client.get_httpx_client"></a>

#### get\_httpx\_client

```python
def get_httpx_client() -> httpx.Client
```

Get the underlying httpx.Client, constructing a new one if not previously set

<a id="client.Client.set_async_httpx_client"></a>

#### set\_async\_httpx\_client

```python
def set_async_httpx_client(async_client: httpx.AsyncClient) -> "Client"
```

Manually the underlying httpx.AsyncClient

**NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.

<a id="client.Client.get_async_httpx_client"></a>

#### get\_async\_httpx\_client

```python
def get_async_httpx_client() -> httpx.AsyncClient
```

Get the underlying httpx.AsyncClient, constructing a new one if not previously set

<a id="client.AuthenticatedClient"></a>

## AuthenticatedClient Objects

```python
@define
class AuthenticatedClient()
```

A Client which has been authenticated for use on secured endpoints

The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

``base_url``: The base URL for the API, all requests are made to a relative path to this URL

``cookies``: A dictionary of cookies to be sent with every request

``headers``: A dictionary of headers to be sent with every request

``timeout``: The maximum amount of a time a request can take. API functions will raise
httpx.TimeoutException if this is exceeded.

``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
but can be set to False for testing purposes.

``follow_redirects``: Whether or not to follow redirects. Default value is False.

``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


**Attributes**:

- `raise_on_unexpected_status` - Whether or not to raise an errors.UnexpectedStatus if the API returns a
  status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
  argument to the constructor.
- `token` - The token to use for authentication
- `prefix` - The prefix to use for the Authorization header
- `auth_header_name` - The name of the Authorization header

<a id="client.AuthenticatedClient.with_headers"></a>

#### with\_headers

```python
def with_headers(headers: dict[str, str]) -> "AuthenticatedClient"
```

Get a new client matching this one with additional headers

<a id="client.AuthenticatedClient.with_cookies"></a>

#### with\_cookies

```python
def with_cookies(cookies: dict[str, str]) -> "AuthenticatedClient"
```

Get a new client matching this one with additional cookies

<a id="client.AuthenticatedClient.with_timeout"></a>

#### with\_timeout

```python
def with_timeout(timeout: httpx.Timeout) -> "AuthenticatedClient"
```

Get a new client matching this one with a new timeout (in seconds)

<a id="client.AuthenticatedClient.set_httpx_client"></a>

#### set\_httpx\_client

```python
def set_httpx_client(client: httpx.Client) -> "AuthenticatedClient"
```

Manually set the underlying httpx.Client

**NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.

<a id="client.AuthenticatedClient.get_httpx_client"></a>

#### get\_httpx\_client

```python
def get_httpx_client() -> httpx.Client
```

Get the underlying httpx.Client, constructing a new one if not previously set

<a id="client.AuthenticatedClient.set_async_httpx_client"></a>

#### set\_async\_httpx\_client

```python
def set_async_httpx_client(
        async_client: httpx.AsyncClient) -> "AuthenticatedClient"
```

Manually the underlying httpx.AsyncClient

**NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.

<a id="client.AuthenticatedClient.get_async_httpx_client"></a>

#### get\_async\_httpx\_client

```python
def get_async_httpx_client() -> httpx.AsyncClient
```

Get the underlying httpx.AsyncClient, constructing a new one if not previously set

<a id="errors"></a>

# errors

Contains shared errors types that can be raised from API functions

<a id="errors.UnexpectedStatus"></a>

## UnexpectedStatus Objects

```python
class UnexpectedStatus(Exception)
```

Raised by api functions when the response status an undocumented status and Client.raise_on_unexpected_status is True

<a id="types"></a>

# types

Contains some shared types for properties

<a id="types.File"></a>

## File Objects

```python
@define
class File()
```

Contains information for file uploads

<a id="types.File.to_tuple"></a>

#### to\_tuple

```python
def to_tuple() -> FileJsonType
```

Return a tuple representation that httpx will accept for multipart/form-data

<a id="types.Response"></a>

## Response Objects

```python
@define
class Response(Generic[T])
```

A response from an endpoint

<a id="api.default.query_datasource"></a>

# api.default.query\_datasource

<a id="api.default.query_datasource.sync_detailed"></a>

#### sync\_detailed

```python
def sync_detailed(*, client: Union[AuthenticatedClient, Client],
                  body: QueryRequest) -> Response[QueryOutput]
```

Query data source

Queries a specific data source and returns the resulting data.

**Arguments**:

  body (QueryRequest):
  

**Raises**:

- `errors.UnexpectedStatus` - If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
- `httpx.TimeoutException` - If the request takes longer than Client.timeout.
  

**Returns**:

  Response[QueryOutput]

<a id="api.default.query_datasource.sync"></a>

#### sync

```python
def sync(*, client: Union[AuthenticatedClient, Client],
         body: QueryRequest) -> Optional[QueryOutput]
```

Query data source

Queries a specific data source and returns the resulting data.

**Arguments**:

  body (QueryRequest):
  

**Raises**:

- `errors.UnexpectedStatus` - If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
- `httpx.TimeoutException` - If the request takes longer than Client.timeout.
  

**Returns**:

  QueryOutput

<a id="api.default.query_datasource.asyncio_detailed"></a>

#### asyncio\_detailed

```python
async def asyncio_detailed(*, client: Union[AuthenticatedClient, Client],
                           body: QueryRequest) -> Response[QueryOutput]
```

Query data source

Queries a specific data source and returns the resulting data.

**Arguments**:

  body (QueryRequest):
  

**Raises**:

- `errors.UnexpectedStatus` - If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
- `httpx.TimeoutException` - If the request takes longer than Client.timeout.
  

**Returns**:

  Response[QueryOutput]

<a id="api.default.query_datasource.asyncio"></a>

#### asyncio

```python
async def asyncio(*, client: Union[AuthenticatedClient, Client],
                  body: QueryRequest) -> Optional[QueryOutput]
```

Query data source

Queries a specific data source and returns the resulting data.

**Arguments**:

  body (QueryRequest):
  

**Raises**:

- `errors.UnexpectedStatus` - If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
- `httpx.TimeoutException` - If the request takes longer than Client.timeout.
  

**Returns**:

  QueryOutput

<a id="api.default.read_metadata"></a>

# api.default.read\_metadata

<a id="api.default.read_metadata.sync_detailed"></a>

#### sync\_detailed

```python
def sync_detailed(*, client: Union[AuthenticatedClient, Client],
                  body: ReadMetadataRequest) -> Response[MetadataOutput]
```

Request data source metadata

Requests metadata for a specific data source. The metadata provides information about the data
fields, such as field names, data types, and descriptions.

**Arguments**:

  body (ReadMetadataRequest):
  

**Raises**:

- `errors.UnexpectedStatus` - If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
- `httpx.TimeoutException` - If the request takes longer than Client.timeout.
  

**Returns**:

  Response[MetadataOutput]

<a id="api.default.read_metadata.sync"></a>

#### sync

```python
def sync(*, client: Union[AuthenticatedClient, Client],
         body: ReadMetadataRequest) -> Optional[MetadataOutput]
```

Request data source metadata

Requests metadata for a specific data source. The metadata provides information about the data
fields, such as field names, data types, and descriptions.

**Arguments**:

  body (ReadMetadataRequest):
  

**Raises**:

- `errors.UnexpectedStatus` - If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
- `httpx.TimeoutException` - If the request takes longer than Client.timeout.
  

**Returns**:

  MetadataOutput

<a id="api.default.read_metadata.asyncio_detailed"></a>

#### asyncio\_detailed

```python
async def asyncio_detailed(
        *, client: Union[AuthenticatedClient, Client],
        body: ReadMetadataRequest) -> Response[MetadataOutput]
```

Request data source metadata

Requests metadata for a specific data source. The metadata provides information about the data
fields, such as field names, data types, and descriptions.

**Arguments**:

  body (ReadMetadataRequest):
  

**Raises**:

- `errors.UnexpectedStatus` - If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
- `httpx.TimeoutException` - If the request takes longer than Client.timeout.
  

**Returns**:

  Response[MetadataOutput]

<a id="api.default.read_metadata.asyncio"></a>

#### asyncio

```python
async def asyncio(*, client: Union[AuthenticatedClient, Client],
                  body: ReadMetadataRequest) -> Optional[MetadataOutput]
```

Request data source metadata

Requests metadata for a specific data source. The metadata provides information about the data
fields, such as field names, data types, and descriptions.

**Arguments**:

  body (ReadMetadataRequest):
  

**Raises**:

- `errors.UnexpectedStatus` - If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
- `httpx.TimeoutException` - If the request takes longer than Client.timeout.
  

**Returns**:

  MetadataOutput

<a id="models.aggregated_field"></a>

# models.aggregated\_field

<a id="models.aggregated_field.AggregatedField"></a>

## AggregatedField Objects

```python
@_attrs_define
class AggregatedField()
```

**Attributes**:

- `function` _Function_ - The standard set of Tableau aggregations which can be applied to a field.
- `field_caption` _str_ - Either the name of a specific Field in the data source, or, in the case of a calculation, a
  user-supplied name for the calculation.
- `field_alias` _Union[Unset, str]_ - An alternative name to give the field. Will only be used in object format
  output.
- `max_decimal_places` _Union[Unset, int]_ - The maximum number of decimal places. Any trailing 0s will be dropped.
  The maxDecimalPlaces value must be greater or equal to 0.
- `sort_direction` _Union[Unset, SortDirection]_ - The direction of the sort, either ascending or descending. If not
  supplied, the default is ascending.
- `sort_priority` _Union[Unset, int]_ - To enable sorting on a specific Field, provide a sortPriority for that field,
  and that field will be sorted. The sortPriority provides a ranking of how to sort fields when multiple fields
  are being sorted. The highest priority (lowest number) field is sorted first. If only one field is being sorted,
  then any value may be used for sortPriority. SortPriority should be an integer greater than 0.

<a id="models.aggregated_filter_field"></a>

# models.aggregated\_filter\_field

<a id="models.aggregated_filter_field.AggregatedFilterField"></a>

## AggregatedFilterField Objects

```python
@_attrs_define
class AggregatedFilterField()
```

**Attributes**:

- `field_caption` _str_ - The caption of the field to filter on.
- `function` _Function_ - The standard set of Tableau aggregations which can be applied to a field.

<a id="models.calculated_field"></a>

# models.calculated\_field

<a id="models.calculated_field.CalculatedField"></a>

## CalculatedField Objects

```python
@_attrs_define
class CalculatedField()
```

**Attributes**:

- `calculation` _str_ - A Tableau calculation that will be returned as a Field in the query.
- `field_caption` _str_ - Either the name of a specific Field in the data source, or, in the case of a calculation, a
  user-supplied name for the calculation.
- `field_alias` _Union[Unset, str]_ - An alternative name to give the field. Will only be used in object format
  output.
- `max_decimal_places` _Union[Unset, int]_ - The maximum number of decimal places. Any trailing 0s will be dropped.
  The maxDecimalPlaces value must be greater or equal to 0.
- `sort_direction` _Union[Unset, SortDirection]_ - The direction of the sort, either ascending or descending. If not
  supplied, the default is ascending.
- `sort_priority` _Union[Unset, int]_ - To enable sorting on a specific Field, provide a sortPriority for that field,
  and that field will be sorted. The sortPriority provides a ranking of how to sort fields when multiple fields
  are being sorted. The highest priority (lowest number) field is sorted first. If only one field is being sorted,
  then any value may be used for sortPriority. SortPriority should be an integer greater than 0.

<a id="models.calculated_filter_field"></a>

# models.calculated\_filter\_field

<a id="models.calculated_filter_field.CalculatedFilterField"></a>

## CalculatedFilterField Objects

```python
@_attrs_define
class CalculatedFilterField()
```

**Attributes**:

- `calculation` _str_ - A Tableau calculation that will be used to filter on.

<a id="models.connection"></a>

# models.connection

<a id="models.connection.Connection"></a>

## Connection Objects

```python
@_attrs_define
class Connection()
```

**Attributes**:

  connection_username (str):
  connection_password (str):
  connection_luid (Union[Unset, str]):

<a id="models.datasource"></a>

# models.datasource

<a id="models.datasource.Datasource"></a>

## Datasource Objects

```python
@_attrs_define
class Datasource()
```

**Attributes**:

- `datasource_luid` _str_ - The LUID of the data source to be queried.
  connections (Union[Unset, list['Connection']]):

<a id="models.field_metadata"></a>

# models.field\_metadata

<a id="models.field_metadata.FieldMetadata"></a>

## FieldMetadata Objects

```python
@_attrs_define
class FieldMetadata()
```

Describes a field in the data source that can be used to create queries.

**Attributes**:

  field_name (Union[Unset, str]):
  field_caption (Union[Unset, str]):
  data_type (Union[Unset, FieldMetadataDataType]):
  logical_table_id (Union[Unset, str]):

<a id="models.field_metadata_data_type"></a>

# models.field\_metadata\_data\_type

<a id="models.field_metadata_data_type.FieldMetadataDataType"></a>

## FieldMetadataDataType Objects

```python
class FieldMetadataDataType(str, Enum)
```

Fieldmetadatadatatype enumeration.

This enum represents the fieldmetadatadatatype values supported by the VizQL Data Service.

Values:
- BOOLEAN: Boolean
- DATE: Date
- DATETIME: Datetime
- INTEGER: Integer
- REAL: Real
- SPATIAL: Spatial
- STRING: String
- UNKNOWN: Unknown

**Example**:

  >>> FieldMetadataDataType.BOOLEAN
  FieldMetadataDataType.BOOLEAN

<a id="models.filter_"></a>

# models.filter\_

<a id="models.filter_.Filter"></a>

## Filter Objects

```python
@_attrs_define
class Filter()
```

A filter to be used in the query to filter on the data source.

**Attributes**:

  field (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField']):
  filter_type (FilterFilterType):
- `context` _Union[Unset, bool]_ - Make the given filter a context filter, meaning that it's an independent filter.
  Any other filters that you set are defined as dependent filters because they process only the data that passes
  through the context filter. Default: False.

<a id="models.filter_filter_type"></a>

# models.filter\_filter\_type

<a id="models.filter_filter_type.FilterFilterType"></a>

## FilterFilterType Objects

```python
class FilterFilterType(str, Enum)
```

Filterfiltertype enumeration.

This enum represents the filterfiltertype values supported by the VizQL Data Service.

Values:
- DATE: Date
- MATCH: Match
- QUANTITATIVE_DATE: Quantitative Date
- QUANTITATIVE_NUMERICAL: Quantitative Numerical
- SET: Set
- TOP: Top

**Example**:

  >>> FilterFilterType.DATE
  FilterFilterType.DATE

<a id="models.function"></a>

# models.function

<a id="models.function.Function"></a>

## Function Objects

```python
class Function(str, Enum)
```

Function enumeration.

This enum represents the function values supported by the VizQL Data Service.

Values:
- AVG: Avg
- COLLECT: Collect
- COUNT: Count
- COUNTD: Countd
- DAY: Day
- MAX: Max
- MEDIAN: Median
- MIN: Min
- MONTH: Month
- QUARTER: Quarter
- STDEV: Stdev
- SUM: Sum
- TRUNC_DAY: Trunc Day
- TRUNC_MONTH: Trunc Month
- TRUNC_QUARTER: Trunc Quarter
- TRUNC_WEEK: Trunc Week
- TRUNC_YEAR: Trunc Year
- VAR: Var
- WEEK: Week
- YEAR: Year

**Example**:

  >>> Function.AVG
  Function.AVG

<a id="models.match_filter"></a>

# models.match\_filter

<a id="models.match_filter.MatchFilter"></a>

## MatchFilter Objects

```python
@_attrs_define
class MatchFilter()
```

**Attributes**:

  field (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField']):
  filter_type (FilterFilterType):
- `context` _Union[Unset, bool]_ - Make the given filter a context filter, meaning that it's an independent filter.
  Any other filters that you set are defined as dependent filters because they process only the data that passes
  through the context filter. Default: False.
- `contains` _Union[Unset, str]_ - Matches when a field contains this value.
- `starts_with` _Union[Unset, str]_ - Matches when a field starts with this value.
- `ends_with` _Union[Unset, str]_ - Matches when a field ends with this value.
- `exclude` _Union[Unset, bool]_ - When true, the inverse of the matching logic will be used. Default: False.

<a id="models.metadata_output"></a>

# models.metadata\_output

<a id="models.metadata_output.MetadataOutput"></a>

## MetadataOutput Objects

```python
@_attrs_define
class MetadataOutput()
```

**Attributes**:

  data (Union[Unset, list['FieldMetadata']]):

<a id="models.quantitative_date_filter"></a>

# models.quantitative\_date\_filter

<a id="models.quantitative_date_filter.QuantitativeDateFilter"></a>

## QuantitativeDateFilter Objects

```python
@_attrs_define
class QuantitativeDateFilter()
```

**Attributes**:

  field (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField']):
  filter_type (FilterFilterType):
  quantitative_filter_type (QuantitativeFilterBaseQuantitativeFilterType):
- `context` _Union[Unset, bool]_ - Make the given filter a context filter, meaning that it's an independent filter.
  Any other filters that you set are defined as dependent filters because they process only the data that passes
  through the context filter. Default: False.
- `include_nulls` _Union[Unset, bool]_ - Should nulls be returned or not. Only applies to RANGE, MIN, and MAX
  filters. If not provided, the default is to not include null values.
- `min_date` _Union[Unset, datetime.date]_ - An RFC 3339 date indicating the earliest date to filter upon. Required
  if using quantitativeFilterType RANGE or if using quantitativeFilterType MIN.
- `max_date` _Union[Unset, datetime.date]_ - An RFC 3339 date indicating the latest date to filter on. Required if
  using quantitativeFilterType RANGE or if using quantitativeFilterType MIN.

<a id="models.quantitative_filter_base"></a>

# models.quantitative\_filter\_base

<a id="models.quantitative_filter_base.QuantitativeFilterBase"></a>

## QuantitativeFilterBase Objects

```python
@_attrs_define
class QuantitativeFilterBase()
```

**Attributes**:

  field (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField']):
  filter_type (FilterFilterType):
  quantitative_filter_type (QuantitativeFilterBaseQuantitativeFilterType):
- `context` _Union[Unset, bool]_ - Make the given filter a context filter, meaning that it's an independent filter.
  Any other filters that you set are defined as dependent filters because they process only the data that passes
  through the context filter. Default: False.
- `include_nulls` _Union[Unset, bool]_ - Should nulls be returned or not. Only applies to RANGE, MIN, and MAX
  filters. If not provided, the default is to not include null values.

<a id="models.quantitative_filter_base_quantitative_filter_type"></a>

# models.quantitative\_filter\_base\_quantitative\_filter\_type

<a id="models.quantitative_filter_base_quantitative_filter_type.QuantitativeFilterBaseQuantitativeFilterType"></a>

## QuantitativeFilterBaseQuantitativeFilterType Objects

```python
class QuantitativeFilterBaseQuantitativeFilterType(str, Enum)
```

Quantitativefilterbasequantitativefiltertype enumeration.

This enum represents the quantitativefilterbasequantitativefiltertype values supported by the VizQL Data Service.

Values:
- MAX: Max
- MIN: Min
- ONLY_NON_NULL: Only Non Null
- ONLY_NULL: Only Null
- RANGE: Range

**Example**:

  >>> QuantitativeFilterBaseQuantitativeFilterType.MAX
  QuantitativeFilterBaseQuantitativeFilterType.MAX

<a id="models.quantitative_numerical_filter"></a>

# models.quantitative\_numerical\_filter

<a id="models.quantitative_numerical_filter.QuantitativeNumericalFilter"></a>

## QuantitativeNumericalFilter Objects

```python
@_attrs_define
class QuantitativeNumericalFilter()
```

**Attributes**:

  field (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField']):
  filter_type (FilterFilterType):
  quantitative_filter_type (QuantitativeFilterBaseQuantitativeFilterType):
- `context` _Union[Unset, bool]_ - Make the given filter a context filter, meaning that it's an independent filter.
  Any other filters that you set are defined as dependent filters because they process only the data that passes
  through the context filter. Default: False.
- `include_nulls` _Union[Unset, bool]_ - Should nulls be returned or not. Only applies to RANGE, MIN, and MAX
  filters. If not provided, the default is to not include null values.
- `min_` _Union[Unset, float]_ - A numerical value, either integer or floating point, indicating the minimum value to
  filter upon. Required if using quantitativeFilterType RANGE or if using quantitativeFilterType MIN.
- `max_` _Union[Unset, float]_ - A numerical value, either integer or floating point, indicating the maximum value to
  filter upon. Required if using quantitativeFilterType RANGE or if using quantitativeFilterType MIN.

<a id="models.query"></a>

# models.query

<a id="models.query.Query"></a>

## Query Objects

```python
@_attrs_define
class Query()
```

The query is the fundamental interface to the VizQL Data Service. It holds the specific semantics to perform against
the data source. A query consists of an array of fields to query against, and an optional array of filters to apply
to the query.

**Attributes**:

- `fields` _list[Union['AggregatedField', 'CalculatedField', 'SimpleField']]_ - An array of fields that define the
  query.
- `filters` _Union[Unset, list['Filter']]_ - An optional array of filters to apply to the query.

<a id="models.query_datasource_options"></a>

# models.query\_datasource\_options

<a id="models.query_datasource_options.QueryDatasourceOptions"></a>

## QueryDatasourceOptions Objects

```python
@_attrs_define
class QueryDatasourceOptions()
```

**Attributes**:

  return_format (Union[Unset, ReturnFormat]):
- `debug` _Union[Unset, bool]_ - Default: False.
- `disaggregate` _Union[Unset, bool]_ - Default: False.

<a id="models.query_options"></a>

# models.query\_options

<a id="models.query_options.QueryOptions"></a>

## QueryOptions Objects

```python
@_attrs_define
class QueryOptions()
```

Some optional metadata that can be used to adjust the behavior of an endpoint.

**Attributes**:

  return_format (Union[Unset, ReturnFormat]):
- `debug` _Union[Unset, bool]_ - Default: False.

<a id="models.query_output"></a>

# models.query\_output

<a id="models.query_output.QueryOutput"></a>

## QueryOutput Objects

```python
@_attrs_define
class QueryOutput()
```

**Attributes**:

  data (Union[Unset, list[Any]]):

<a id="models.query_request"></a>

# models.query\_request

<a id="models.query_request.QueryRequest"></a>

## QueryRequest Objects

```python
@_attrs_define
class QueryRequest()
```

**Attributes**:

  datasource (Datasource):
- `query` _Query_ - The query is the fundamental interface to the VizQL Data Service. It holds the specific semantics
  to perform against the data source. A query consists of an array of fields to query against, and an optional
  array of filters to apply to the query.
  options (Union[Unset, QueryDatasourceOptions]):

<a id="models.read_metadata_request"></a>

# models.read\_metadata\_request

<a id="models.read_metadata_request.ReadMetadataRequest"></a>

## ReadMetadataRequest Objects

```python
@_attrs_define
class ReadMetadataRequest()
```

**Attributes**:

  datasource (Datasource):
- `options` _Union[Unset, QueryOptions]_ - Some optional metadata that can be used to adjust the behavior of an
  endpoint.

<a id="models.relative_date_filter"></a>

# models.relative\_date\_filter

<a id="models.relative_date_filter.RelativeDateFilter"></a>

## RelativeDateFilter Objects

```python
@_attrs_define
class RelativeDateFilter()
```

**Attributes**:

  field (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField']):
  filter_type (FilterFilterType):
- `period_type` _RelativeDateFilterPeriodType_ - The units of time in the relative date range.
- `date_range_type` _RelativeDateFilterDateRangeType_ - The direction in the relative date range.
- `context` _Union[Unset, bool]_ - Make the given filter a context filter, meaning that it's an independent filter.
  Any other filters that you set are defined as dependent filters because they process only the data that passes
  through the context filter. Default: False.
- `range_n` _Union[Unset, int]_ - When dateRangeType is LASTN or NEXTN, this is the N value (how many years, months,
  etc.).
- `anchor_date` _Union[Unset, datetime.date]_ - If a value for this field isn't provided, the value defaults to
  today.
- `include_nulls` _Union[Unset, bool]_ - Should nulls be returned or not. If a value isn't provided, the default is
  to not include null values.

<a id="models.relative_date_filter_date_range_type"></a>

# models.relative\_date\_filter\_date\_range\_type

<a id="models.relative_date_filter_date_range_type.RelativeDateFilterDateRangeType"></a>

## RelativeDateFilterDateRangeType Objects

```python
class RelativeDateFilterDateRangeType(str, Enum)
```

Relativedatefilterdaterangetype enumeration.

This enum represents the relativedatefilterdaterangetype values supported by the VizQL Data Service.

Values:
- CURRENT: Current
- LAST: Last
- LASTN: Lastn
- NEXT: Next
- NEXTN: Nextn
- TODATE: Todate

**Example**:

  >>> RelativeDateFilterDateRangeType.CURRENT
  RelativeDateFilterDateRangeType.CURRENT

<a id="models.relative_date_filter_period_type"></a>

# models.relative\_date\_filter\_period\_type

<a id="models.relative_date_filter_period_type.RelativeDateFilterPeriodType"></a>

## RelativeDateFilterPeriodType Objects

```python
class RelativeDateFilterPeriodType(str, Enum)
```

Relativedatefilterperiodtype enumeration.

This enum represents the relativedatefilterperiodtype values supported by the VizQL Data Service.

Values:
- DAYS: Days
- HOURS: Hours
- MINUTES: Minutes
- MONTHS: Months
- QUARTERS: Quarters
- WEEKS: Weeks
- YEARS: Years

**Example**:

  >>> RelativeDateFilterPeriodType.DAYS
  RelativeDateFilterPeriodType.DAYS

<a id="models.return_format"></a>

# models.return\_format

<a id="models.return_format.ReturnFormat"></a>

## ReturnFormat Objects

```python
class ReturnFormat(str, Enum)
```

Returnformat enumeration.

This enum represents the returnformat values supported by the VizQL Data Service.

Values:
- ARRAYS: Arrays
- OBJECTS: Objects

**Example**:

  >>> ReturnFormat.ARRAYS
  ReturnFormat.ARRAYS

<a id="models.set_filter"></a>

# models.set\_filter

<a id="models.set_filter.SetFilter"></a>

## SetFilter Objects

```python
@_attrs_define
class SetFilter()
```

**Attributes**:

  field (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField']):
  filter_type (FilterFilterType):
- `values` _list[Any]_ - An array of values to filter on.
- `context` _Union[Unset, bool]_ - Make the given filter a context filter, meaning that it's an independent filter.
  Any other filters that you set are defined as dependent filters because they process only the data that passes
  through the context filter. Default: False.
- `exclude` _Union[Unset, bool]_ - Default: False.

<a id="models.simple_field"></a>

# models.simple\_field

<a id="models.simple_field.SimpleField"></a>

## SimpleField Objects

```python
@_attrs_define
class SimpleField()
```

**Attributes**:

- `field_caption` _Union[Unset, str]_ - Either the name of a specific Field in the data source, or, in the case of a
  calculation, a user-supplied name for the calculation.
- `field_alias` _Union[Unset, str]_ - An alternative name to give the field. Will only be used in object format
  output.
- `max_decimal_places` _Union[Unset, int]_ - The maximum number of decimal places. Any trailing 0s will be dropped.
  The maxDecimalPlaces value must be greater or equal to 0.
- `sort_direction` _Union[Unset, SortDirection]_ - The direction of the sort, either ascending or descending. If not
  supplied, the default is ascending.
- `sort_priority` _Union[Unset, int]_ - To enable sorting on a specific Field, provide a sortPriority for that field,
  and that field will be sorted. The sortPriority provides a ranking of how to sort fields when multiple fields
  are being sorted. The highest priority (lowest number) field is sorted first. If only one field is being sorted,
  then any value may be used for sortPriority. SortPriority should be an integer greater than 0.

<a id="models.simple_filter_field"></a>

# models.simple\_filter\_field

<a id="models.simple_filter_field.SimpleFilterField"></a>

## SimpleFilterField Objects

```python
@_attrs_define
class SimpleFilterField()
```

**Attributes**:

- `field_caption` _str_ - The caption of the field to filter on.

<a id="models.sort_direction"></a>

# models.sort\_direction

<a id="models.sort_direction.SortDirection"></a>

## SortDirection Objects

```python
class SortDirection(str, Enum)
```

Sortdirection enumeration.

This enum represents the sortdirection values supported by the VizQL Data Service.

Values:
- ASC: Asc
- DESC: Desc

**Example**:

  >>> SortDirection.ASC
  SortDirection.ASC

<a id="models.tableau_error"></a>

# models.tableau\_error

<a id="models.tableau_error.TableauError"></a>

## TableauError Objects

```python
@_attrs_define
class TableauError()
```

**Attributes**:

  error_code (Union[Unset, str]):
  message (Union[Unset, str]):
  datetime_ (Union[Unset, datetime.datetime]):
  debug (Union[Unset, TableauErrorDebug]):
  tab_error_code (Union[Unset, str]):

<a id="models.tableau_error_debug"></a>

# models.tableau\_error\_debug

<a id="models.tableau_error_debug.TableauErrorDebug"></a>

## TableauErrorDebug Objects

```python
@_attrs_define
class TableauErrorDebug()
```



<a id="models.top_n_filter"></a>

# models.top\_n\_filter

<a id="models.top_n_filter.TopNFilter"></a>

## TopNFilter Objects

```python
@_attrs_define
class TopNFilter()
```

**Attributes**:

  field (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField']):
  filter_type (FilterFilterType):
- `context` _Union[Unset, bool]_ - Make the given filter a context filter, meaning that it's an independent filter.
  Any other filters that you set are defined as dependent filters because they process only the data that passes
  through the context filter. Default: False.
- `direction` _Union[Unset, TopNFilterDirection]_ - Top (ascending) or Bottom (descending) N. Default:
  TopNFilterDirection.TOP.
- `how_many` _Union[Unset, int]_ - The number of values from the top or the bottom of the given fieldToMeasure.
  field_to_measure (Union['AggregatedFilterField', 'CalculatedFilterField', 'SimpleFilterField', Unset]):

<a id="models.top_n_filter_direction"></a>

# models.top\_n\_filter\_direction

<a id="models.top_n_filter_direction.TopNFilterDirection"></a>

## TopNFilterDirection Objects

```python
class TopNFilterDirection(str, Enum)
```

Topnfilterdirection enumeration.

This enum represents the topnfilterdirection values supported by the VizQL Data Service.

Values:
- BOTTOM: Bottom
- TOP: Top

**Example**:

  >>> TopNFilterDirection.BOTTOM
  TopNFilterDirection.BOTTOM

