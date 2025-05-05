from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_filter_type import FilterFilterType
from ..models.top_n_filter_direction import TopNFilterDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field_with_calculation import FilterFieldWithCalculation
    from ..models.filter_field_with_caption import FilterFieldWithCaption
    from ..models.filter_field_with_caption_function import FilterFieldWithCaptionFunction


T = TypeVar("T", bound="TopNFilter")


@_attrs_define
class TopNFilter:
    """
    Attributes:
        field (Union['FilterFieldWithCalculation', 'FilterFieldWithCaption', 'FilterFieldWithCaptionFunction']):
        filter_type (FilterFilterType):
        context (Union[Unset, bool]): Make the given filter a context filter, meaning that it's an independent filter.
            Any other filters that you set are defined as dependent filters because they process only the data that passes
            through the context filter. Default: False.
        direction (Union[Unset, TopNFilterDirection]): Top (ascending) or Bottom (descending) N. Default:
            TopNFilterDirection.TOP.
        how_many (Union[Unset, int]): The number of values from the top or the bottom of the given fieldToMeasure.
        field_to_measure (Union['FilterFieldWithCalculation', 'FilterFieldWithCaption',
            'FilterFieldWithCaptionFunction', Unset]):
    """

    field: Union["FilterFieldWithCalculation", "FilterFieldWithCaption", "FilterFieldWithCaptionFunction"]
    filter_type: FilterFilterType
    context: Union[Unset, bool] = False
    direction: Union[Unset, TopNFilterDirection] = TopNFilterDirection.TOP
    how_many: Union[Unset, int] = UNSET
    field_to_measure: Union[
        "FilterFieldWithCalculation", "FilterFieldWithCaption", "FilterFieldWithCaptionFunction", Unset
    ] = UNSET
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

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        how_many = self.how_many

        field_to_measure: Union[Unset, dict[str, Any]]
        if isinstance(self.field_to_measure, Unset):
            field_to_measure = UNSET
        elif isinstance(self.field_to_measure, FilterFieldWithCaption):
            field_to_measure = self.field_to_measure.to_dict()
        elif isinstance(self.field_to_measure, FilterFieldWithCaptionFunction):
            field_to_measure = self.field_to_measure.to_dict()
        else:
            field_to_measure = self.field_to_measure.to_dict()

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
        if direction is not UNSET:
            field_dict["direction"] = direction
        if how_many is not UNSET:
            field_dict["howMany"] = how_many
        if field_to_measure is not UNSET:
            field_dict["fieldToMeasure"] = field_to_measure

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

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, TopNFilterDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = TopNFilterDirection(_direction)

        how_many = d.pop("howMany", UNSET)

        def _parse_field_to_measure(
            data: object,
        ) -> Union["FilterFieldWithCalculation", "FilterFieldWithCaption", "FilterFieldWithCaptionFunction", Unset]:
            if isinstance(data, Unset):
                return data
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

        field_to_measure = _parse_field_to_measure(d.pop("fieldToMeasure", UNSET))

        top_n_filter = cls(
            field=field,
            filter_type=filter_type,
            context=context,
            direction=direction,
            how_many=how_many,
            field_to_measure=field_to_measure,
        )

        top_n_filter.additional_properties = d
        return top_n_filter

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
