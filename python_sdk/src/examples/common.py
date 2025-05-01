import argparse
from typing import Union

import tableauserverclient as TSC


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Calls the VizQL Data Service query_datasource and read_metadata APIs asynchronously"
    )
    parser.add_argument("--server", "-s", help="Server address")
    parser.add_argument("--site", "-S", help="Site name")
    parser.add_argument("--user", "-user", help="User name")
    parser.add_argument("--password", "-password", help="Password")
    parser.add_argument("--pat-name", "-pat-name", help="Personal Access Token Name")
    parser.add_argument(
        "--pat-secret", "-pat-secret", help="Personal Access Token Secret"
    )
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
        return TSC.TableauAuth(
            username=args.user, password=args.password, site_id=args.site or ""
        )
    else:
        raise ValueError(
            "User must provide either a username/password or a personal access token."
        )
