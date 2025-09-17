import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.degree_enum import DegreeEnum
from ..models.discipline_enum import DisciplineEnum
from ..models.lifecycle_state_enum import LifecycleStateEnum
from ..models.user_type_enum import UserTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.institution_list import InstitutionList
    from ..models.user_list import UserList


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (int):
        account (Account):
        last_login (Union[None, datetime.datetime]):
        is_superuser (bool): Designates that this user has all permissions without explicitly assigning them.
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        email (str):
        is_staff (bool): Designates whether the user can log into this admin site.
        is_active (bool): Designates whether this user should be treated as active. Unselect this instead of deleting
            accounts.
        date_joined (datetime.datetime):
        first_name (str):
        last_name (str):
        discipline (DisciplineEnum): * `Atmospheric Physics` - Atmospheric Physics
            * `Atmospheric Chemistry` - Atmospheric Chemistry
            * `Climate Change` - Climate Change
            * `Earth System Science` - Earth System Science
            * `Marine Science` - Marine Science
            * `Terrestrial and Fresh Water` - Terrestrial and Fresh Water
            * `Earth Observation` - Earth Observation
            * `Polar Science` - Polar Science
            * `Geography` - Geography
            * `Engineering` - Engineering
            * `Medical/Biological Sciences` - Medical/Biological Sciences
            * `Mathematics/Computer Science` - Mathematics/Computer Science
            * `Economics` - Economics
            * `Other` - Other
        degree (Union[BlankEnum, DegreeEnum]): The type of degree you are studying for, if applicable

            * `` - Not studying for a degree
            * `First degree` - First Degree (Bachelor's / Undergraduate Master's)
            * `Postgraduate Master's` - Postgraduate Master's
            * `Doctorate` - Doctorate
            * `Other` - Other
        internal_comment (str): Internal notes about the user that will not be displayed to the user
        service_user (Union[None, bool]): Service user is True if user type is SERVICE.
        email_confirmed_at (Union[None, datetime.datetime]):
        conditions_accepted_at (Union[None, datetime.datetime]):
        approved_for_root_at (Union[None, datetime.datetime]):
        user_reason (str): Indicate why the user has been suspended
        internal_reason (str): Any internal details about the user's suspension that should not be displayed to the user
        institution (Union['InstitutionList', None]):
        otp_required (Union[None, bool]): OTP is now always required.
        event (Union[None, str]):
        responsible_users (List['UserList']):
        user_type (UserTypeEnum): * `STANDARD` - Standard
            * `SERVICE` - Service User
            * `TRAINING` - Training Account
            * `SHARED` - Shared User
        deactivated_at (Union[None, datetime.datetime]): Date on which this account was deactivated.
        lifecycle_state (Union[Unset, LifecycleStateEnum]): * `NORMAL` - Normal
            * `AWAITING_CLEANUP` - Awaiting Cleanup
            * `DORMANT` - Dormant
    """

    id: int
    account: "Account"
    last_login: Union[None, datetime.datetime]
    is_superuser: bool
    username: str
    email: str
    is_staff: bool
    is_active: bool
    date_joined: datetime.datetime
    first_name: str
    last_name: str
    discipline: DisciplineEnum
    degree: Union[BlankEnum, DegreeEnum]
    internal_comment: str
    service_user: Union[None, bool]
    email_confirmed_at: Union[None, datetime.datetime]
    conditions_accepted_at: Union[None, datetime.datetime]
    approved_for_root_at: Union[None, datetime.datetime]
    user_reason: str
    internal_reason: str
    institution: Union["InstitutionList", None]
    otp_required: Union[None, bool]
    event: Union[None, str]
    responsible_users: List["UserList"]
    user_type: UserTypeEnum
    deactivated_at: Union[None, datetime.datetime]
    lifecycle_state: Union[Unset, LifecycleStateEnum] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.institution_list import InstitutionList

        id = self.id

        account = self.account.to_dict()

        last_login: Union[None, str]
        if isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        is_superuser = self.is_superuser

        username = self.username

        email = self.email

        is_staff = self.is_staff

        is_active = self.is_active

        date_joined = self.date_joined.isoformat()

        first_name = self.first_name

        last_name = self.last_name

        discipline = self.discipline.value

        degree: str
        if isinstance(self.degree, DegreeEnum):
            degree = self.degree.value
        else:
            degree = self.degree.value

        internal_comment = self.internal_comment

        service_user: Union[None, bool]
        service_user = self.service_user

        email_confirmed_at: Union[None, str]
        if isinstance(self.email_confirmed_at, datetime.datetime):
            email_confirmed_at = self.email_confirmed_at.isoformat()
        else:
            email_confirmed_at = self.email_confirmed_at

        conditions_accepted_at: Union[None, str]
        if isinstance(self.conditions_accepted_at, datetime.datetime):
            conditions_accepted_at = self.conditions_accepted_at.isoformat()
        else:
            conditions_accepted_at = self.conditions_accepted_at

        approved_for_root_at: Union[None, str]
        if isinstance(self.approved_for_root_at, datetime.datetime):
            approved_for_root_at = self.approved_for_root_at.isoformat()
        else:
            approved_for_root_at = self.approved_for_root_at

        user_reason = self.user_reason

        internal_reason = self.internal_reason

        institution: Union[Dict[str, Any], None]
        if isinstance(self.institution, InstitutionList):
            institution = self.institution.to_dict()
        else:
            institution = self.institution

        otp_required: Union[None, bool]
        otp_required = self.otp_required

        event: Union[None, str]
        event = self.event

        responsible_users = []
        for responsible_users_item_data in self.responsible_users:
            responsible_users_item = responsible_users_item_data.to_dict()
            responsible_users.append(responsible_users_item)

        user_type = self.user_type.value

        deactivated_at: Union[None, str]
        if isinstance(self.deactivated_at, datetime.datetime):
            deactivated_at = self.deactivated_at.isoformat()
        else:
            deactivated_at = self.deactivated_at

        lifecycle_state: Union[Unset, str] = UNSET
        if not isinstance(self.lifecycle_state, Unset):
            lifecycle_state = self.lifecycle_state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "account": account,
                "last_login": last_login,
                "is_superuser": is_superuser,
                "username": username,
                "email": email,
                "is_staff": is_staff,
                "is_active": is_active,
                "date_joined": date_joined,
                "first_name": first_name,
                "last_name": last_name,
                "discipline": discipline,
                "degree": degree,
                "internal_comment": internal_comment,
                "service_user": service_user,
                "email_confirmed_at": email_confirmed_at,
                "conditions_accepted_at": conditions_accepted_at,
                "approved_for_root_at": approved_for_root_at,
                "user_reason": user_reason,
                "internal_reason": internal_reason,
                "institution": institution,
                "otp_required": otp_required,
                "event": event,
                "responsible_users": responsible_users,
                "user_type": user_type,
                "deactivated_at": deactivated_at,
            }
        )
        if lifecycle_state is not UNSET:
            field_dict["lifecycle_state"] = lifecycle_state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account
        from ..models.institution_list import InstitutionList
        from ..models.user_list import UserList

        d = src_dict.copy()
        id = d.pop("id")

        account = Account.from_dict(d.pop("account"))

        def _parse_last_login(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = isoparse(data)

                return last_login_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_login = _parse_last_login(d.pop("last_login"))

        is_superuser = d.pop("is_superuser")

        username = d.pop("username")

        email = d.pop("email")

        is_staff = d.pop("is_staff")

        is_active = d.pop("is_active")

        date_joined = isoparse(d.pop("date_joined"))

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        discipline = DisciplineEnum(d.pop("discipline"))

        def _parse_degree(data: object) -> Union[BlankEnum, DegreeEnum]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                degree_type_0 = DegreeEnum(data)

                return degree_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            degree_type_1 = BlankEnum(data)

            return degree_type_1

        degree = _parse_degree(d.pop("degree"))

        internal_comment = d.pop("internal_comment")

        def _parse_service_user(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        service_user = _parse_service_user(d.pop("service_user"))

        def _parse_email_confirmed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                email_confirmed_at_type_0 = isoparse(data)

                return email_confirmed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        email_confirmed_at = _parse_email_confirmed_at(d.pop("email_confirmed_at"))

        def _parse_conditions_accepted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conditions_accepted_at_type_0 = isoparse(data)

                return conditions_accepted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        conditions_accepted_at = _parse_conditions_accepted_at(d.pop("conditions_accepted_at"))

        def _parse_approved_for_root_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_for_root_at_type_0 = isoparse(data)

                return approved_for_root_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        approved_for_root_at = _parse_approved_for_root_at(d.pop("approved_for_root_at"))

        user_reason = d.pop("user_reason")

        internal_reason = d.pop("internal_reason")

        def _parse_institution(data: object) -> Union["InstitutionList", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                institution_type_1 = InstitutionList.from_dict(data)

                return institution_type_1
            except:  # noqa: E722
                pass
            return cast(Union["InstitutionList", None], data)

        institution = _parse_institution(d.pop("institution"))

        def _parse_otp_required(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        otp_required = _parse_otp_required(d.pop("otp_required"))

        def _parse_event(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        event = _parse_event(d.pop("event"))

        responsible_users = []
        _responsible_users = d.pop("responsible_users")
        for responsible_users_item_data in _responsible_users:
            responsible_users_item = UserList.from_dict(responsible_users_item_data)

            responsible_users.append(responsible_users_item)

        user_type = UserTypeEnum(d.pop("user_type"))

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

        _lifecycle_state = d.pop("lifecycle_state", UNSET)
        lifecycle_state: Union[Unset, LifecycleStateEnum]
        if isinstance(_lifecycle_state, Unset):
            lifecycle_state = UNSET
        else:
            lifecycle_state = LifecycleStateEnum(_lifecycle_state)

        user = cls(
            id=id,
            account=account,
            last_login=last_login,
            is_superuser=is_superuser,
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            date_joined=date_joined,
            first_name=first_name,
            last_name=last_name,
            discipline=discipline,
            degree=degree,
            internal_comment=internal_comment,
            service_user=service_user,
            email_confirmed_at=email_confirmed_at,
            conditions_accepted_at=conditions_accepted_at,
            approved_for_root_at=approved_for_root_at,
            user_reason=user_reason,
            internal_reason=internal_reason,
            institution=institution,
            otp_required=otp_required,
            event=event,
            responsible_users=responsible_users,
            user_type=user_type,
            deactivated_at=deactivated_at,
            lifecycle_state=lifecycle_state,
        )

        user.additional_properties = d
        return user

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
