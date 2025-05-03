from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Connection")



@_attrs_define
class Connection:
    """ 
        Attributes:
            connection_username (str):
            connection_password (str):
            connection_luid (Union[Unset, str]):
     """

    connection_username: str
    connection_password: str
    connection_luid: Union[Unset, str] = UNSET


    def to_dict(self) -> dict[str, Any]:
        connection_username = self.connection_username

        connection_password = self.connection_password

        connection_luid = self.connection_luid


        field_dict: dict[str, Any] = {}
        field_dict.update({
            "connectionUsername": connection_username,
            "connectionPassword": connection_password,
        })
        if connection_luid is not UNSET:
            field_dict["connectionLuid"] = connection_luid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_username = d.pop("connectionUsername")

        connection_password = d.pop("connectionPassword")

        connection_luid = d.pop("connectionLuid", UNSET)

        connection = cls(
            connection_username=connection_username,
            connection_password=connection_password,
            connection_luid=connection_luid,
        )

        return connection

