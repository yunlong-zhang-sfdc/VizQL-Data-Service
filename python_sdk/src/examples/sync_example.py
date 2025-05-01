import os
import sys
from pprint import pprint

import tableauserverclient as TSC

from openapi_client.models.query_request import QueryRequest
from openapi_client.models.read_metadata_request import ReadMetadataRequest
from src.api.EndPoints import EndPoints
from src.api.HTTPHeaders import default_headers
from src.api.SyncHTTPClient import SyncHTTPClient
from src.examples import common
from src.utils import file_util

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def query_datasource(client, server_url, headers, sample_superstore_luid):
    query_request_json = file_util.read_json("./", "query_request.json")
    query_request = QueryRequest.from_json(query_request_json)
    query_request.datasource.datasource_luid = sample_superstore_luid
    response = client.query_datasource(
        server_url + EndPoints.VIZQL_DATA_SERVICE_URL,
        headers.to_dict(),
        query_request,
    )
    if response:
        print("Response for query_datasource request: ")
        pprint(response.data)


def read_metadata(client, server_url, headers, sample_superstore_luid):
    readmetadata_request_json = file_util.read_json("./", "read_metadata_request.json")
    read_metadata_request = ReadMetadataRequest.from_json(readmetadata_request_json)
    read_metadata_request.datasource.datasource_luid = sample_superstore_luid
    response = client.read_metadata(
        server_url + EndPoints.VIZQL_DATA_SERVICE_URL,
        headers.to_dict(),
        read_metadata_request,
    )
    if response:
        print("Response for read_metadata request: ")
        pprint(response.data)


def main():
    args = common.parse_arguments()
    tableau_auth = common.construct_tableau_auth(args)
    server = TSC.Server(args.server)
    headers = default_headers()
    client = SyncHTTPClient()

    with server.auth.sign_in(tableau_auth):
        headers.set_tableau_auth(server.auth_token)
        datasource_luid = common.list_datasources_and_get_luid(server)
        query_datasource(client, args.server, headers, datasource_luid)
        read_metadata(client, args.server, headers, datasource_luid)


if __name__ == "__main__":
    main()
