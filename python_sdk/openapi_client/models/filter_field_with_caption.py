from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FilterFieldWithCaption")


@_attrs_define
class FilterFieldWithCaption:
    """
    Attributes:
        field_caption (str): The caption of the field to filter on.
    """

    field_caption: str

    def to_dict(self) -> dict[str, Any]:
        field_caption = self.field_caption

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "fieldCaption": field_caption,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_caption = d.pop("fieldCaption")

        filter_field_with_caption = cls(
            field_caption=field_caption,
        )

        return filter_field_with_caption
