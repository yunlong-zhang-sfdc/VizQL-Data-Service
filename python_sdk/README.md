# VizQL Data Service Python SDK 

[![Tableau Supported](https://img.shields.io/badge/Support%20Level-Tableau%20Supported-53bd92.svg)](https://www.tableau.com/support-levels-it-and-developer-tools)
[![GitHub](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://raw.githubusercontent.com/Tableau/TabPy/master/LICENSE)
[![Python SDK CI Configuration](https://github.com/tableau/VizQL-Data-Service/actions/workflows/python_gitlab_ci.yml/badge.svg)](https://github.com/tableau/VizQL-Data-Service/actions/workflows/python_gitlab_ci.yml)

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

## 🚀 Quick start
```python
from vizqldataservicepythonsdk import (
    QueryRequest,
    Datasource,
    VizQLDataServiceClient,
    Server,
    query_datasource,
    SimpleField,
    AggregatedField,
    Function,
    Query
)

server = Server(
    url="<server-url>",
    # user password authentication
    username="<user>",
    password="<password>"
    # ---- OR ----
    # PAT authentication
    pat_name="<name>",
    pat_secret="<secret>"
)
datasource_luid = "<superstore-datasource-luid>"
with server.sign_in():
    datasource = Datasource(datasource_luid=datasource_luid)
    query = Query(
        fields=[
            SimpleField(field_caption="Category"),
            AggregatedField(field_caption="Sales", function=Function.SUM),
        ]
    )
    client = VizQLDataServiceClient(server)
    query_request = QueryRequest(
        query=query, datasource=datasource
    )
    response = query_datasource.sync_detailed(
        client=client.client, body=query_request
    )
    print(f"Response: {response.parsed}")
```

This SDK is built using `openapi-python-cli` to generate all VizQL Data Service models. For detailed API documentation and model specifications, please refer to the [openapi_client.md](https://github.com/tableau/VizQL-Data-Service/python_sdk/openapi_client.md) file. 

> **Note**: While raw JSON requests are supported, we strongly recommend using the provided Python objects to construct requests. This approach offers several advantages:
> - Type safety and validation at compile time
> - Better IDE support with autocompletion
> - Consistent request structure
> - Easier maintenance and debugging
>
> For comprehensive examples demonstrating various query patterns and filter combinations, please check the `src/examples` directory.

## 📘 Supported Features
- ✅ Query published datasources with selectable fields and filters
- ✅ Read metadata of published Tableau datasources
- ✅ Synchronous and asynchronous Python clients (SyncHTTPClient and AsyncHTTPClient)
- ✅ Authentication using Tableau username/password or Personal Access Token (PAT)
- ✅ Works with both Tableau Cloud and Tableau Server (on-prem)

## 🛠️ Requirements
- Python 3.9+
- pip 20.0+
- Tableau Server 2022.1+ or Tableau Cloud

## 🤝 Contributing
To contribute, see our [CONTRIBUTING.md](https://github.com/tableau/VizQL-Data-Service/python_sdk/CONTRIBUTING.md) Guide. A list of all our contributors to date is in [CONTRIBUTORS.md](https://github.com/tableau/VizQL-Data-Service/python_sdk/CONTRIBUTORS.md).
