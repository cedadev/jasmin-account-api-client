import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_list import RoleList
    from ..models.service_list import ServiceList
    from ..models.service_user import ServiceUser


T = TypeVar("T", bound="Grant")


@_attrs_define
class Grant:
    """Simple details about a grant.

    Attributes:
        id (int):
        service (ServiceList): Simple details about a service.
        role (RoleList): Basic list of roles.
        user (ServiceUser): Basic UserSerializer to provide a link to the full one.
        granted_at (datetime.datetime):
        expires (Union[Unset, datetime.date]):
        revoked (Union[Unset, bool]):
        revoked_at (Union[None, Unset, datetime.datetime]): Date on which this grant was revoked.
        user_reason (Union[Unset, str]): <a href="http://daringfireball.net/projects/markdown/syntax"
            target="_blank">Markdown syntax</a> allowed, but no raw HTML. Examples: **bold**, *italic*, indent 4 spaces for
            a code block.
    """

    id: int
    service: "ServiceList"
    role: "RoleList"
    user: "ServiceUser"
    granted_at: datetime.datetime
    expires: Union[Unset, datetime.date] = UNSET
    revoked: Union[Unset, bool] = UNSET
    revoked_at: Union[None, Unset, datetime.datetime] = UNSET
    user_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        service = self.service.to_dict()

        role = self.role.to_dict()

        user = self.user.to_dict()

        granted_at = self.granted_at.isoformat()

        expires: Union[Unset, str] = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        revoked = self.revoked

        revoked_at: Union[None, Unset, str]
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        user_reason = self.user_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "service": service,
                "role": role,
                "user": user,
                "granted_at": granted_at,
            }
        )
        if expires is not UNSET:
            field_dict["expires"] = expires
        if revoked is not UNSET:
            field_dict["revoked"] = revoked
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at
        if user_reason is not UNSET:
            field_dict["user_reason"] = user_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.role_list import RoleList
        from ..models.service_list import ServiceList
        from ..models.service_user import ServiceUser

        d = src_dict.copy()
        id = d.pop("id")

        service = ServiceList.from_dict(d.pop("service"))

        role = RoleList.from_dict(d.pop("role"))

        user = ServiceUser.from_dict(d.pop("user"))

        granted_at = isoparse(d.pop("granted_at"))

        _expires = d.pop("expires", UNSET)
        expires: Union[Unset, datetime.date]
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires).date()

        revoked = d.pop("revoked", UNSET)

        def _parse_revoked_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = isoparse(data)

                return revoked_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))

        user_reason = d.pop("user_reason", UNSET)

        grant = cls(
            id=id,
            service=service,
            role=role,
            user=user,
            granted_at=granted_at,
            expires=expires,
            revoked=revoked,
            revoked_at=revoked_at,
            user_reason=user_reason,
        )

        grant.additional_properties = d
        return grant

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
