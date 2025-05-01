# VizQL Data Service Python SDK 

[![Tableau Supported](https://img.shields.io/badge/Support%20Level-Tableau%20Supported-53bd92.svg)](https://www.tableau.com/support-levels-it-and-developer-tools)
[![GitHub](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://raw.githubusercontent.com/Tableau/TabPy/master/LICENSE)
[![Python SDK CI Configuration](https://github.com/tableau/VizQL-Data-Service/actions/workflows/python_gitlab_ci.yml/badge.svg)](https://github.com/tableau/VizQL-Data-Service/actions/workflows/python_gitlab_ci.yml)

The VizQL Data Service Python SDK is a lightweight client library that enables interaction with Tableau's VizQL Data Service APIs. It supports both cloud and on-premises deployments, offering both synchronous and asynchronous methods for querying the VizQL Data Service APIs.

Consider rieading VizQL Data Service in the following order:
- [VizQL Data Service help documentation](https://help.tableau.com/current/api/vizql-data-service/en-us/index.html)
- [VizQL Data Service API Reference](https://help.tableau.com/current/api/vizql-data-service/en-us/reference/index.html)
- [VizQL Data Service Postman collection](https://www.postman.com/salesforce-developers/salesforce-developers/folder/jdy4gr3/vizql-data-service-queries)
- [VizQL Data Service OpenAPI Schema](https://github.com/tableau/VizQL-Data-Service/blob/main/VizQLDataServiceOpenAPISchema.json)

## 🔧 Installationion
```bash
pip install vizql-data-service-python-sdk
```

## 🚀 Quick start

```python
from openapi_client.models.query_request import QueryRequest
from src.models.user import User
from src.models.server import Server
from src.utils import file_util
from src.client import Client

# Using Tableau server password auth
user = User.from_password('<username>', '<password>')
# Using Tableau server PAT auth
user = User.from_pat('<tokenname>', '<pat>')
server = Server('http://localhost', '<sitename>') # Leave empty for default site

# Replace datasource LUID and reate query request
query_request_json = '{"datasource": {"datasourceLuid": "<datasource-luid>"}, "options": {"returnFormat": "OBJECTS"}, "query": {"fields": [{"fieldCaption": "Category"}, {"fieldCaption": "Sales", "function": "SUM"}]}}'
# OR from file
# query_request_json = file_util.read_json('src/examples', 'query_request.json')

query_request = QueryRequest.from_json(query_request_json)
client = Client(user, server)
# Synchronous request
client.query_datasource(query_request)
# Asynchronous request
asyncio.run(client.query_datasource(query_request, False))
```

## 📘 Supported Features
- ✅ Query published datasources with selectable fields and filters
- ✅ Read metadata of published Tableau datasources
- ✅ Synchronous and asynchronous Python clients (SyncHTTPClient and AsyncHTTPClient)
- ✅ Authentication using Tableau username/password or Personal Access Token (PAT)
- ✅ Works with both Tableau Cloud and Tableau Server (on-prem)

## 🛠️ Requirement
- Python 3.9+

## 🤝 Contributing
To contribute, see our [CONTRIBUTING.md](https://github.com/tableau/VizQL-Data-Service/python_sdk/CONTRIBUTING.md) Guide. A list of all our contributors to date is in [CONTRIBUTORS.md](https://github.com/tableau/VizQL-Data-Service/python_sdk/CONTRIBUTORS.md).
