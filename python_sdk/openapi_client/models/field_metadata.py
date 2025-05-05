from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_metadata_data_type import FieldMetadataDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldMetadata")


@_attrs_define
class FieldMetadata:
    """Describes a field in the data source that can be used to create queries.

    Attributes:
        field_name (Union[Unset, str]):
        field_caption (Union[Unset, str]):
        data_type (Union[Unset, FieldMetadataDataType]):
        logical_table_id (Union[Unset, str]):
    """

    field_name: Union[Unset, str] = UNSET
    field_caption: Union[Unset, str] = UNSET
    data_type: Union[Unset, FieldMetadataDataType] = UNSET
    logical_table_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        field_caption = self.field_caption

        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        logical_table_id = self.logical_table_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if field_caption is not UNSET:
            field_dict["fieldCaption"] = field_caption
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if logical_table_id is not UNSET:
            field_dict["logicalTableId"] = logical_table_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("fieldName", UNSET)

        field_caption = d.pop("fieldCaption", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, FieldMetadataDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = FieldMetadataDataType(_data_type)

        logical_table_id = d.pop("logicalTableId", UNSET)

        field_metadata = cls(
            field_name=field_name,
            field_caption=field_caption,
            data_type=data_type,
            logical_table_id=logical_table_id,
        )

        field_metadata.additional_properties = d
        return field_metadata

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
