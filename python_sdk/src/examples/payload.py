from datetime import date

from src.api.openapi_generated import (
    AggregatedField,
    CalculatedField,
    DateRangeType,
    Direction,
    FilterAggregatedField,
    FilterSimpleField,
    FilterType,
    Function,
    MatchFilter,
    PeriodType,
    QuantitativeDateFilter,
    QuantitativeFilterType,
    QuantitativeNumericalFilter,
    Query,
    RelativeDateFilter,
    SetFilter,
    SimpleField,
    TopNFilter,
)


def create_simple_query():
    return Query(
        fields=[
            SimpleField(fieldCaption="Category"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ]
    )


def create_custom_calculation():
    return Query(
        fields=[
            CalculatedField(
                fieldCaption="AOV", calculation="SUM([Profit])/COUNTD([Order ID])"
            ),
        ]
    )


def create_dimension_filter():
    return Query(
        fields=[
            SimpleField(fieldCaption="Ship Mode"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ],
        filters=[
            SetFilter(
                field=FilterSimpleField(fieldCaption="Ship Mode"),
                filterType=FilterType.SET,
                values=["First Class", "Standard Class"],
                exclude=False,
            )
        ],
    )


def create_quantitative_range_filter():
    return Query(
        fields=[
            SimpleField(fieldCaption="Ship Mode"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ],
        filters=[
            QuantitativeNumericalFilter(
                field=FilterAggregatedField(
                    fieldCaption="Sales", function=Function.SUM
                ),
                filterType=FilterType.QUANTITATIVE_NUMERICAL,
                quantitativeFilterType=QuantitativeFilterType.RANGE,
                min=266839,
                max=1149562,
            )
        ],
    )


def create_quantitative_date_filter():
    return Query(
        fields=[
            AggregatedField(fieldCaption="Order Date", function=Function.YEAR),
            AggregatedField(fieldCaption="Order Date", function=Function.QUARTER),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ],
        filters=[
            QuantitativeDateFilter(
                field=FilterSimpleField(fieldCaption="Order Date"),
                filterType=FilterType.QUANTITATIVE_DATE,
                quantitativeFilterType=QuantitativeFilterType.MIN,
                minDate=date(2020, 1, 1),
            )
        ],
    )


def create_relative_date_filter():
    return Query(
        fields=[
            AggregatedField(
                fieldCaption="Order Date", function=Function.YEAR, sortPriority=1
            ),
            AggregatedField(
                fieldCaption="Order Date", function=Function.MONTH, sortPriority=2
            ),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ],
        filters=[
            RelativeDateFilter(
                field=FilterSimpleField(fieldCaption="Order Date"),
                filterType=FilterType.DATE,
                periodType=PeriodType.MONTHS,
                dateRangeType=DateRangeType.CURRENT,
                anchorDate=date(2022, 1, 1),
            )
        ],
    )


def create_match_filter():
    return Query(
        fields=[
            SimpleField(fieldCaption="State/Province"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ],
        filters=[
            MatchFilter(
                field=FilterSimpleField(fieldCaption="State/Province"),
                filterType=FilterType.MATCH,
                startsWith="A",
                endsWith="a",
                contains="o",
                exclude=False,
            )
        ],
    )


def create_top_n_filter():
    return Query(
        fields=[
            SimpleField(fieldCaption="State/Province"),
            AggregatedField(fieldCaption="Profit", function=Function.SUM),
        ],
        filters=[
            TopNFilter(
                field=FilterSimpleField(fieldCaption="State/Province"),
                filterType=FilterType.TOP,
                howMany=10,
                fieldToMeasure=FilterAggregatedField(
                    fieldCaption="Profit", function=Function.SUM
                ),
                direction=Direction.TOP,
            )
        ],
    )


def create_multiple_dimension_filters():
    return Query(
        fields=[
            SimpleField(fieldCaption="Ship Mode"),
            SimpleField(fieldCaption="Segment"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ],
        filters=[
            SetFilter(
                field=FilterSimpleField(fieldCaption="Ship Mode"),
                filterType=FilterType.SET,
                values=["First Class", "Standard Class"],
                exclude=False,
            ),
            SetFilter(
                field=FilterSimpleField(fieldCaption="Segment"),
                filterType=FilterType.SET,
                values=["Consumer"],
                exclude=True,
            ),
        ],
    )


def create_multiple_min_max_numeric_filters():
    return Query(
        fields=[
            SimpleField(fieldCaption="Ship Mode"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
            AggregatedField(fieldCaption="Profit", function=Function.SUM),
        ],
        filters=[
            QuantitativeNumericalFilter(
                field=FilterAggregatedField(
                    fieldCaption="Sales", function=Function.SUM
                ),
                filterType=FilterType.QUANTITATIVE_NUMERICAL,
                quantitativeFilterType=QuantitativeFilterType.MIN,
                min=266839,
            ),
            QuantitativeNumericalFilter(
                field=FilterAggregatedField(
                    fieldCaption="Profit", function=Function.SUM
                ),
                filterType=FilterType.QUANTITATIVE_NUMERICAL,
                quantitativeFilterType=QuantitativeFilterType.MAX,
                max=164098,
            ),
        ],
    )


def create_dimension_numeric_filters():
    return Query(
        fields=[
            SimpleField(fieldCaption="Ship Mode"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ],
        filters=[
            SetFilter(
                field=FilterSimpleField(fieldCaption="Ship Mode"),
                filterType=FilterType.SET,
                values=["First Class", "Standard Class"],
                exclude=True,
            ),
            QuantitativeNumericalFilter(
                field=FilterAggregatedField(
                    fieldCaption="Profit", function=Function.SUM
                ),
                filterType=FilterType.QUANTITATIVE_NUMERICAL,
                quantitativeFilterType=QuantitativeFilterType.MIN,
                min=40000,
            ),
        ],
    )


def create_context_filter():
    return Query(
        fields=[
            SimpleField(fieldCaption="Sub-Category"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
        ],
        filters=[
            TopNFilter(
                field=FilterSimpleField(fieldCaption="Sub-Category"),
                filterType=FilterType.TOP,
                howMany=10,
                fieldToMeasure=FilterAggregatedField(
                    fieldCaption="Sales", function=Function.SUM
                ),
                direction=Direction.TOP,
            ),
            SetFilter(
                field=FilterSimpleField(fieldCaption="Category"),
                filterType=FilterType.SET,
                values=["Furniture"],
                exclude=False,
                context=True,
            ),
        ],
    )


def create_numeric_date_dimension_filters():
    return Query(
        fields=[
            SimpleField(fieldCaption="Order Date"),
            AggregatedField(fieldCaption="Sales", function=Function.SUM),
            SimpleField(fieldCaption="Ship Mode"),
        ],
        filters=[
            QuantitativeNumericalFilter(
                field=FilterAggregatedField(
                    fieldCaption="Sales", function=Function.SUM
                ),
                filterType=FilterType.QUANTITATIVE_NUMERICAL,
                quantitativeFilterType=QuantitativeFilterType.RANGE,
                min=10,
                max=63,
            ),
            RelativeDateFilter(
                field=FilterSimpleField(fieldCaption="Order Date"),
                filterType=FilterType.DATE,
                periodType=PeriodType.MONTHS,
                dateRangeType=DateRangeType.NEXTN,
                rangeN=3,
                anchorDate=date(2022, 1, 1),
            ),
            SetFilter(
                field=FilterSimpleField(fieldCaption="Ship Mode"),
                filterType=FilterType.SET,
                values=["First Class"],
                exclude=False,
            ),
        ],
    )


QUERY_FUNCTIONS = [
    create_simple_query,
    create_custom_calculation,
    create_dimension_filter,
    create_quantitative_range_filter,
    create_quantitative_date_filter,
    create_relative_date_filter,
    create_match_filter,
    create_top_n_filter,
    create_multiple_dimension_filters,
    create_multiple_min_max_numeric_filters,
    create_dimension_numeric_filters,
    create_context_filter,
    create_numeric_date_dimension_filters,
]
