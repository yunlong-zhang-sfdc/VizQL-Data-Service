from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.return_format import ReturnFormat
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="QueryDatasourceOptions")



@_attrs_define
class QueryDatasourceOptions:
    """ 
        Attributes:
            return_format (Union[Unset, ReturnFormat]):
            debug (Union[Unset, bool]):  Default: False.
            disaggregate (Union[Unset, bool]):  Default: False.
     """

    return_format: Union[Unset, ReturnFormat] = UNSET
    debug: Union[Unset, bool] = False
    disaggregate: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        return_format: Union[Unset, str] = UNSET
        if not isinstance(self.return_format, Unset):
            return_format = self.return_format.value


        debug = self.debug

        disaggregate = self.disaggregate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if return_format is not UNSET:
            field_dict["returnFormat"] = return_format
        if debug is not UNSET:
            field_dict["debug"] = debug
        if disaggregate is not UNSET:
            field_dict["disaggregate"] = disaggregate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _return_format = d.pop("returnFormat", UNSET)
        return_format: Union[Unset, ReturnFormat]
        if isinstance(_return_format,  Unset):
            return_format = UNSET
        else:
            return_format = ReturnFormat(_return_format)




        debug = d.pop("debug", UNSET)

        disaggregate = d.pop("disaggregate", UNSET)

        query_datasource_options = cls(
            return_format=return_format,
            debug=debug,
            disaggregate=disaggregate,
        )


        query_datasource_options.additional_properties = d
        return query_datasource_options

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
