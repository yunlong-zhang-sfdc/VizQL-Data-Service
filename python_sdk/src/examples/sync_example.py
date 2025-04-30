import argparse
import os
import sys
from pprint import pprint

import tableauserverclient as TSC

from openapi_client.models.query_request import QueryRequest
from openapi_client.models.read_metadata_request import ReadMetadataRequest
from src.api.EndPoints import EndPoints
from src.api.HTTPHeaders import default_headers
from src.api.SyncHTTPClient import SyncHTTPClient
from src.utils import file_util

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def main():
    parser = argparse.ArgumentParser(
        description="Calls the VizQL Data Service query_datasource and read_metadata APIs synchronously"
    )
    parser.add_argument("--server", "-s", help="server address")
    parser.add_argument("--site", "-S", help="site name")
    parser.add_argument("--user", "-user", help="user name")
    parser.add_argument("--password", "-password", help="password")
    args = parser.parse_args()
    tableau_auth = TSC.TableauAuth(args.user, args.password, "")
    server = TSC.Server(args.server)
    headers = default_headers()
    client = SyncHTTPClient()
    with server.auth.sign_in(tableau_auth):
        headers.set_tableau_auth(server.auth_token)
        all_datasources, pagination_item = server.datasources.get()
        print(f"\nThere are {pagination_item.total_available} datasources on site: ")
        if all_datasources:
            sample_datasource = all_datasources[0]
            print(f"{sample_datasource.name} with luid -> {sample_datasource.id}")
        sample_superstore_luid = [
            ds.id for ds in all_datasources if ds.name == "Superstore Datasource"
        ][0]
        print(f"Using {sample_datasource.name} with id {sample_superstore_luid}")

        # sample query_datasource
        query_request_json = file_util.read_json("./", "query_request.json")
        query_request = QueryRequest.from_json(query_request_json)
        query_request.datasource.datasource_luid = sample_superstore_luid
        response = client.query_datasource(
            args.server + EndPoints.VIZQL_DATA_SERVICE_URL,
            headers.to_dict(),
            query_request,
        )
        if response:
            print("Response for query_datasource request: ")
            pprint(response.data)

        # sample read metadata
        readmetadata_request_json = file_util.read_json(
            "./", "read_metadata_request.json"
        )
        read_metadata_request = ReadMetadataRequest.from_json(readmetadata_request_json)
        read_metadata_request.datasource.datasource_luid = sample_superstore_luid
        response = client.read_metadata(
            args.server + EndPoints.VIZQL_DATA_SERVICE_URL,
            headers.to_dict(),
            read_metadata_request,
        )
        if response:
            print("Response for read_metadata request: ")
            pprint(response.data)


if __name__ == "__main__":
    main()
