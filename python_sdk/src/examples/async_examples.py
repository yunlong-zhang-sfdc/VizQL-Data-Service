import asyncio
import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import tableauserverclient as TSC

import src.examples.common as common
from openapi_client.api.default import query_datasource, read_metadata
from openapi_client.models import QueryRequest, ReadMetadataRequest
from src.examples.payload import QUERY_FUNCTIONS


async def main():
    # Create authenticated client
    args = common.parse_arguments()
    tableau_auth = common.construct_tableau_auth(args)
    server = TSC.Server(args.server, use_server_version=True)

    with server.auth.sign_in(tableau_auth):
        print("\n=== Authentication Info ===")
        print(f"Server Auth Token: {server.auth_token}")
        print(f"Token Type: {type(server.auth_token)}")

        datasource_luid = common.list_datasources_and_get_luid(server)
        print(f"\nSelected Datasource LUID: {datasource_luid}")

        client = common.create_authenticated_client(server, args)
        datasource = common.create_datasource(datasource_luid)

        # Read metadata example
        try:
            print("\n=== Reading Metadata ===")
            metadata_request = ReadMetadataRequest(datasource=datasource)
            print(f"Request Body: {metadata_request.to_dict()}")

            metadata_response = await read_metadata.asyncio_detailed(
                client=client, body=metadata_request
            )
            common.handle_response(metadata_response, "Metadata Query")
        except Exception as e:
            common.handle_error(e, "Metadata Query")

        # Query data source examples
        for query_func in QUERY_FUNCTIONS:
            try:
                print(f"\n=== Executing Query: {query_func.__name__} ===")
                # Create query request
                query_request = QueryRequest(query=query_func(), datasource=datasource)
                print(f"Request Body: {query_request.to_dict()}")

                print("\nSending query request...")
                response = await query_datasource.asyncio_detailed(
                    client=client, body=query_request
                )
                common.handle_response(response, f"Query {query_func.__name__}")
            except Exception as e:
                common.handle_error(e, f"Query {query_func.__name__}")


if __name__ == "__main__":
    asyncio.run(main())
