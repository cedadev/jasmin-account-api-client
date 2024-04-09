from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        tags (List[Any]):
        username (Union[Unset, str]):
        surname (Union[Unset, str]):
        full_name (Union[Unset, str]):
        uid_number (Union[Unset, int]): Leave blank for default (next available uidNumber)
        uid (Union[Unset, str]): This is always overridden to match username
        home_directory (Union[Unset, str]): Leave blank for default (/home/users/{user})
        gid_number (Union[Unset, int]):
        login_shell (Union[Unset, str]):
    """

    tags: List[Any]
    username: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    uid_number: Union[Unset, int] = UNSET
    uid: Union[Unset, str] = UNSET
    home_directory: Union[Unset, str] = UNSET
    gid_number: Union[Unset, int] = UNSET
    login_shell: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tags = self.tags

        username = self.username

        surname = self.surname

        full_name = self.full_name

        uid_number = self.uid_number

        uid = self.uid

        home_directory = self.home_directory

        gid_number = self.gid_number

        login_shell = self.login_shell

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if surname is not UNSET:
            field_dict["surname"] = surname
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if uid_number is not UNSET:
            field_dict["uidNumber"] = uid_number
        if uid is not UNSET:
            field_dict["uid"] = uid
        if home_directory is not UNSET:
            field_dict["homeDirectory"] = home_directory
        if gid_number is not UNSET:
            field_dict["gidNumber"] = gid_number
        if login_shell is not UNSET:
            field_dict["loginShell"] = login_shell

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tags = cast(List[Any], d.pop("tags"))

        username = d.pop("username", UNSET)

        surname = d.pop("surname", UNSET)

        full_name = d.pop("full_name", UNSET)

        uid_number = d.pop("uidNumber", UNSET)

        uid = d.pop("uid", UNSET)

        home_directory = d.pop("homeDirectory", UNSET)

        gid_number = d.pop("gidNumber", UNSET)

        login_shell = d.pop("loginShell", UNSET)

        account = cls(
            tags=tags,
            username=username,
            surname=surname,
            full_name=full_name,
            uid_number=uid_number,
            uid=uid,
            home_directory=home_directory,
            gid_number=gid_number,
            login_shell=login_shell,
        )

        account.additional_properties = d
        return account

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
