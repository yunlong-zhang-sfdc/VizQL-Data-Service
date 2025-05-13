# VizQL Data Service Python SDK 

[![Tableau Supported](https://img.shields.io/badge/Support%20Level-Tableau%20Supported-53bd92.svg)](https://www.tableau.com/support-levels-it-and-developer-tools)
[![GitHub](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square.svg)](https://raw.githubusercontent.com/Tableau/TabPy/master/LICENSE)
[![Python SDK CI Configuration](https://github.com/tableau/VizQL-Data-Service/actions/workflows/release.yml/badge.svg)](https://github.com/tableau/VizQL-Data-Service/actions/workflows/release.yml)

The VizQL Data Service Python SDK is a lightweight client library that enables interaction with Tableau's VizQL Data Service APIs. It supports both cloud and on-premises deployments, offering both synchronous and asynchronous methods for querying the VizQL Data Service APIs.

Consider reading VizQL Data Service in the following order:
- [VizQL Data Service help documentation](https://help.tableau.com/current/api/vizql-data-service/en-us/index.html)
- [VizQL Data Service API Reference](https://help.tableau.com/current/api/vizql-data-service/en-us/reference/index.html)
- [VizQL Data Service Postman collection](https://www.postman.com/salesforce-developers/salesforce-developers/folder/jdy4gr3/vizql-data-service-queries)
- [VizQL Data Service OpenAPI Schema](https://github.com/tableau/VizQL-Data-Service/blob/main/VizQLDataServiceOpenAPISchema.json)

## 🔧 Installation
```bash
pip install vizqldataservicepythonsdk
```

## 🚀 Quick Start

### Importing Required Modules
```python
from vizqldataservicepythonsdk import (
    ReadMetadataRequest,
    QueryRequest,
    Datasource,
    Connection,
    VizQLDataServiceClient,
    Server,
    read_metadata,
    query_datasource,
    SimpleField,
    AggregatedField,
    Function,
    Query
)
```

### Setting Up Server Connection
> **Note**: Authentication methods differ between Tableau Cloud and On-premises:
> - Tableau Cloud: Only supports Personal Access Token (PAT) authentication
> - Tableau Onprem: Supports both PAT and username/password authentication
```python
# Initialize server with either user credentials or PAT (Personal Access Token)
server = Server(
    # For Tableau Cloud (online.tableau.com), HTTPS will be automatically added
    # For other servers, HTTP will be added if no protocol is specified
    url="<server-url>",
    # Option 1: User password authentication
    username="<user>",
    password="<password>"
    # ---- OR ----
    # Option 2: PAT authentication
    pat_name="<name>",
    pat_secret="<secret>",
    # Required for tableau cloud
    site_id="<site-name>"
)
```

### Configuring Data Source
```python
# Create a data source instance with optional connection parameters
datasource = Datasource(
    datasource_luid="<datasource-luid>",
    # Optional: Configure connections for external data sources
    connections=[
        Connection(
            connection_username="<connection-username>",
            connection_password="<connection-password>"
        )
    ]
)
```

### Sign in, Read metadata and query data sources
```python
with server.sign_in():
    # Define your query fields
    query = Query(
        # Example using Super Store dataset
        fields=[
            SimpleField(field_caption="Category"),
            AggregatedField(field_caption="Sales", function=Function.SUM),
        ]
    )
    client = VizQLDataServiceClient(server)

    # Step 1: Read metadata
    read_metadata_request = ReadMetadataRequest(
        datasource=datasource
    )
    read_metadata_response = read_metadata.sync_detailed(
        client=client.client, body=read_metadata_request
    )
    print(f"Read Metadata Response: {read_metadata_response.parsed}")

    # Step 2: Execute query
    query_request = QueryRequest(
        query=query, datasource=datasource
    )
    query_response = query_datasource.sync_detailed(
        client=client.client, body=query_request
    )
    print(f"Query Datasource Response: {query_response.parsed}")
```

This SDK is built using `openapi-python-cli` to generate all VizQL Data Service models. For detailed API documentation and model specifications, please refer to the [openapi_client.md](https://github.com/tableau/VizQL-Data-Service/python_sdk/openapi_client.md) file. 

> **Note**: While raw JSON requests are supported, we strongly recommend using the provided Python objects to construct requests. This approach offers several advantages:
> - Type safety and validation at compile time
> - Better IDE support with autocompletion
> - Consistent request structure
> - Easier maintenance and debugging

For comprehensive examples demonstrating various query patterns and filter combinations, please check the `src/examples` directory.

## 📘 Supported Features
- ✅ Read metadata of published Tableau datasources
- ✅ Query published datasources with selectable fields and queires supports various filters
- ✅ Synchronous and asynchronous Python client support in examples
- ✅ Authentication using Tableau username/password or Personal Access Token (PAT)
- ✅ Works with both Tableau Cloud and Tableau Server (on-prem)

## 🛠️ Requirements
- Python 3.9+
- pip 20.0+
- Tableau Server 2025.1+ or Tableau Cloud

## 🤝 Contributing
To contribute, see our [CONTRIBUTING.md](https://github.com/tableau/VizQL-Data-Service/python_sdk/CONTRIBUTING.md) Guide. A list of all our contributors to date is in [CONTRIBUTORS.md](https://github.com/tableau/VizQL-Data-Service/python_sdk/CONTRIBUTORS.md).
