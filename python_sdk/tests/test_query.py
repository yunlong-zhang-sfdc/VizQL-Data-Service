import pytest

from openapi_client.models.aggregated_field import AggregatedField
from openapi_client.models.query_request import QueryRequest
from openapi_client.models.read_metadata_request import ReadMetadataRequest
from openapi_client.models.simple_field import SimpleField


@pytest.fixture
def sample_query_json():
    return {
        "datasource": {"datasourceLuid": "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"},
        "options": {"returnFormat": "OBJECTS"},
        "query": {
            "fields": [
                {"fieldCaption": "Category"},
                {"fieldCaption": "Sales", "function": "SUM"},
            ]
        },
    }


@pytest.fixture
def sample_query_request():
    return {
        "datasource": {"datasourceLuid": "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"},
        "query": {
            "fields": [
                {"fieldCaption": "Order Date"},
                {"fieldCaption": "Sales", "function": "SUM"},
                {"fieldCaption": "Ship Mode"},
            ],
            "filters": [
                {
                    "field": {"fieldCaption": "Sales", "function": "SUM"},
                    "filterType": "QUANTITATIVE_NUMERICAL",
                    "quantitativeFilterType": "RANGE",
                    "min": 10,
                    "max": 63,
                },
                {
                    "filterType": "DATE",
                    "field": {"fieldCaption": "Order Date"},
                    "periodType": "MONTHS",
                    "dateRangeType": "NEXTN",
                    "rangeN": 3,
                    "anchorDate": "2021-01-01",
                },
                {
                    "field": {"fieldCaption": "Ship Mode"},
                    "filterType": "SET",
                    "values": ["First Class"],
                    "exclude": False,
                },
            ],
        },
    }


def test_read_metadata_request_from_dict(sample_query_json):
    """Test creating ReadMetadataRequest instance from dictionary"""
    request = ReadMetadataRequest.from_dict(sample_query_json)
    assert request.datasource.datasource_luid == "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"
    assert request.options.return_format == "OBJECTS"
    query = request.additional_properties.get("query")
    assert len(query.get("fields")) == 2
    assert query.get("fields")[0].get("fieldCaption") == "Category"
    assert query.get("fields")[1].get("fieldCaption") == "Sales"
    assert query.get("fields")[1].get("function") == "SUM"


def test_read_metadata_request_to_dict(sample_query_json):
    """Test converting ReadMetadataRequest instance to dictionary"""
    request = ReadMetadataRequest.from_dict(sample_query_json)
    request_dict = request.to_dict()

    assert isinstance(request_dict, dict)
    assert (
        request_dict["datasource"]["datasourceLuid"]
        == "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"
    )
    assert request_dict["options"]["returnFormat"] == "OBJECTS"
    assert len(request_dict["query"]["fields"]) == 2


def test_query_request_from_dict(sample_query_request):
    """Test creating QueryRequest instance from dictionary"""
    request = QueryRequest.from_dict(sample_query_request)

    # Test datasource
    assert request.datasource.datasource_luid == "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"

    # Test fields
    assert len(request.query.fields) == 3
    assert isinstance(request.query.fields[0], SimpleField)
    assert request.query.fields[0].field_caption == "Order Date"
    assert isinstance(request.query.fields[1], AggregatedField)
    assert request.query.fields[1].field_caption == "Sales"
    assert request.query.fields[1].function == "SUM"
    assert isinstance(request.query.fields[2], SimpleField)
    assert request.query.fields[2].field_caption == "Ship Mode"

    # Test filters
    assert len(request.query.filters) == 3

    # Test quantitative filter
    quant_filter = request.query.filters[0]
    assert quant_filter.filter_type == "QUANTITATIVE_NUMERICAL"
    assert quant_filter.additional_properties.get("quantitativeFilterType") == "RANGE"
    assert quant_filter.additional_properties.get("min") == 10
    assert quant_filter.additional_properties.get("max") == 63
    assert quant_filter.field.field_caption == "Sales"
    assert quant_filter.field.function == "SUM"

    # Test date filter
    date_filter = request.query.filters[1]
    assert date_filter.filter_type == "DATE"
    assert date_filter.additional_properties.get("periodType") == "MONTHS"
    assert date_filter.additional_properties.get("dateRangeType") == "NEXTN"
    assert date_filter.additional_properties.get("rangeN") == 3
    assert date_filter.additional_properties.get("anchorDate") == "2021-01-01"
    assert date_filter.field.field_caption == "Order Date"

    # Test set filter
    set_filter = request.query.filters[2]
    assert set_filter.filter_type == "SET"
    assert set_filter.additional_properties.get("values") == ["First Class"]
    assert set_filter.additional_properties.get("exclude") is False
    assert set_filter.field.field_caption == "Ship Mode"


def test_query_request_to_dict(sample_query_request):
    """Test converting QueryRequest instance to dictionary"""
    request = QueryRequest.from_dict(sample_query_request)
    request_dict = request.to_dict()

    assert isinstance(request_dict, dict)
    assert (
        request_dict["datasource"]["datasourceLuid"]
        == "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"
    )

    # Test fields
    assert len(request_dict["query"]["fields"]) == 3
    assert request_dict["query"]["fields"][0]["fieldCaption"] == "Order Date"
    assert request_dict["query"]["fields"][1]["fieldCaption"] == "Sales"
    assert request_dict["query"]["fields"][1]["function"] == "SUM"
    assert request_dict["query"]["fields"][2]["fieldCaption"] == "Ship Mode"

    # Test filters
    assert len(request_dict["query"]["filters"]) == 3

    # Test quantitative filter
    quant_filter = request_dict["query"]["filters"][0]
    assert quant_filter["filterType"] == "QUANTITATIVE_NUMERICAL"
    assert quant_filter["quantitativeFilterType"] == "RANGE"
    assert quant_filter["min"] == 10
    assert quant_filter["max"] == 63
    assert quant_filter["field"]["fieldCaption"] == "Sales"
    assert quant_filter["field"].get("function") == "SUM"

    # Test date filter
    date_filter = request_dict["query"]["filters"][1]
    assert date_filter["filterType"] == "DATE"
    assert date_filter["periodType"] == "MONTHS"
    assert date_filter["dateRangeType"] == "NEXTN"
    assert date_filter["rangeN"] == 3
    assert date_filter["anchorDate"] == "2021-01-01"
    assert date_filter["field"]["fieldCaption"] == "Order Date"

    # Test set filter
    set_filter = request_dict["query"]["filters"][2]
    assert set_filter["filterType"] == "SET"
    assert set_filter["values"] == ["First Class"]
    assert set_filter["exclude"] is False
    assert set_filter["field"]["fieldCaption"] == "Ship Mode"
