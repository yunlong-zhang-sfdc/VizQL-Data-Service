from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sort_direction import SortDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldWithCalculation")


@_attrs_define
class FieldWithCalculation:
    """
    Attributes:
        field_caption (str): Either the name of a specific Field in the data source, or, in the case of a calculation, a
            user-supplied name for the calculation.
        calculation (str): A Tableau calculation that will be returned as a Field in the query.
        field_alias (Union[Unset, str]): An alternative name to give the field. Will only be used in object format
            output.
        max_decimal_places (Union[Unset, int]): The maximum number of decimal places. Any trailing 0s will be dropped.
            The maxDecimalPlaces value must be greater or equal to 0.
        sort_direction (Union[Unset, SortDirection]): The direction of the sort, either ascending or descending. If not
            supplied, the default is ascending.
        sort_priority (Union[Unset, int]): To enable sorting on a specific Field, provide a sortPriority for that field,
            and that field will be sorted. The sortPriority provides a ranking of how to sort fields when multiple fields
            are being sorted. The highest priority (lowest number) field is sorted first. If only one field is being sorted,
            then any value may be used for sortPriority. SortPriority should be an integer greater than 0.
    """

    field_caption: str
    calculation: str
    field_alias: Union[Unset, str] = UNSET
    max_decimal_places: Union[Unset, int] = UNSET
    sort_direction: Union[Unset, SortDirection] = UNSET
    sort_priority: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_caption = self.field_caption

        calculation = self.calculation

        field_alias = self.field_alias

        max_decimal_places = self.max_decimal_places

        sort_direction: Union[Unset, str] = UNSET
        if not isinstance(self.sort_direction, Unset):
            sort_direction = self.sort_direction.value

        sort_priority = self.sort_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldCaption": field_caption,
                "calculation": calculation,
            }
        )
        if field_alias is not UNSET:
            field_dict["fieldAlias"] = field_alias
        if max_decimal_places is not UNSET:
            field_dict["maxDecimalPlaces"] = max_decimal_places
        if sort_direction is not UNSET:
            field_dict["sortDirection"] = sort_direction
        if sort_priority is not UNSET:
            field_dict["sortPriority"] = sort_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_caption = d.pop("fieldCaption")

        calculation = d.pop("calculation")

        field_alias = d.pop("fieldAlias", UNSET)

        max_decimal_places = d.pop("maxDecimalPlaces", UNSET)

        _sort_direction = d.pop("sortDirection", UNSET)
        sort_direction: Union[Unset, SortDirection]
        if isinstance(_sort_direction, Unset):
            sort_direction = UNSET
        else:
            sort_direction = SortDirection(_sort_direction)

        sort_priority = d.pop("sortPriority", UNSET)

        field_with_calculation = cls(
            field_caption=field_caption,
            calculation=calculation,
            field_alias=field_alias,
            max_decimal_places=max_decimal_places,
            sort_direction=sort_direction,
            sort_priority=sort_priority,
        )

        field_with_calculation.additional_properties = d
        return field_with_calculation

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
