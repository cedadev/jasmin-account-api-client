import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.lifecycle_state_enum import LifecycleStateEnum
from ..models.user_type_enum import UserTypeEnum

if TYPE_CHECKING:
    from ..models.related_institution import RelatedInstitution


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
        institution (Union['RelatedInstitution', None]):
        service_user (Union[None, bool]): Service user is True if user type is SERVICE.
        is_active (bool): Designates whether this user should be treated as active. Unselect this instead of deleting
            accounts.
        email (str):
        user_type (UserTypeEnum): * `STANDARD` - Standard
            * `SERVICE` - Service User
            * `TRAINING` - Training Account
            * `SHARED` - Shared User
        lifecycle_state (LifecycleStateEnum): * `NORMAL` - Normal
            * `AWAITING_CLEANUP` - Awaiting Cleanup
            * `DORMANT` - Dormant
            * `ACCNT_DEL_NOTIFIED` - Impending Account Deletion Notified
            * `ACCNT_DEL_HOME_MOVED` - Home Directory Hidden
            * `ACCNT_DEL_HOME_REMOVED` - Home Directory Deleted
        deactivated_at (Union[None, datetime.datetime]): Date on which this account was deactivated.
    """

    id: int
    url: str
    username: str
    first_name: str
    last_name: str
    institution: Union["RelatedInstitution", None]
    service_user: Union[None, bool]
    is_active: bool
    email: str
    user_type: UserTypeEnum
    lifecycle_state: LifecycleStateEnum
    deactivated_at: Union[None, datetime.datetime]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.related_institution import RelatedInstitution

        id = self.id

        url = self.url

        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        institution: Union[Dict[str, Any], None]
        if isinstance(self.institution, RelatedInstitution):
            institution = self.institution.to_dict()
        else:
            institution = self.institution

        service_user: Union[None, bool]
        service_user = self.service_user

        is_active = self.is_active

        email = self.email

        user_type = self.user_type.value

        lifecycle_state = self.lifecycle_state.value

        deactivated_at: Union[None, str]
        if isinstance(self.deactivated_at, datetime.datetime):
            deactivated_at = self.deactivated_at.isoformat()
        else:
            deactivated_at = self.deactivated_at

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
                "is_active": is_active,
                "email": email,
                "user_type": user_type,
                "lifecycle_state": lifecycle_state,
                "deactivated_at": deactivated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.related_institution import RelatedInstitution

        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        username = d.pop("username")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        def _parse_institution(data: object) -> Union["RelatedInstitution", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                institution_type_1 = RelatedInstitution.from_dict(data)

                return institution_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RelatedInstitution", None], data)

        institution = _parse_institution(d.pop("institution"))

        def _parse_service_user(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        service_user = _parse_service_user(d.pop("service_user"))

        is_active = d.pop("is_active")

        email = d.pop("email")

        user_type = UserTypeEnum(d.pop("user_type"))

        lifecycle_state = LifecycleStateEnum(d.pop("lifecycle_state"))

        def _parse_deactivated_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deactivated_at_type_0 = isoparse(data)

                return deactivated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        deactivated_at = _parse_deactivated_at(d.pop("deactivated_at"))

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
            lifecycle_state=lifecycle_state,
            deactivated_at=deactivated_at,
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
