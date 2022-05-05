from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.institution_list import InstitutionList
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserList")


@attr.s(auto_attribs=True)
class UserList:
    """
    Attributes:
        id (int):
        url (str):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        first_name (str):
        last_name (str):
        institution (InstitutionList):
        service_user (Union[Unset, bool]): Indicates if this user is a service user, i.e. a user that exists to run a
            service rather than a regular user account.
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        email (Union[Unset, str]):
    """

    id: int
    url: str
    username: str
    first_name: str
    last_name: str
    institution: InstitutionList
    service_user: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        institution = self.institution.to_dict()

        service_user = self.service_user
        is_active = self.is_active
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "institution": institution,
            }
        )
        if service_user is not UNSET:
            field_dict["service_user"] = service_user
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        username = d.pop("username")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        institution = InstitutionList.from_dict(d.pop("institution"))

        service_user = d.pop("service_user", UNSET)

        is_active = d.pop("is_active", UNSET)

        email = d.pop("email", UNSET)

        user_list = cls(
            id=id,
            url=url,
            username=username,
            first_name=first_name,
            last_name=last_name,
            institution=institution,
            service_user=service_user,
            is_active=is_active,
            email=email,
        )

        user_list.additional_properties = d
        return user_list

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
