from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.filter_filter_type import FilterFilterType
from ..models.quantitative_filter_base_quantitative_filter_type import QuantitativeFilterBaseQuantitativeFilterType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.filter_by_calculation import FilterByCalculation
  from ..models.filter_by_caption_function import FilterByCaptionFunction
  from ..models.filter_by_caption import FilterByCaption





T = TypeVar("T", bound="QuantitativeFilterBase")



@_attrs_define
class QuantitativeFilterBase:
    """ 
        Attributes:
            field (Union['FilterByCalculation', 'FilterByCaption', 'FilterByCaptionFunction']):
            filter_type (FilterFilterType):
            quantitative_filter_type (QuantitativeFilterBaseQuantitativeFilterType):
            context (Union[Unset, bool]): Make the given filter a context filter, meaning that it's an independent filter.
                Any other filters that you set are defined as dependent filters because they process only the data that passes
                through the context filter. Default: False.
            include_nulls (Union[Unset, bool]): Should nulls be returned or not. Only applies to RANGE, MIN, and MAX
                filters. If not provided, the default is to not include null values.
     """

    field: Union['FilterByCalculation', 'FilterByCaption', 'FilterByCaptionFunction']
    filter_type: FilterFilterType
    quantitative_filter_type: QuantitativeFilterBaseQuantitativeFilterType
    context: Union[Unset, bool] = False
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

        quantitative_filter_type = self.quantitative_filter_type.value

        context = self.context

        include_nulls = self.include_nulls


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "filterType": filter_type,
            "quantitativeFilterType": quantitative_filter_type,
        })
        if context is not UNSET:
            field_dict["context"] = context
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




        quantitative_filter_type = QuantitativeFilterBaseQuantitativeFilterType(d.pop("quantitativeFilterType"))




        context = d.pop("context", UNSET)

        include_nulls = d.pop("includeNulls", UNSET)

        quantitative_filter_base = cls(
            field=field,
            filter_type=filter_type,
            quantitative_filter_type=quantitative_filter_type,
            context=context,
            include_nulls=include_nulls,
        )


        quantitative_filter_base.additional_properties = d
        return quantitative_filter_base

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
