from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_type_enum import UserTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.institution_list import InstitutionList


T = TypeVar("T", bound="UserList")


@_attrs_define
class UserList:
    """
    Attributes:
        id (int):
        url (str):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        first_name (str):
        last_name (str):
        institution (InstitutionList):
        service_user (Optional[bool]):
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        email (Union[Unset, str]):
        user_type (Union[Unset, UserTypeEnum]): * `STANDARD` - Standard
            * `SERVICE` - Service User
            * `TRAINING` - Training Account
            * `SHARED` - Shared User
    """

    id: int
    url: str
    username: str
    first_name: str
    last_name: str
    institution: "InstitutionList"
    service_user: Optional[bool]
    is_active: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    user_type: Union[Unset, UserTypeEnum] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        user_type: Union[Unset, str] = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = self.user_type.value

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
                "service_user": service_user,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if email is not UNSET:
            field_dict["email"] = email
        if user_type is not UNSET:
            field_dict["user_type"] = user_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.institution_list import InstitutionList

        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        username = d.pop("username")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        institution = InstitutionList.from_dict(d.pop("institution"))

        service_user = d.pop("service_user")

        is_active = d.pop("is_active", UNSET)

        email = d.pop("email", UNSET)

        _user_type = d.pop("user_type", UNSET)
        user_type: Union[Unset, UserTypeEnum]
        if isinstance(_user_type, Unset):
            user_type = UNSET
        else:
            user_type = UserTypeEnum(_user_type)

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
            user_type=user_type,
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
