from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoryService")


@_attrs_define
class CategoryService:
    """Simple details about a service, excluding it's category.

    Attributes:
        id (int):
        url (str):
        name (str): The name of the service. This is also used in URLs.
        summary (str): One-line description of the service, shown in listings. No special formatting allowed.
        hidden (Union[Unset, bool]): Prevents the service appearing in listings unless the user has an active grant or
            request for it. The service details page will still be accessible to anybody who knows the URL.
    """

    id: int
    url: str
    name: str
    summary: str
    hidden: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        url = self.url

        name = self.name

        summary = self.summary

        hidden = self.hidden

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
                "summary": summary,
            }
        )
        if hidden is not UNSET:
            field_dict["hidden"] = hidden

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        summary = d.pop("summary")

        hidden = d.pop("hidden", UNSET)

        category_service = cls(
            id=id,
            url=url,
            name=name,
            summary=summary,
            hidden=hidden,
        )

        category_service.additional_properties = d
        return category_service

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
