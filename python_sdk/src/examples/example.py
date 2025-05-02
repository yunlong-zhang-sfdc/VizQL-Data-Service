from openapi_client.openapi_client.api.default import query_datasource
from openapi_client.openapi_client.models import (
    Datasource,
    Query,
    QueryRequest,
    FieldBase,
    Filter,
    FilterFieldType0,
    FilterFieldType1,
    FilterFilterType,
    Function,
    QuantitativeFilterBase,
    QuantitativeFilterBaseQuantitativeFilterType,
    RelativeDateFilter,
    RelativeDateFilterDateRangeType,
    RelativeDateFilterPeriodType
)

import traceback
import inspect

import tableauserverclient as TSC
import common
from openapi_client.openapi_client.client import AuthenticatedClient

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
        
        # Print local variables
        print("\nLocal Variables:")
        for name, value in frame.f_locals.items():
            print(f"  {name}: {type(value)} = {value}")

def query_dat(client, datasource_luid):
    # Create fields with functions
    sales_field = FieldBase(field_caption="Sales")
    sales_field.additional_properties["function"] = "SUM"

    sales_filter_field = FilterFieldType1(field_caption="Sales", function=Function.SUM)

    # Create quantitative filter
    quantitative_filter = QuantitativeFilterBase(
        field=sales_filter_field,
        filter_type=FilterFilterType.QUANTITATIVE_NUMERICAL,
        quantitative_filter_type=QuantitativeFilterBaseQuantitativeFilterType.RANGE
    )
    quantitative_filter.additional_properties["min"] = 10
    quantitative_filter.additional_properties["max"] = 63

    # Create date filter
    date_filter = Filter(
        field=FilterFieldType0(field_caption="Order Date"),
        filter_type=FilterFilterType.DATE
    )
    date_filter.additional_properties["periodType"] = RelativeDateFilterPeriodType.MONTHS
    date_filter.additional_properties["dateRangeType"] = RelativeDateFilterDateRangeType.NEXTN
    date_filter.additional_properties["rangeN"] = 3
    date_filter.additional_properties["anchorDate"] = "2021-01-01"

    # Create set filter
    set_filter = Filter(
        field=FilterFieldType0(field_caption="Ship Mode"),
        filter_type=FilterFilterType.SET
    )
    set_filter.additional_properties["values"] = ["First Class"]
    set_filter.additional_properties["exclude"] = False

    datasource=Datasource(
        datasource_luid=datasource_luid
    )
    # Create the query request
    query_request = QueryRequest(
        datasource=datasource,
        query=Query(
            fields= [
                FieldBase(field_caption="Order Date"),
                sales_field,
                FieldBase(field_caption="Ship Mode")
            ],
            filters= [
                quantitative_filter,
                # date_filter,
                # set_filter
            ]
        )
    )
    # Synchronous query example
    try:
        response = query_datasource.sync_detailed(
            client=client,
            body=query_request
        )
        print(f"Query response: {response.parsed}")
    except Exception as e:
        print_exception_details(e)
        print(f"Query failed: {e}")

# Asynchronous query example
# async def async_query():
#     try:
#         print(query_request)
#         response = await query_datasource.asyncio_detailed(
#             client=client,
#             body=query_request
#         )
#         print(f"Async query response: {response.parsed}")
#     except Exception as e:
#         print(f"Async query failed: {e}")

# # Run the async query
# asyncio.run(async_query())

#def read_metadata(client, server_url, headers, sample_superstore_luid):
#    readmetadata_request_json = file_util.read_json("./", "read_metadata_request.json")
#    read_metadata_request = ReadMetadataRequest.from_json(readmetadata_request_json)
#    read_metadata_request.datasource.datasource_luid = sample_superstore_luid
#    response = client.read_metadata(
#        server_url + EndPoints.VIZQL_DATA_SERVICE_URL,
#        headers.to_dict(),
#        read_metadata_request,
#    )
#    if response:
#        print("Response for read_metadata request: ")
#        pprint(response.data)


def main():
    args = common.parse_arguments()
    tableau_auth = common.construct_tableau_auth(args)
    server = TSC.Server(args.server)
    #headers = default_headers()
    #client = SyncHTTPClient()

    with server.auth.sign_in(tableau_auth):
        # Create authenticated client
        client = AuthenticatedClient(
            base_url="https://prod-useast-b.online.tableau.com/api/v1/vizql-data-service",
            token=server.auth_token,
            prefix="",
            auth_header_name="X-Tableau-Auth"
        )
        #headers.set_tableau_auth(server.auth_token)
        datasource_luid = common.list_datasources_and_get_luid(server)
        query_dat(client, datasource_luid)
        #read_metadata(client, args.server, headers, datasource_luid)


if __name__ == "__main__":
    main()
