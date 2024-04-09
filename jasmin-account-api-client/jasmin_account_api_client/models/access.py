from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_user import ServiceUser


T = TypeVar("T", bound="Access")


@_attrs_define
class Access:
    """List of service accesses.

    Attributes:
        id (int):
        user (ServiceUser): Basic UserSerializer to provide a link to the full one.
    """

    id: int
    user: "ServiceUser"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_user import ServiceUser

        d = src_dict.copy()
        id = d.pop("id")

        user = ServiceUser.from_dict(d.pop("user"))

        access = cls(
            id=id,
            user=user,
        )

        access.additional_properties = d
        return access

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
