from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FilterFieldWithCalculation")


@_attrs_define
class FilterFieldWithCalculation:
    """
    Attributes:
        calculation (str): A Tableau calculation that will be used to filter on.
    """

    calculation: str

    def to_dict(self) -> dict[str, Any]:
        calculation = self.calculation

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "calculation": calculation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calculation = d.pop("calculation")

        filter_field_with_calculation = cls(
            calculation=calculation,
        )

        return filter_field_with_calculation
