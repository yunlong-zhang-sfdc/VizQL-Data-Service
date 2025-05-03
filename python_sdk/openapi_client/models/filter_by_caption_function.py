from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.function import Function






T = TypeVar("T", bound="FilterByCaptionFunction")



@_attrs_define
class FilterByCaptionFunction:
    """ 
        Attributes:
            field_caption (str): The caption of the field to filter on.
            function (Function): The standard set of Tableau aggregations which can be applied to a field.
     """

    field_caption: str
    function: Function


    def to_dict(self) -> dict[str, Any]:
        field_caption = self.field_caption

        function = self.function.value


        field_dict: dict[str, Any] = {}
        field_dict.update({
            "fieldCaption": field_caption,
            "function": function,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_caption = d.pop("fieldCaption")

        function = Function(d.pop("function"))




        filter_by_caption_function = cls(
            field_caption=field_caption,
            function=function,
        )

        return filter_by_caption_function

