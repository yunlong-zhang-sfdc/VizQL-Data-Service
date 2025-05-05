from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_filter_type import FilterFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field_with_calculation import FilterFieldWithCalculation
    from ..models.filter_field_with_caption import FilterFieldWithCaption
    from ..models.filter_field_with_caption_function import FilterFieldWithCaptionFunction


T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """A filter to be used in the query to filter on the data source.

    Attributes:
        field (Union['FilterFieldWithCalculation', 'FilterFieldWithCaption', 'FilterFieldWithCaptionFunction']):
        filter_type (FilterFilterType):
        context (Union[Unset, bool]): Make the given filter a context filter, meaning that it's an independent filter.
            Any other filters that you set are defined as dependent filters because they process only the data that passes
            through the context filter. Default: False.
    """

    field: Union["FilterFieldWithCalculation", "FilterFieldWithCaption", "FilterFieldWithCaptionFunction"]
    filter_type: FilterFilterType
    context: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_field_with_caption import FilterFieldWithCaption
        from ..models.filter_field_with_caption_function import FilterFieldWithCaptionFunction

        field: dict[str, Any]
        if isinstance(self.field, FilterFieldWithCaption):
            field = self.field.to_dict()
        elif isinstance(self.field, FilterFieldWithCaptionFunction):
            field = self.field.to_dict()
        else:
            field = self.field.to_dict()

        filter_type = self.filter_type.value

        context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "filterType": filter_type,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_field_with_calculation import FilterFieldWithCalculation
        from ..models.filter_field_with_caption import FilterFieldWithCaption
        from ..models.filter_field_with_caption_function import FilterFieldWithCaptionFunction

        d = dict(src_dict)

        def _parse_field(
            data: object,
        ) -> Union["FilterFieldWithCalculation", "FilterFieldWithCaption", "FilterFieldWithCaptionFunction"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_field_type_0 = FilterFieldWithCaption.from_dict(data)

                return componentsschemas_filter_field_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_field_type_1 = FilterFieldWithCaptionFunction.from_dict(data)

                return componentsschemas_filter_field_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_field_type_2 = FilterFieldWithCalculation.from_dict(data)

            return componentsschemas_filter_field_type_2

        field = _parse_field(d.pop("field"))

        filter_type = FilterFilterType(d.pop("filterType"))

        context = d.pop("context", UNSET)

        filter_ = cls(
            field=field,
            filter_type=filter_type,
            context=context,
        )

        filter_.additional_properties = d
        return filter_

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
