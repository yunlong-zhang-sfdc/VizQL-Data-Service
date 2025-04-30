import argparse
import asyncio
from pprint import pprint

import tableauserverclient as TSC

from openapi_client import QueryRequest, ReadMetadataRequest
from src.api.AsyncHTTPClient import AsyncHTTPClient
from src.api.EndPoints import EndPoints
from src.api.HTTPHeaders import default_headers
from src.utils import file_util


async def main():
    parser = argparse.ArgumentParser(
        description="Calls the VizQL Data Service query_datasource and read_metadata APIs asynchronously"
    )
    parser.add_argument("--server", "-s", help="server address")
    parser.add_argument("--site", "-S", help="site name")
    parser.add_argument("--user", "-user", help="user name")
    parser.add_argument("--password", "-password", help="password")
    args = parser.parse_args()
    tableau_auth = TSC.TableauAuth(args.user, args.password, "")
    server = TSC.Server(args.server)
    headers = default_headers()
    client = AsyncHTTPClient()
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
        print(
            f"Using {sample_datasource.name} in the  with id {sample_superstore_luid}"
        )

        # sample query_datasource
        query_request = QueryRequest.from_json(
            file_util.read_json("payloads", "query_request.json")
        )
        query_request.datasource.datasource_luid = sample_superstore_luid
        response = await client.query_datasource(
            args.server
            + "".join(
                [EndPoints.VIZQL_DATA_SERVICE_URL, EndPoints.QUERY_DATASOURCE_ENDPOINT]
            ),
            headers.to_dict(),
            query_request,
        )
        if response:
            print("Response for query_datasource request: ")
            pprint(response.data)

        # sample read_metadata
        read_metadata_request = ReadMetadataRequest.from_json(
            file_util.read_json("payloads", "read_metadata_request.json")
        )
        read_metadata_request.datasource.datasource_luid = sample_superstore_luid
        response = await client.read_metadata(
            args.server
            + "".join(
                [EndPoints.VIZQL_DATA_SERVICE_URL, EndPoints.READ_METADATA_ENDPOINT]
            ),
            headers.to_dict(),
            read_metadata_request,
        )
        if response:
            print("Response for read_metadata request: ")
            pprint(response.data)


if __name__ == "__main__":
    asyncio.run(main())
