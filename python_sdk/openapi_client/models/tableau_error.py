import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tableau_error_debug import TableauErrorDebug


T = TypeVar("T", bound="TableauError")


@_attrs_define
class TableauError:
    """
    Attributes:
        error_code (Union[Unset, str]):
        message (Union[Unset, str]):
        datetime_ (Union[Unset, datetime.datetime]):
        debug (Union[Unset, TableauErrorDebug]):
        tab_error_code (Union[Unset, str]):
    """

    error_code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    datetime_: Union[Unset, datetime.datetime] = UNSET
    debug: Union[Unset, "TableauErrorDebug"] = UNSET
    tab_error_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        message = self.message

        datetime_: Union[Unset, str] = UNSET
        if not isinstance(self.datetime_, Unset):
            datetime_ = self.datetime_.isoformat()

        debug: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        tab_error_code = self.tab_error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if message is not UNSET:
            field_dict["message"] = message
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_
        if debug is not UNSET:
            field_dict["debug"] = debug
        if tab_error_code is not UNSET:
            field_dict["tab-error-code"] = tab_error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tableau_error_debug import TableauErrorDebug

        d = dict(src_dict)
        error_code = d.pop("errorCode", UNSET)

        message = d.pop("message", UNSET)

        _datetime_ = d.pop("datetime", UNSET)
        datetime_: Union[Unset, datetime.datetime]
        if isinstance(_datetime_, Unset):
            datetime_ = UNSET
        else:
            datetime_ = isoparse(_datetime_)

        _debug = d.pop("debug", UNSET)
        debug: Union[Unset, TableauErrorDebug]
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = TableauErrorDebug.from_dict(_debug)

        tab_error_code = d.pop("tab-error-code", UNSET)

        tableau_error = cls(
            error_code=error_code,
            message=message,
            datetime_=datetime_,
            debug=debug,
            tab_error_code=tab_error_code,
        )

        tableau_error.additional_properties = d
        return tableau_error

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
