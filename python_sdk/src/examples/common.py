import argparse
import inspect
import traceback
from typing import Union

import tableauserverclient as TSC

from openapi_client.client import AuthenticatedClient
from openapi_client.models import Datasource

X_TABLEAU_AUTH = "X-Tableau-Auth"
API_SUBDOMAIN = "/api/v1/vizql-data-service"


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Calls the VizQL Data Service query_datasource and read_metadata APIs asynchronously"
    )
    parser.add_argument("--server", "-s", help="Server address")
    parser.add_argument("--site", "-S", help="Site name")
    parser.add_argument("--user", "-u", help="User name")
    parser.add_argument("--password", "-p", help="Password")
    parser.add_argument("--pat_name", "-n", help="Personal Access Token Name")
    parser.add_argument("--pat_secret", "-t", help="Personal Access Token Secret")
    return parser.parse_args()


def list_datasources_and_get_luid(server):
    target_name = "Superstore Datasource"
    all_datasources, pagination_item = server.datasources.get()
    print(f"\nThere are {pagination_item.total_available} datasources on site:")
    for ds in all_datasources:
        print(f"- {ds.name} (luid: {ds.id})")

    matching_datasources = [ds for ds in all_datasources if ds.name == target_name]
    if not matching_datasources:
        raise ValueError(f"Datasource named '{target_name}' not found.")

    selected_ds = matching_datasources[0]
    print(f"\nUsing '{selected_ds.name}' with ID: {selected_ds.id}")
    return selected_ds.id


def construct_tableau_auth(
    args: argparse.Namespace,
) -> Union[TSC.PersonalAccessTokenAuth, TSC.TableauAuth]:
    if args.pat_name and args.pat_secret:
        return TSC.PersonalAccessTokenAuth(
            token_name=args.pat_name,
            personal_access_token=args.pat_secret,
            site_id=args.site or "",
        )
    elif args.user and args.password:
        return TSC.TableauAuth(args.user, args.password, site_id=args.site or "")
    else:
        raise ValueError(
            "User must provide either a username/password or a personal access token."
        )


def create_authenticated_client(
    server: TSC.Server, args: argparse.Namespace
) -> AuthenticatedClient:
    """Create an authenticated client with proper server URL."""
    server_url = (
        args.server if args.server.startswith("http") else f"http://{args.server}"
    )
    base_url = f"{server_url}{API_SUBDOMAIN}"

    print("\n=== Client Configuration ===")
    print(f"Server URL: {server_url}")
    print(f"Base URL: {base_url}")
    print(f"Auth Token: {server.auth_token}")
    print(f"Auth Header: {X_TABLEAU_AUTH}")

    client = AuthenticatedClient(
        base_url=base_url,
        token=server.auth_token,
        prefix="",
        auth_header_name=X_TABLEAU_AUTH,
    )

    print("\n=== Client Created ===")
    print(f"Client Base URL: {client._base_url}")
    print(f"Client Token: {client.token}")
    print(f"Client Auth Header: {client.auth_header_name}")

    return client


def create_datasource(luid: str) -> Datasource:
    """Create a Datasource object with the given LUID."""
    return Datasource(datasource_luid=luid)


def handle_response(response, operation_name: str = "Operation"):
    """Handle API response and print detailed information.

    Args:
        response: The API response
        operation_name: Name of the operation for logging
    """
    print(f"\nResponse Status: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Body: {response.parsed}")

    if response.status_code == 401:
        print("\nAuthentication failed (401 Unauthorized)")
        print("Please check:")
        print("1. Token format is correct")
        print("2. Token is not expired")
        print("3. Token has correct permissions")
        print("4. Token has correct permissions")
        print(
            "5. Make sure all API calls are executed within the 'with server.auth.sign_in(tableau_auth):' scope"
        )
    elif response.status_code != 200:
        print(f"\nRequest failed with status code: {response.status_code}")


def handle_error(e, operation_name: str = "Operation"):
    """Handle exceptions and print detailed information.

    Args:
        e: The exception
        operation_name: Name of the operation for logging
    """
    print(f"\n=== Error Details for {operation_name} ===")
    print(f"Error Type: {type(e)}")
    print(f"Error Message: {str(e)}")
    print_exception_details(e)
    print(f"{operation_name} failed: {e}")


def print_exception_details(e):
    """Print detailed exception information"""
    print("\n=== Exception Details ===")
    print(f"Exception Type: {type(e).__name__}")
    print(f"Exception Message: {str(e)}")
    print("\n=== Full Traceback ===")
    traceback.print_exc()

    # Print the current frame information
    frame = inspect.currentframe()
    if frame:
        print("\n=== Current Frame Info ===")
        print(f"File: {frame.f_code.co_filename}")
        print(f"Line: {frame.f_lineno}")
        print(f"Function: {frame.f_code.co_name}")
        print("\nLocal Variables:")
        for name, value in frame.f_locals.items():
            print(f"  {name}: {type(value)} = {value}")
