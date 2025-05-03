from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.connection import Connection





T = TypeVar("T", bound="Datasource")



@_attrs_define
class Datasource:
    """ 
        Attributes:
            datasource_luid (str): The LUID of the data source to be queried.
            connections (Union[Unset, list['Connection']]):
     """

    datasource_luid: str
    connections: Union[Unset, list['Connection']] = UNSET


    def to_dict(self) -> dict[str, Any]:
        from ..models.connection import Connection
        datasource_luid = self.datasource_luid

        connections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)




        field_dict: dict[str, Any] = {}
        field_dict.update({
            "datasourceLuid": datasource_luid,
        })
        if connections is not UNSET:
            field_dict["connections"] = connections

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection import Connection
        d = dict(src_dict)
        datasource_luid = d.pop("datasourceLuid")

        connections = []
        _connections = d.pop("connections", UNSET)
        for connections_item_data in (_connections or []):
            connections_item = Connection.from_dict(connections_item_data)



            connections.append(connections_item)


        datasource = cls(
            datasource_luid=datasource_luid,
            connections=connections,
        )

        return datasource

