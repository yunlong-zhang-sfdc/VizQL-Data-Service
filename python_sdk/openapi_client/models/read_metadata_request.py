from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.query_options import QueryOptions
  from ..models.datasource import Datasource





T = TypeVar("T", bound="ReadMetadataRequest")



@_attrs_define
class ReadMetadataRequest:
    """ 
        Attributes:
            datasource (Datasource):
            options (Union[Unset, QueryOptions]): Some optional metadata that can be used to adjust the behavior of an
                endpoint.
     """

    datasource: 'Datasource'
    options: Union[Unset, 'QueryOptions'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.query_options import QueryOptions
        from ..models.datasource import Datasource
        datasource = self.datasource.to_dict()

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "datasource": datasource,
        })
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_options import QueryOptions
        from ..models.datasource import Datasource
        d = dict(src_dict)
        datasource = Datasource.from_dict(d.pop("datasource"))




        _options = d.pop("options", UNSET)
        options: Union[Unset, QueryOptions]
        if isinstance(_options,  Unset):
            options = UNSET
        else:
            options = QueryOptions.from_dict(_options)




        read_metadata_request = cls(
            datasource=datasource,
            options=options,
        )


        read_metadata_request.additional_properties = d
        return read_metadata_request

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
