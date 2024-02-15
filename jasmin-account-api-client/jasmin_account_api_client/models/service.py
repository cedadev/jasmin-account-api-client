from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.institution_countries_enum import InstitutionCountriesEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_list import CategoryList
    from ..models.role_list import RoleList


T = TypeVar("T", bound="Service")


@_attrs_define
class Service:
    """Full details of a service.

    Attributes:
        id (int):
        url (str):
        name (str): The name of the service. This is also used in URLs.
        category (CategoryList): Basic information about a service category.
        roles (List['RoleList']):
        summary (str): One-line description of the service, shown in listings. No special formatting allowed.
        institution_countries (List[Union[BlankEnum, InstitutionCountriesEnum]]):
        description (Union[Unset, None, str]): Full description of the service, shown on the details page. Markdown
            formatting is allowed.
        approver_message (Union[Unset, None, str]): Service specific instructions to be added to the external approver
            message.
        hidden (Union[Unset, bool]): Prevents the service appearing in listings unless the user has an active grant or
            request for it. The service details page will still be accessible to anybody who knows the URL.
        position (Union[Unset, int]): Number defining where the service appears in listings. Services are ordered in
            ascending order by category, then by this field, then alphabetically by name.
        ceda_managed (Union[Unset, bool]): Whether the service is managed by CEDA.
    """

    id: int
    url: str
    name: str
    category: "CategoryList"
    roles: List["RoleList"]
    summary: str
    institution_countries: List[Union[BlankEnum, InstitutionCountriesEnum]]
    description: Union[Unset, None, str] = UNSET
    approver_message: Union[Unset, None, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    position: Union[Unset, int] = UNSET
    ceda_managed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        institution_countries = []
        for institution_countries_item_data in self.institution_countries:
            institution_countries_item: str

            if isinstance(institution_countries_item_data, InstitutionCountriesEnum):
                institution_countries_item = institution_countries_item_data.value

            else:
                institution_countries_item = institution_countries_item_data.value

            institution_countries.append(institution_countries_item)

        description = self.description
        approver_message = self.approver_message
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
                "institution_countries": institution_countries,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if approver_message is not UNSET:
            field_dict["approver_message"] = approver_message
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if position is not UNSET:
            field_dict["position"] = position
        if ceda_managed is not UNSET:
            field_dict["ceda_managed"] = ceda_managed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_list import CategoryList
        from ..models.role_list import RoleList

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

        institution_countries = []
        _institution_countries = d.pop("institution_countries")
        for institution_countries_item_data in _institution_countries:

            def _parse_institution_countries_item(data: object) -> Union[BlankEnum, InstitutionCountriesEnum]:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    institution_countries_item_type_0 = InstitutionCountriesEnum(data)

                    return institution_countries_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, str):
                    raise TypeError()
                institution_countries_item_type_1 = BlankEnum(data)

                return institution_countries_item_type_1

            institution_countries_item = _parse_institution_countries_item(institution_countries_item_data)

            institution_countries.append(institution_countries_item)

        description = d.pop("description", UNSET)

        approver_message = d.pop("approver_message", UNSET)

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
            institution_countries=institution_countries,
            description=description,
            approver_message=approver_message,
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
