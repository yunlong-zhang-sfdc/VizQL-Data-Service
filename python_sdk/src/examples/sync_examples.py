import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import tableauserverclient as TSC

import src.examples.common as common
from src.api import query_datasource, read_metadata
from src.api.client import VizQLDataServiceClient
from src.examples.payload import QUERY_FUNCTIONS
from src.openapi_client import QueryRequest, ReadMetadataRequest


def execute(args):
    server_url, auth = common.create_server(
        url=args.server,
        username=args.user,
        password=args.password,
        pat_name=args.pat_name,
        pat_secret=args.pat_secret,
        jwt_token=args.jwt_token,
        site_id=args.site,
    )
    server = TSC.Server(server_url)

    with server.auth.sign_in(auth):
        client = VizQLDataServiceClient(server_url, server, auth)
        datasource_luid = common.list_datasources_and_get_luid(server, args.verbose)
        datasource = common.create_datasource(datasource_luid)

        # Read metadata example
        try:
            print("\n=== ReadMetadata Query ===")
            metadata_request = ReadMetadataRequest(datasource=datasource)
            if args.verbose:
                print(f"Request Body: {metadata_request}")

            metadata_response = read_metadata.sync_detailed(
                client=client.client, body=metadata_request
            )
            common.handle_response(
                metadata_response, "ReadMetadata Query", args.verbose
            )
        except Exception as e:
            common.handle_error(e, "ReadMetadata Query", args.verbose)

        # Query data source examples
        for query_func in QUERY_FUNCTIONS:
            try:
                query_request = QueryRequest(query=query_func(), datasource=datasource)
                response = query_datasource.sync_detailed(
                    client=client.client, body=query_request
                )
                print(f"\n=== ExecuteQuery: {query_func.__name__} ===")
                if args.verbose:
                    print(f"Request Body: {query_request}")
                common.handle_response(
                    response, f"Query {query_func.__name__}", args.verbose
                )
            except Exception as e:
                print(f"\n=== ExecuteQuery: {query_func.__name__} ===")
                common.handle_error(e, f"Query {query_func.__name__}", args.verbose)
