import datetime

import pytest

from src.api.openapi_generated import (
    AggregatedField,
    DataType,
    DateRangeType,
    FilterType,
    Function,
    MetadataOutput,
    PeriodType,
    QuantitativeFilterType,
    QueryRequest,
    ReadMetadataRequest,
    ReturnFormat,
    SimpleField,
)


@pytest.fixture
def sample_metadata_request():
    return {
        "datasource": {"datasourceLuid": "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"},
        "options": {"returnFormat": "OBJECTS"},
    }


@pytest.fixture
def sample_metadata_output():
    return {
        "data": [
            {
                "fieldName": "Category",
                "fieldCaption": "Category",
                "dataType": "STRING",
                "logicalTableId": "table1",
            },
            {
                "fieldName": "Sales",
                "fieldCaption": "Sales",
                "dataType": "REAL",
                "logicalTableId": "table1",
            },
        ]
    }


@pytest.fixture
def sample_query_request():
    return {
        "datasource": {"datasourceLuid": "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"},
        "query": {
            "fields": [
                {"fieldCaption": "Order Date"},
                {"fieldCaption": "Sales", "function": Function.SUM},
                {"fieldCaption": "Ship Mode"},
            ],
            "filters": [
                {
                    "field": {"fieldCaption": "Sales", "function": Function.SUM},
                    "filterType": FilterType.QUANTITATIVE_NUMERICAL,
                    "quantitativeFilterType": QuantitativeFilterType.RANGE,
                    "min": 10,
                    "max": 63,
                },
                {
                    "filterType": FilterType.DATE,
                    "field": {"fieldCaption": "Order Date"},
                    "periodType": PeriodType.MONTHS,
                    "dateRangeType": DateRangeType.NEXTN,
                    "rangeN": 3,
                    "anchorDate": "2021-01-01",
                },
                {
                    "field": {"fieldCaption": "Ship Mode"},
                    "filterType": FilterType.SET,
                    "values": ["First Class"],
                    "exclude": False,
                },
            ],
        },
    }


def test_read_metadata_request_from_obj(sample_metadata_request):
    """Test creating ReadMetadataRequest instance from dictionary"""
    request = ReadMetadataRequest.model_validate(sample_metadata_request)
    assert request.datasource.datasourceLuid == "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"
    assert request.datasource.connections is None
    assert request.options.returnFormat == ReturnFormat.OBJECTS


def test_metadata_output_from_obj(sample_metadata_output):
    """Test creating MetadataOutput instance from dictionary"""
    output = MetadataOutput.model_validate(sample_metadata_output)

    # Test data field
    assert output.data is not None
    assert len(output.data) == 2

    # Test first field (Category)
    category_field = output.data[0]
    assert category_field.fieldName == "Category"
    assert category_field.fieldCaption == "Category"
    assert category_field.dataType == DataType.STRING
    assert category_field.logicalTableId == "table1"

    # Test second field (Sales)
    sales_field = output.data[1]
    assert sales_field.fieldName == "Sales"
    assert sales_field.fieldCaption == "Sales"
    assert sales_field.dataType == DataType.REAL
    assert sales_field.logicalTableId == "table1"


def test_metadata_output_to_dict(sample_metadata_output):
    """Test converting MetadataOutput instance to dictionary"""
    output = MetadataOutput.model_validate(sample_metadata_output)
    output_dict = output.model_dump()

    assert isinstance(output_dict, dict)
    assert "data" in output_dict
    assert len(output_dict["data"]) == 2

    # Test first field (Category)
    category_field = output_dict["data"][0]
    assert category_field["fieldName"] == "Category"
    assert category_field["fieldCaption"] == "Category"
    assert category_field["dataType"] == DataType.STRING
    assert category_field["logicalTableId"] == "table1"

    # Test second field (Sales)
    sales_field = output_dict["data"][1]
    assert sales_field["fieldName"] == "Sales"
    assert sales_field["fieldCaption"] == "Sales"
    assert sales_field["dataType"] == DataType.REAL
    assert sales_field["logicalTableId"] == "table1"


