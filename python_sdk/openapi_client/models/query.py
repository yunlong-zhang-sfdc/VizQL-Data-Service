from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_with_calculation import FieldWithCalculation
    from ..models.field_with_caption import FieldWithCaption
    from ..models.field_with_caption_function import FieldWithCaptionFunction
    from ..models.filter_ import Filter


T = TypeVar("T", bound="Query")


@_attrs_define
class Query:
    """The query is the fundamental interface to the VizQL Data Service. It holds the specific semantics to perform against
    the data source. A query consists of an array of fields to query against, and an optional array of filters to apply
    to the query.

        Attributes:
            fields (list[Union['FieldWithCalculation', 'FieldWithCaption', 'FieldWithCaptionFunction']]): An array of fields
                that define the query.
            filters (Union[Unset, list['Filter']]): An optional array of filters to apply to the query.
    """

    fields: list[Union["FieldWithCalculation", "FieldWithCaption", "FieldWithCaptionFunction"]]
    filters: Union[Unset, list["Filter"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.field_with_caption import FieldWithCaption
        from ..models.field_with_caption_function import FieldWithCaptionFunction

        fields = []
        for fields_item_data in self.fields:
            fields_item: dict[str, Any]
            if isinstance(fields_item_data, FieldWithCaption):
                fields_item = fields_item_data.to_dict()
            elif isinstance(fields_item_data, FieldWithCaptionFunction):
                fields_item = fields_item_data.to_dict()
            else:
                fields_item = fields_item_data.to_dict()

            fields.append(fields_item)

        filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "fields": fields,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_with_calculation import FieldWithCalculation
        from ..models.field_with_caption import FieldWithCaption
        from ..models.field_with_caption_function import FieldWithCaptionFunction
        from ..models.filter_ import Filter

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:

            def _parse_fields_item(
                data: object,
            ) -> Union["FieldWithCalculation", "FieldWithCaption", "FieldWithCaptionFunction"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_field_type_0 = FieldWithCaption.from_dict(data)

                    return componentsschemas_field_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_field_type_1 = FieldWithCaptionFunction.from_dict(data)

                    return componentsschemas_field_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_field_type_2 = FieldWithCalculation.from_dict(data)

                return componentsschemas_field_type_2

            fields_item = _parse_fields_item(fields_item_data)

            fields.append(fields_item)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = Filter.from_dict(filters_item_data)

            filters.append(filters_item)

        query = cls(
            fields=fields,
            filters=filters,
        )

        return query
