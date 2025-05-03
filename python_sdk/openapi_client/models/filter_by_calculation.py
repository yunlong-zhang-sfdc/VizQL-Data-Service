from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FilterByCalculation")



@_attrs_define
class FilterByCalculation:
    """ 
        Attributes:
            calculation (str): A Tableau calculation that will be used to filter on.
     """

    calculation: str


    def to_dict(self) -> dict[str, Any]:
        calculation = self.calculation


        field_dict: dict[str, Any] = {}
        field_dict.update({
            "calculation": calculation,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calculation = d.pop("calculation")

        filter_by_calculation = cls(
            calculation=calculation,
        )

        return filter_by_calculation

