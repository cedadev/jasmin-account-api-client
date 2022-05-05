from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.category_service import CategoryService
from ..types import UNSET, Unset

T = TypeVar("T", bound="Category")


@attr.s(auto_attribs=True)
class Category:
    """Details of a service category.

    Attributes:
        id (int):
        url (str):
        name (str): Short name for the category, used in URLs
        long_name (str): Long name for the category, used for display
        services (List[CategoryService]):
        position (Union[Unset, int]): Number defining where the category appears in listings. Categories are ordered in
            ascending order by this field, then alphabetically by name within that.
    """

    id: int
    url: str
    name: str
    long_name: str
    services: List[CategoryService]
    position: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        name = self.name
        long_name = self.long_name
        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()

            services.append(services_item)

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
                "long_name": long_name,
                "services": services,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        long_name = d.pop("long_name")

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = CategoryService.from_dict(services_item_data)

            services.append(services_item)

        position = d.pop("position", UNSET)

        category = cls(
            id=id,
            url=url,
            name=name,
            long_name=long_name,
            services=services,
            position=position,
        )

        category.additional_properties = d
        return category

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
