# import argparse
# import os
# import sys
# from pprint import pprint
# from typing import Union

# # Add project root to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# import tableauserverclient as TSC

# from openapi_client.models import (
#     Datasource,
#     Field,
#     FieldOneOf,
#     FieldOneOf1,
#     FieldOneOf2,
#     FilterField,
#     FilterFieldOneOf,
#     FilterFieldOneOf1,
#     FilterFieldOneOf2,
#     Function,
#     Query,
#     QueryRequest,
#     SetFilter,
#     TopNFilter,
# )
# from src.api.EndPoints import EndPoints
# from src.api.HTTPHeaders import default_headers
# from src.api.SyncHTTPClient import SyncHTTPClient


# def list_datasources_and_get_luid(server):
#     target_name = "Superstore Datasource"
#     all_datasources, pagination_item = server.datasources.get()
#     print(f"\nThere are {pagination_item.total_available} datasources on site:")
#     for ds in all_datasources:
#         print(f"- {ds.name} (luid: {ds.id})")

#     matching_datasources = [ds for ds in all_datasources if ds.name == target_name]
#     if not matching_datasources:
#         raise ValueError(f"Datasource named '{target_name}' not found.")

#     selected_ds = matching_datasources[0]
#     print(f"\nUsing '{selected_ds.name}' with ID: {selected_ds.id}")
#     return selected_ds.id


# def parse_arguments():
#     parser = argparse.ArgumentParser(
#         description="Calls the VizQL Data Service query_datasource and read_metadata APIs asynchronously"
#     )
#     parser.add_argument("--server", "-s", help="Server address")
#     parser.add_argument("--site", "-S", help="Site name")
#     parser.add_argument("--user", "-u", help="User name")
#     parser.add_argument("--password", "-p", help="Password")
#     parser.add_argument("--pat_name", "-n", help="Personal Access Token Name")
#     parser.add_argument("--pat_secret", "-t", help="Personal Access Token Secret")
#     return parser.parse_args()


# def construct_tableau_auth(
#     args: argparse.Namespace,
# ) -> Union[TSC.PersonalAccessTokenAuth, TSC.TableauAuth]:
#     if args.pat_name and args.pat_secret:
#         return TSC.PersonalAccessTokenAuth(
#             token_name=args.pat_name,
#             personal_access_token=args.pat_secret,
#             site_id=args.site or "",
#         )
#     elif args.user and args.password:
#         return TSC.TableauAuth(args.user, args.password, site_id=args.site or "")
#     else:
#         raise ValueError(
#             "User must provide either a username/password or a personal access token."
#         )


# def main():
#     # Create authenticated client
#     args = parse_arguments()
#     tableau_auth = construct_tableau_auth(args)
#     server = TSC.Server(args.server, use_server_version=True)

#     headers = default_headers()
#     client = SyncHTTPClient()

#     with server.auth.sign_in(tableau_auth):
#         print("\n=== Authentication Info ===")
#         print(f"Server Auth Token: {server.auth_token}")
#         print(f"Token Type: {type(server.auth_token)}")

#         headers.set_tableau_auth(server.auth_token)
#         datasource_luid = list_datasources_and_get_luid(server)
#         print(f"\nSelected Datasource LUID: {datasource_luid}")

#         client = SyncHTTPClient()
#         datasource = Datasource(datasource_luid=datasource_luid)

#         # Create query request
#         query = Query(
#             fields=[
#                 FieldOneOf(field_caption="Sub-Category"),
#                 FieldOneOf1(field_caption="Sales", function=Function.SUM),
#             ],
#             filters=[
#                 TopNFilter(
#                     field=FilterFieldOneOf(field_caption="Sub-Category"),
#                     filter_type="TOP",
#                     how_many=10,
#                     field_to_measure=FilterFieldOneOf1(
#                         field_caption="Sales", function=Function.SUM
#                     ),
#                     direction="TOP",
#                 ),
#                 SetFilter(
#                     field=FilterFieldOneOf(field_caption="Category"),
#                     filter_type="SET",
#                     values=["Furniture"],
#                     exclude=False,
#                     context=True,
#                 ),
#             ],
#         )
#         print(query.to_dict())
#         query_request = QueryRequest(query=query, datasource=datasource)

#         print("\n=== Executing Query ===")
#         print(f"Request Body: {query_request.to_dict()}")
#         print("\nSending query request...")
#         response = client.query_datasource(
#             args.server + EndPoints.VIZQL_DATA_SERVICE_URL,
#             headers.to_dict(),
#             query_request,
#         )
#         if response:
#             print("Response for request: ")
#             pprint(response.model_dump_json(indent=4))


# if __name__ == "__main__":
#     main()
