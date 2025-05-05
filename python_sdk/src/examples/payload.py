from datetime import date

from openapi_client.models import (
    FieldWithCalculation,
    FieldWithCaption,
    FieldWithCaptionFunction,
    FilterFieldWithCaption,
    FilterFieldWithCaptionFunction,
    FilterFilterType,
    Function,
    MatchFilter,
    QuantitativeDateFilter,
    QuantitativeFilterBaseQuantitativeFilterType,
    QuantitativeNumericalFilter,
    Query,
    RelativeDateFilter,
    RelativeDateFilterDateRangeType,
    RelativeDateFilterPeriodType,
    SetFilter,
    TopNFilter,
    TopNFilterDirection,
)


def create_simple_query():
    return Query(
        fields=[
            FieldWithCaption(field_caption="Category"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ]
    )


def create_custom_calculation():
    return Query(
        fields=[
            FieldWithCalculation(
                field_caption="AOV", calculation="SUM([Profit])/COUNTD([Order ID])"
            ),
        ]
    )


def create_dimension_filter():
    return Query(
        fields=[
            FieldWithCaption(field_caption="Ship Mode"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ],
        filters=[
            SetFilter(
                field=FilterFieldWithCaption(field_caption="Ship Mode"),
                filter_type=FilterFilterType.SET,
                values=["First Class", "Standard Class"],
                exclude=False,
            )
        ],
    )


def create_quantitative_range_filter():
    return Query(
        fields=[
            FieldWithCaption(field_caption="Ship Mode"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ],
        filters=[
            QuantitativeNumericalFilter(
                field=FilterFieldWithCaptionFunction(
                    field_caption="Sales", function=Function.SUM
                ),
                filter_type=FilterFilterType.QUANTITATIVE_NUMERICAL,
                quantitative_filter_type=QuantitativeFilterBaseQuantitativeFilterType.RANGE,
                min_=266839,
                max_=1149562,
            )
        ],
    )


def create_quantitative_date_filter():
    return Query(
        fields=[
            FieldWithCaptionFunction(
                field_caption="Order Date", function=Function.YEAR
            ),
            FieldWithCaptionFunction(
                field_caption="Order Date", function=Function.QUARTER
            ),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ],
        filters=[
            QuantitativeDateFilter(
                field=FilterFieldWithCaption(field_caption="Order Date"),
                filter_type=FilterFilterType.QUANTITATIVE_DATE,
                quantitative_filter_type=QuantitativeFilterBaseQuantitativeFilterType.MIN,
                min_date=date(2020, 1, 1),
            )
        ],
    )


def create_relative_date_filter():
    return Query(
        fields=[
            FieldWithCaptionFunction(
                field_caption="Order Date", function=Function.YEAR, sort_priority=1
            ),
            FieldWithCaptionFunction(
                field_caption="Order Date", function=Function.MONTH, sort_priority=2
            ),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ],
        filters=[
            RelativeDateFilter(
                field=FilterFieldWithCaption(field_caption="Order Date"),
                filter_type=FilterFilterType.DATE,
                period_type=RelativeDateFilterPeriodType.MONTHS,
                date_range_type=RelativeDateFilterDateRangeType.CURRENT,
                anchor_date=date(2021, 1, 1),
            )
        ],
    )


def create_match_filter():
    return Query(
        fields=[
            FieldWithCaption(field_caption="State/Province"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ],
        filters=[
            MatchFilter(
                field=FilterFieldWithCaption(field_caption="State/Province"),
                filter_type=FilterFilterType.MATCH,
                starts_with="A",
                ends_with="a",
                contains="o",
                exclude=False,
            )
        ],
    )


def create_top_n_filter():
    return Query(
        fields=[
            FieldWithCaption(field_caption="State/Province"),
            FieldWithCaptionFunction(field_caption="Profit", function=Function.SUM),
        ],
        filters=[
            TopNFilter(
                field=FilterFieldWithCaption(field_caption="State/Province"),
                filter_type=FilterFilterType.TOP,
                how_many=10,
                field_to_measure=FilterFieldWithCaptionFunction(
                    field_caption="Profit", function=Function.SUM
                ),
                direction=TopNFilterDirection.TOP,
            )
        ],
    )


def create_multiple_dimension_filters():
    return Query(
        fields=[
            FieldWithCaption(field_caption="Ship Mode"),
            FieldWithCaption(field_caption="Segment"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ],
        filters=[
            SetFilter(
                field=FilterFieldWithCaption(field_caption="Ship Mode"),
                filter_type=FilterFilterType.SET,
                values=["First Class", "Standard Class"],
                exclude=False,
            ),
            SetFilter(
                field=FilterFieldWithCaption(field_caption="Segment"),
                filter_type=FilterFilterType.SET,
                values=["Consumer"],
                exclude=True,
            ),
        ],
    )


def create_multiple_min_max_numeric_filters():
    return Query(
        fields=[
            FieldWithCaption(field_caption="Ship Mode"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
            FieldWithCaptionFunction(field_caption="Profit", function=Function.SUM),
        ],
        filters=[
            QuantitativeNumericalFilter(
                field=FilterFieldWithCaptionFunction(
                    field_caption="Sales", function=Function.SUM
                ),
                filter_type=FilterFilterType.QUANTITATIVE_NUMERICAL,
                quantitative_filter_type=QuantitativeFilterBaseQuantitativeFilterType.MIN,
                min_=266839,
            ),
            QuantitativeNumericalFilter(
                field=FilterFieldWithCaptionFunction(
                    field_caption="Profit", function=Function.SUM
                ),
                filter_type=FilterFilterType.QUANTITATIVE_NUMERICAL,
                quantitative_filter_type=QuantitativeFilterBaseQuantitativeFilterType.MAX,
                max_=164098,
            ),
        ],
    )


def create_dimension_numeric_filters():
    return Query(
        fields=[
            FieldWithCaption(field_caption="Ship Mode"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ],
        filters=[
            SetFilter(
                field=FilterFieldWithCaption(field_caption="Ship Mode"),
                filter_type=FilterFilterType.SET,
                values=["First Class", "Standard Class"],
                exclude=True,
            ),
            QuantitativeNumericalFilter(
                field=FilterFieldWithCaptionFunction(
                    field_caption="Profit", function=Function.SUM
                ),
                filter_type=FilterFilterType.QUANTITATIVE_NUMERICAL,
                quantitative_filter_type=QuantitativeFilterBaseQuantitativeFilterType.MIN,
                min_=400000,
            ),
        ],
    )


def create_context_filter():
    return Query(
        fields=[
            FieldWithCaption(field_caption="Sub-Category"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
        ],
        filters=[
            TopNFilter(
                field=FilterFieldWithCaption(field_caption="Sub-Category"),
                filter_type=FilterFilterType.TOP,
                how_many=10,
                field_to_measure=FilterFieldWithCaptionFunction(
                    field_caption="Sales", function=Function.SUM
                ),
                direction=TopNFilterDirection.TOP,
            ),
            SetFilter(
                field=FilterFieldWithCaption(field_caption="Category"),
                filter_type=FilterFilterType.SET,
                values=["Furniture"],
                exclude=False,
                context=True,
            ),
        ],
    )


def create_numeric_date_dimension_filters():
    return Query(
        fields=[
            FieldWithCaption(field_caption="Order Date"),
            FieldWithCaptionFunction(field_caption="Sales", function=Function.SUM),
            FieldWithCaption(field_caption="Ship Mode"),
        ],
        filters=[
            QuantitativeNumericalFilter(
                field=FilterFieldWithCaptionFunction(
                    field_caption="Sales", function=Function.SUM
                ),
                filter_type=FilterFilterType.QUANTITATIVE_NUMERICAL,
                quantitative_filter_type=QuantitativeFilterBaseQuantitativeFilterType.RANGE,
                min_=10,
                max_=63,
            ),
            RelativeDateFilter(
                field=FilterFieldWithCaption(field_caption="Order Date"),
                filter_type=FilterFilterType.DATE,
                period_type=RelativeDateFilterPeriodType.MONTHS,
                date_range_type=RelativeDateFilterDateRangeType.NEXTN,
                range_n=3,
                anchor_date=date(2020, 1, 1),
            ),
            SetFilter(
                field=FilterFieldWithCaption(field_caption="Ship Mode"),
                filter_type=FilterFilterType.SET,
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
