import argparse
import inspect
import traceback

from src import Datasource, Server

SAMPLE_DATASOURCE = "Superstore Datasource"


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


def list_datasources_and_get_luid(server: Server):
    all_datasources, pagination_item = server.get_datasources()
    print(f"\nThere are {pagination_item.total_available} datasources on site:")
    for ds in all_datasources:
        print(f"- {ds.name} (LUID: {ds.id})")

    matching_datasources = [
        ds for ds in all_datasources if ds.name == SAMPLE_DATASOURCE
    ]
    if not matching_datasources:
        raise ValueError(f"Datasource named '{SAMPLE_DATASOURCE}' not found.")

    selected_ds = matching_datasources[0]
    print(f"\nUsing '{selected_ds.name}' with ID: {selected_ds.id}")
    return selected_ds.id


def create_datasource(luid: str) -> Datasource:
    """Create a Datasource object with the given LUID."""
    return Datasource(datasource_luid=luid)


def handle_response(response, operation_name: str = "Operation"):
    """Handle API response and print detailed information.

    Args:
        response: The API response
        operation_name: Name of the operation for logging
    """
    print(f"\n=== Response Details for {operation_name} ===")
    print(f"Response Status: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Body: {response.parsed}")

    if response.status_code == 401:
        print("\nAuthentication failed (401 Unauthorized)")
        print("Please check:")
        print("1. Token format is correct")
        print("2. Token is not expired")
        print("3. Token has correct permissions")
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
    frame = inspect.currentframe()
    if frame:
        print("\n=== Current Frame Info ===")
        print(f"File: {frame.f_code.co_filename}")
        print(f"Line: {frame.f_lineno}")
        print(f"Function: {frame.f_code.co_name}")
        print("\nLocal Variables:")
        for name, value in frame.f_locals.items():
            print(f"  {name}: {type(value)} = {value}")
