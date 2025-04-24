# VizQL Data Service Python SDK 

[![Tableau Supported](https://img.shields.io/badge/Support%20Level-Tableau%20Supported-53bd92.svg)](https://www.tableau.com/support-levels-it-and-developer-tools)
[![GitHub](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://raw.githubusercontent.com/Tableau/TabPy/master/LICENSE)

The VizQL Data Service Python SDK is a lightweight client library that enables interaction with Tableau's VizQL Data Service APIs. It supports both cloud and on-premises deployments, offering both synchronous and asynchronous methods for querying the VizQL Data Service APIs.

## Installation
TBD
```bash
pip install vizqldataservicesdk
```

## Quick Start

### Basic Usage
```python
from openapi_client.models.query_request import QueryRequest
from vizdataserviceclient.models.user import User
from vizdataserviceclient.models.server import Server
from vizdataserviceclient.utils import file_util
from vizdataserviceclient.client import Client

# Initialize client
user = User('<username>', '<password>', '')
server = Server('http://localhost', '<sitename>')

# Replace datasource LUID and reate query request
query_request_json = '{"datasource": {"datasourceLuid": "<datasource-luid>"}, "options": {"returnFormat": "OBJECTS"}, "query": {"fields": [{"fieldCaption": "Category"}, {"fieldCaption": "Sales", "function": "SUM"}]}}'
# OR from file
# query_request_json = file_util.read_json('examples/payloads', 'query_request.json')

query_request = QueryRequest.from_json(query_request_json)
client = Client(user, server)
client.query_datasource(query_request)
```

### Development Setup
1. Clone repository
   ```bash
   git clone https://github.com/tableau/VizQL-Data-Service.git
   ```

2. Create virtual environment:
   ```bash
   cd VizQL-Data-Service/python-sdk
   python -m venv --system-site-packages venv
   venv\Scripts\activate
   python setup.py install
   ```

3. Generate OpenAPI client:
   ```bash
   pip install openapi-generator-cli
   openapi-generator-cli generate -i ../VizQLDataServiceOpenAPISchema.json -g python -o openapi_client --additional-properties=generateSourceCodeOnly=true,packageName=openapi_client,projectName=openapi_client
   ```

4. Install SDK:
   ```bash
   cd python_sdk
   python setup.py install
   ```

### Running Examples
```bash
python .\examples\sync_example.py --user=<username> --password=<password> --server="http://localhost" >> out_sync.txt
python .\examples\async_example.py --user=<username> --password=<password> --server="http://localhost" >> out_async.txt
```

## Testing
TBD