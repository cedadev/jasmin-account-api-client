from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.category_list import CategoryList
from ..models.instution_countries_enum import InstutionCountriesEnum
from ..models.role_list import RoleList
from ..types import UNSET, Unset

T = TypeVar("T", bound="Service")


@attr.s(auto_attribs=True)
class Service:
    """Full details of a service.

    Attributes:
        id (int):
        url (str):
        name (str): The name of the service. This is also used in URLs.
        category (CategoryList): Basic information about a service category.
        roles (List[RoleList]):
        summary (str): One-line description of the service, shown in listings. No special formatting allowed.
        description (Union[Unset, None, str]): Full description of the service, shown on the details page. Markdown
            formatting is allowed.
        approver_message (Union[Unset, None, str]): Service specific instructions to be added to the external approver
            message.
        instution_countries (Union[Unset, List[InstutionCountriesEnum]]): Coutries a user's institute must be located to
            begin approval. Hold ctrl or cmd for mac to select multiple countries. Leave blank for any country.
        hidden (Union[Unset, bool]): Prevents the service appearing in listings unless the user has an active grant or
            request for it. The service details page will still be accessible to anybody who knows the URL.
        position (Union[Unset, int]): Number defining where the service appears in listings. Services are ordered in
            ascending order by category, then by this field, then alphabetically by name.
        ceda_managed (Union[Unset, bool]): Whether the service is managed by CEDA.
    """

    id: int
    url: str
    name: str
    category: CategoryList
    roles: List[RoleList]
    summary: str
    description: Union[Unset, None, str] = UNSET
    approver_message: Union[Unset, None, str] = UNSET
    instution_countries: Union[Unset, List[InstutionCountriesEnum]] = UNSET
    hidden: Union[Unset, bool] = UNSET
    position: Union[Unset, int] = UNSET
    ceda_managed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        name = self.name
        category = self.category.to_dict()

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()

            roles.append(roles_item)

        summary = self.summary
        description = self.description
        approver_message = self.approver_message
        instution_countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instution_countries, Unset):
            instution_countries = []
            for instution_countries_item_data in self.instution_countries:
                instution_countries_item = instution_countries_item_data.value

                instution_countries.append(instution_countries_item)

        hidden = self.hidden
        position = self.position
        ceda_managed = self.ceda_managed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
                "category": category,
                "roles": roles,
                "summary": summary,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if approver_message is not UNSET:
            field_dict["approver_message"] = approver_message
        if instution_countries is not UNSET:
            field_dict["instution_countries"] = instution_countries
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if position is not UNSET:
            field_dict["position"] = position
        if ceda_managed is not UNSET:
            field_dict["ceda_managed"] = ceda_managed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        category = CategoryList.from_dict(d.pop("category"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RoleList.from_dict(roles_item_data)

            roles.append(roles_item)

        summary = d.pop("summary")

        description = d.pop("description", UNSET)

        approver_message = d.pop("approver_message", UNSET)

        instution_countries = []
        _instution_countries = d.pop("instution_countries", UNSET)
        for instution_countries_item_data in _instution_countries or []:
            instution_countries_item = InstutionCountriesEnum(instution_countries_item_data)

            instution_countries.append(instution_countries_item)

        hidden = d.pop("hidden", UNSET)

        position = d.pop("position", UNSET)

        ceda_managed = d.pop("ceda_managed", UNSET)

        service = cls(
            id=id,
            url=url,
            name=name,
            category=category,
            roles=roles,
            summary=summary,
            description=description,
            approver_message=approver_message,
            instution_countries=instution_countries,
            hidden=hidden,
            position=position,
            ceda_managed=ceda_managed,
        )

        service.additional_properties = d
        return service

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
