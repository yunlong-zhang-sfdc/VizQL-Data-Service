from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.filter_filter_type import FilterFilterType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.filter_by_calculation import FilterByCalculation
  from ..models.filter_by_caption_function import FilterByCaptionFunction
  from ..models.filter_by_caption import FilterByCaption





T = TypeVar("T", bound="SetFilter")



@_attrs_define
class SetFilter:
    """ 
        Attributes:
            field (Union['FilterByCalculation', 'FilterByCaption', 'FilterByCaptionFunction']):
            filter_type (FilterFilterType):
            values (list[Any]): An array of values to filter on.
            context (Union[Unset, bool]): Make the given filter a context filter, meaning that it's an independent filter.
                Any other filters that you set are defined as dependent filters because they process only the data that passes
                through the context filter. Default: False.
            exclude (Union[Unset, bool]):  Default: False.
     """

    field: Union['FilterByCalculation', 'FilterByCaption', 'FilterByCaptionFunction']
    filter_type: FilterFilterType
    values: list[Any]
    context: Union[Unset, bool] = False
    exclude: Union[Unset, bool] = False
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

        values = self.values



        context = self.context

        exclude = self.exclude


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "filterType": filter_type,
            "values": values,
        })
        if context is not UNSET:
            field_dict["context"] = context
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

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




        values = cast(list[Any], d.pop("values"))


        context = d.pop("context", UNSET)

        exclude = d.pop("exclude", UNSET)

        set_filter = cls(
            field=field,
            filter_type=filter_type,
            values=values,
            context=context,
            exclude=exclude,
        )


        set_filter.additional_properties = d
        return set_filter

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