def test_query_request_from_dict(sample_query_request):
    """Test creating QueryRequest instance from dictionary"""
    request = QueryRequest.model_validate(sample_query_request)

    # Test datasource
    assert request.datasource.datasourceLuid == "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"

    # Test fields
    assert len(request.query.fields) == 3
    assert isinstance(request.query.fields[0].root, SimpleField)
    assert request.query.fields[0].root.fieldCaption == "Order Date"
    assert isinstance(request.query.fields[1].root, AggregatedField)
    assert request.query.fields[1].root.fieldCaption == "Sales"
    assert request.query.fields[1].root.function == Function.SUM
    assert isinstance(request.query.fields[2].root, SimpleField)
    assert request.query.fields[2].root.fieldCaption == "Ship Mode"

    # Test filters
    assert len(request.query.filters) == 3

    # Test quantitative filter
    quant_filter = request.query.filters[0].root
    assert quant_filter.filterType == FilterType.QUANTITATIVE_NUMERICAL
    assert quant_filter.quantitativeFilterType == QuantitativeFilterType.RANGE
    assert quant_filter.min == 10
    assert quant_filter.max == 63
    assert quant_filter.field.root.fieldCaption == "Sales"
    assert quant_filter.field.root.function == Function.SUM

    # Test date filter
    date_filter = request.query.filters[1].root
    assert date_filter.filterType == FilterType.DATE
    assert date_filter.periodType == PeriodType.MONTHS
    assert date_filter.dateRangeType == DateRangeType.NEXTN
    assert date_filter.rangeN == 3
    assert date_filter.anchorDate == datetime.date(2021, 1, 1)
    assert date_filter.field.root.fieldCaption == "Order Date"

    # Test set filter
    set_filter = request.query.filters[2].root
    assert set_filter.filterType == FilterType.SET
    assert set_filter.values == ["First Class"]
    assert set_filter.exclude is False
    assert set_filter.field.root.fieldCaption == "Ship Mode"


def test_query_request_to_dict(sample_query_request):
    """Test converting QueryRequest instance to dictionary"""
    request = QueryRequest.model_validate(sample_query_request)
    request_dict = request.model_dump()

    assert isinstance(request_dict, dict)
    assert (
        request_dict["datasource"]["datasourceLuid"]
        == "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"
    )

    # Test fields
    assert len(request_dict["query"]["fields"]) == 3
    assert request_dict["query"]["fields"][0]["fieldCaption"] == "Order Date"
    assert request_dict["query"]["fields"][1]["fieldCaption"] == "Sales"
    assert request_dict["query"]["fields"][1]["function"] == Function.SUM
    assert request_dict["query"]["fields"][2]["fieldCaption"] == "Ship Mode"

    # Test filters
    assert len(request_dict["query"]["filters"]) == 3

    # Test quantitative filter
    quant_filter = request_dict["query"]["filters"][0]
    assert quant_filter["filterType"] == FilterType.QUANTITATIVE_NUMERICAL
    assert quant_filter["quantitativeFilterType"] == QuantitativeFilterType.RANGE
    assert quant_filter["min"] == 10
    assert quant_filter["max"] == 63
    assert quant_filter["field"]["fieldCaption"] == "Sales"
    assert quant_filter["field"]["function"] == Function.SUM

    # Test date filter
    date_filter = request_dict["query"]["filters"][1]
    assert date_filter["filterType"] == FilterType.DATE
    assert date_filter["periodType"] == PeriodType.MONTHS
    assert date_filter["dateRangeType"] == DateRangeType.NEXTN
    assert date_filter["rangeN"] == 3
    assert date_filter["anchorDate"] == datetime.date(2021, 1, 1)
    assert date_filter["field"]["fieldCaption"] == "Order Date"

    # Test set filter
    set_filter = request_dict["query"]["filters"][2]
    assert set_filter["filterType"] == FilterType.SET
    assert set_filter["values"] == ["First Class"]
    assert set_filter["exclude"] is False
    assert set_filter["field"]["fieldCaption"] == "Ship Mode"
