import asyncio
from pprint import pprint

import tableauserverclient as TSC

from openapi_client import QueryRequest, ReadMetadataRequest
from src.api.AsyncHTTPClient import AsyncHTTPClient
from src.api.EndPoints import EndPoints
from src.api.HTTPHeaders import default_headers
from src.examples import common
from src.utils import file_util


async def send_query_datasource_request(client, server_url, headers, datasource_luid):
    query_request_json = file_util.read_json("./", "query_request.json")
    query_request = QueryRequest.from_json(query_request_json)
    query_request.datasource.datasource_luid = datasource_luid
    print(query_request)
    response = await client.query_datasource(
        server_url
        + "".join(
            [EndPoints.VIZQL_DATA_SERVICE_URL, EndPoints.QUERY_DATASOURCE_ENDPOINT]
        ),
        headers.to_dict(),
        query_request.to_dict(),
    )
    if response:
        print("Response for query_datasource request: ")
        pprint(response.data)


async def send_read_metadata_request(client, server_url, headers, datasource_luid):
    readmetadata_request_json = file_util.read_json("./", "read_metadata_request.json")
    read_metadata_request = ReadMetadataRequest.from_json(readmetadata_request_json)
    read_metadata_request.datasource.datasource_luid = datasource_luid
    response = await client.read_metadata(
        server_url
        + "".join([EndPoints.VIZQL_DATA_SERVICE_URL, EndPoints.READ_METADATA_ENDPOINT]),
        headers.to_dict(),
        read_metadata_request.to_dict(),
    )
    if response:
        print("Response for read_metadata request: ")
        pprint(response.data)


async def main():
    args = common.parse_arguments()
    tableau_auth = common.construct_tableau_auth(args)
    server = TSC.Server(args.server)
    headers = default_headers()
    client = AsyncHTTPClient()

    with server.auth.sign_in(tableau_auth):
        headers.set_tableau_auth(server.auth_token)
        datasource_luid = common.list_datasources_and_get_luid(server)
        await send_query_datasource_request(
            client, args.server, headers, datasource_luid
        )
        await send_read_metadata_request(client, args.server, headers, datasource_luid)


if __name__ == "__main__":
    asyncio.run(main())
