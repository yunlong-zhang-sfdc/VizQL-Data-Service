from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.filter_filter_type import FilterFilterType
from ..models.relative_date_filter_date_range_type import RelativeDateFilterDateRangeType
from ..models.relative_date_filter_period_type import RelativeDateFilterPeriodType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.filter_by_calculation import FilterByCalculation
  from ..models.filter_by_caption_function import FilterByCaptionFunction
  from ..models.filter_by_caption import FilterByCaption





T = TypeVar("T", bound="RelativeDateFilter")



@_attrs_define
class RelativeDateFilter:
    """ 
        Attributes:
            field (Union['FilterByCalculation', 'FilterByCaption', 'FilterByCaptionFunction']):
            filter_type (FilterFilterType):
            period_type (RelativeDateFilterPeriodType): The units of time in the relative date range.
            date_range_type (RelativeDateFilterDateRangeType): The direction in the relative date range.
            context (Union[Unset, bool]): Make the given filter a context filter, meaning that it's an independent filter.
                Any other filters that you set are defined as dependent filters because they process only the data that passes
                through the context filter. Default: False.
            range_n (Union[Unset, int]): When dateRangeType is LASTN or NEXTN, this is the N value (how many years, months,
                etc.).
            anchor_date (Union[Unset, datetime.date]): If a value for this field isn't provided, the value defaults to
                today.
            include_nulls (Union[Unset, bool]): Should nulls be returned or not. If a value isn't provided, the default is
                to not include null values.
     """

    field: Union['FilterByCalculation', 'FilterByCaption', 'FilterByCaptionFunction']
    filter_type: FilterFilterType
    period_type: RelativeDateFilterPeriodType
    date_range_type: RelativeDateFilterDateRangeType
    context: Union[Unset, bool] = False
    range_n: Union[Unset, int] = UNSET
    anchor_date: Union[Unset, datetime.date] = UNSET
    include_nulls: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_by_calculation import FilterByCalculation
        from ..models.filter_by_caption_function import FilterByCaptionFunction
        from ..models.filter_by_caption import FilterByCaption
        field: dict[str, Any]
        if isinstance(self.field, FilterByCaption):
            field = self.field.to_dict()
        elif isinstance(self.field, FilterByCaptionFunction):
            field = self.field.to_dict()
        else:
            field = self.field.to_dict()


        filter_type = self.filter_type.value

        period_type = self.period_type.value

        date_range_type = self.date_range_type.value

        context = self.context

        range_n = self.range_n

        anchor_date: Union[Unset, str] = UNSET
        if not isinstance(self.anchor_date, Unset):
            anchor_date = self.anchor_date.isoformat()

        include_nulls = self.include_nulls


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "filterType": filter_type,
            "periodType": period_type,
            "dateRangeType": date_range_type,
        })
        if context is not UNSET:
            field_dict["context"] = context
        if range_n is not UNSET:
            field_dict["rangeN"] = range_n
        if anchor_date is not UNSET:
            field_dict["anchorDate"] = anchor_date
        if include_nulls is not UNSET:
            field_dict["includeNulls"] = include_nulls

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_by_calculation import FilterByCalculation
        from ..models.filter_by_caption_function import FilterByCaptionFunction
        from ..models.filter_by_caption import FilterByCaption
        d = dict(src_dict)
        def _parse_field(data: object) -> Union['FilterByCalculation', 'FilterByCaption', 'FilterByCaptionFunction']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_field_type_0 = FilterByCaption.from_dict(data)



                return componentsschemas_filter_field_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_field_type_1 = FilterByCaptionFunction.from_dict(data)



                return componentsschemas_filter_field_type_1
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_field_type_2 = FilterByCalculation.from_dict(data)



            return componentsschemas_filter_field_type_2

        field = _parse_field(d.pop("field"))


        filter_type = FilterFilterType(d.pop("filterType"))




        period_type = RelativeDateFilterPeriodType(d.pop("periodType"))




        date_range_type = RelativeDateFilterDateRangeType(d.pop("dateRangeType"))




        context = d.pop("context", UNSET)

        range_n = d.pop("rangeN", UNSET)

        _anchor_date = d.pop("anchorDate", UNSET)
        anchor_date: Union[Unset, datetime.date]
        if isinstance(_anchor_date,  Unset):
            anchor_date = UNSET
        else:
            anchor_date = isoparse(_anchor_date).date()




        include_nulls = d.pop("includeNulls", UNSET)

        relative_date_filter = cls(
            field=field,
            filter_type=filter_type,
            period_type=period_type,
            date_range_type=date_range_type,
            context=context,
            range_n=range_n,
            anchor_date=anchor_date,
            include_nulls=include_nulls,
        )


        relative_date_filter.additional_properties = d
        return relative_date_filter

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
