from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegacyProfile")


@_attrs_define
class LegacyProfile:
    """
    Attributes:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        first_name (str):
        last_name (str):
        email (Union[Unset, str]):
    """

    username: str
    first_name: str
    last_name: str
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        email = d.pop("email", UNSET)

        legacy_profile = cls(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        legacy_profile.additional_properties = d
        return legacy_profile

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
