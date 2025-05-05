from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datasource import Datasource
    from ..models.query import Query
    from ..models.query_datasource_options import QueryDatasourceOptions


T = TypeVar("T", bound="QueryRequest")


@_attrs_define
class QueryRequest:
    """
    Attributes:
        datasource (Datasource):
        query (Query): The query is the fundamental interface to the VizQL Data Service. It holds the specific semantics
            to perform against the data source. A query consists of an array of fields to query against, and an optional
            array of filters to apply to the query.
        options (Union[Unset, QueryDatasourceOptions]):
    """

    datasource: "Datasource"
    query: "Query"
    options: Union[Unset, "QueryDatasourceOptions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource = self.datasource.to_dict()

        query = self.query.to_dict()

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasource": datasource,
                "query": query,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datasource import Datasource
        from ..models.query import Query
        from ..models.query_datasource_options import QueryDatasourceOptions

        d = dict(src_dict)
        datasource = Datasource.from_dict(d.pop("datasource"))

        query = Query.from_dict(d.pop("query"))

        _options = d.pop("options", UNSET)
        options: Union[Unset, QueryDatasourceOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = QueryDatasourceOptions.from_dict(_options)

        query_request = cls(
            datasource=datasource,
            query=query,
            options=options,
        )

        query_request.additional_properties = d
        return query_request

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
