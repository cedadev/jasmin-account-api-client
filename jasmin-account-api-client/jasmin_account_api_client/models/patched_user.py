import datetime
import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

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


T = TypeVar("T", bound="PatchedUser")


@_attrs_define
class PatchedUser:
    """
    Attributes:
        id (Union[Unset, int]):
        account (Union[Unset, Account]):
        last_login (Union[None, Unset, datetime.datetime]):
        is_superuser (Union[Unset, bool]): Designates that this user has all permissions without explicitly assigning
            them.
        username (Union[Unset, str]): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        email (Union[Unset, str]):
        is_staff (Union[Unset, bool]): Designates whether the user can log into this admin site.
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        date_joined (Union[Unset, datetime.datetime]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        discipline (Union[Unset, DisciplineEnum]): * `Atmospheric Physics` - Atmospheric Physics
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
        degree (Union[BlankEnum, DegreeEnum, Unset]): The type of degree you are studying for, if applicable

            * `` - Not studying for a degree
            * `First degree` - First Degree (Bachelor's / Undergraduate Master's)
            * `Postgraduate Master's` - Postgraduate Master's
            * `Doctorate` - Doctorate
            * `Other` - Other
        internal_comment (Union[Unset, str]): Internal notes about the user that will not be displayed to the user
        service_user (Union[None, Unset, bool]): Service user is True if user type is SERVICE.
        email_confirmed_at (Union[None, Unset, datetime.datetime]):
        conditions_accepted_at (Union[None, Unset, datetime.datetime]):
        approved_for_root_at (Union[None, Unset, datetime.datetime]):
        user_reason (Union[Unset, str]): Indicate why the user has been suspended
        internal_reason (Union[Unset, str]): Any internal details about the user's suspension that should not be
            displayed to the user
        institution (Union['InstitutionList', None, Unset]):
        otp_required (Union[None, Unset, bool]): OTP is now always required.
        event (Union[None, Unset, str]):
        responsible_users (Union[Unset, List['UserList']]):
        user_type (Union[Unset, UserTypeEnum]): * `STANDARD` - Standard
            * `SERVICE` - Service User
            * `TRAINING` - Training Account
            * `SHARED` - Shared User
        lifecycle_state (Union[Unset, LifecycleStateEnum]): * `NORMAL` - Normal
            * `AWAITING_CLEANUP` - Awaiting Cleanup
            * `DORMANT` - Dormant
        deactivated_at (Union[None, Unset, datetime.datetime]): Date on which this account was deactivated.
    """

    id: Union[Unset, int] = UNSET
    account: Union[Unset, "Account"] = UNSET
    last_login: Union[None, Unset, datetime.datetime] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    is_staff: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    date_joined: Union[Unset, datetime.datetime] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    discipline: Union[Unset, DisciplineEnum] = UNSET
    degree: Union[BlankEnum, DegreeEnum, Unset] = UNSET
    internal_comment: Union[Unset, str] = UNSET
    service_user: Union[None, Unset, bool] = UNSET
    email_confirmed_at: Union[None, Unset, datetime.datetime] = UNSET
    conditions_accepted_at: Union[None, Unset, datetime.datetime] = UNSET
    approved_for_root_at: Union[None, Unset, datetime.datetime] = UNSET
    user_reason: Union[Unset, str] = UNSET
    internal_reason: Union[Unset, str] = UNSET
    institution: Union["InstitutionList", None, Unset] = UNSET
    otp_required: Union[None, Unset, bool] = UNSET
    event: Union[None, Unset, str] = UNSET
    responsible_users: Union[Unset, List["UserList"]] = UNSET
    user_type: Union[Unset, UserTypeEnum] = UNSET
    lifecycle_state: Union[Unset, LifecycleStateEnum] = UNSET
    deactivated_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.institution_list import InstitutionList

        id = self.id

        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        last_login: Union[None, Unset, str]
        if isinstance(self.last_login, Unset):
            last_login = UNSET
        elif isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        is_superuser = self.is_superuser

        username = self.username

        email = self.email

        is_staff = self.is_staff

        is_active = self.is_active

        date_joined: Union[Unset, str] = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        first_name = self.first_name

        last_name = self.last_name

        discipline: Union[Unset, str] = UNSET
        if not isinstance(self.discipline, Unset):
            discipline = self.discipline.value

        degree: Union[Unset, str]
        if isinstance(self.degree, Unset):
            degree = UNSET
        elif isinstance(self.degree, DegreeEnum):
            degree = self.degree.value
        else:
            degree = self.degree.value

        internal_comment = self.internal_comment

        service_user: Union[None, Unset, bool]
        if isinstance(self.service_user, Unset):
            service_user = UNSET
        else:
            service_user = self.service_user

        email_confirmed_at: Union[None, Unset, str]
        if isinstance(self.email_confirmed_at, Unset):
            email_confirmed_at = UNSET
        elif isinstance(self.email_confirmed_at, datetime.datetime):
            email_confirmed_at = self.email_confirmed_at.isoformat()
        else:
            email_confirmed_at = self.email_confirmed_at

        conditions_accepted_at: Union[None, Unset, str]
        if isinstance(self.conditions_accepted_at, Unset):
            conditions_accepted_at = UNSET
        elif isinstance(self.conditions_accepted_at, datetime.datetime):
            conditions_accepted_at = self.conditions_accepted_at.isoformat()
        else:
            conditions_accepted_at = self.conditions_accepted_at

        approved_for_root_at: Union[None, Unset, str]
        if isinstance(self.approved_for_root_at, Unset):
            approved_for_root_at = UNSET
        elif isinstance(self.approved_for_root_at, datetime.datetime):
            approved_for_root_at = self.approved_for_root_at.isoformat()
        else:
            approved_for_root_at = self.approved_for_root_at

        user_reason = self.user_reason

        internal_reason = self.internal_reason

        institution: Union[Dict[str, Any], None, Unset]
        if isinstance(self.institution, Unset):
            institution = UNSET
        elif isinstance(self.institution, InstitutionList):
            institution = self.institution.to_dict()
        else:
            institution = self.institution

        otp_required: Union[None, Unset, bool]
        if isinstance(self.otp_required, Unset):
            otp_required = UNSET
        else:
            otp_required = self.otp_required

        event: Union[None, Unset, str]
        if isinstance(self.event, Unset):
            event = UNSET
        else:
            event = self.event

        responsible_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responsible_users, Unset):
            responsible_users = []
            for responsible_users_item_data in self.responsible_users:
                responsible_users_item = responsible_users_item_data.to_dict()
                responsible_users.append(responsible_users_item)

        user_type: Union[Unset, str] = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = self.user_type.value

        lifecycle_state: Union[Unset, str] = UNSET
        if not isinstance(self.lifecycle_state, Unset):
            lifecycle_state = self.lifecycle_state.value

        deactivated_at: Union[None, Unset, str]
        if isinstance(self.deactivated_at, Unset):
            deactivated_at = UNSET
        elif isinstance(self.deactivated_at, datetime.datetime):
            deactivated_at = self.deactivated_at.isoformat()
        else:
            deactivated_at = self.deactivated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account is not UNSET:
            field_dict["account"] = account
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if discipline is not UNSET:
            field_dict["discipline"] = discipline
        if degree is not UNSET:
            field_dict["degree"] = degree
        if internal_comment is not UNSET:
            field_dict["internal_comment"] = internal_comment
        if service_user is not UNSET:
            field_dict["service_user"] = service_user
        if email_confirmed_at is not UNSET:
            field_dict["email_confirmed_at"] = email_confirmed_at
        if conditions_accepted_at is not UNSET:
            field_dict["conditions_accepted_at"] = conditions_accepted_at
        if approved_for_root_at is not UNSET:
            field_dict["approved_for_root_at"] = approved_for_root_at
        if user_reason is not UNSET:
            field_dict["user_reason"] = user_reason
        if internal_reason is not UNSET:
            field_dict["internal_reason"] = internal_reason
        if institution is not UNSET:
            field_dict["institution"] = institution
        if otp_required is not UNSET:
            field_dict["otp_required"] = otp_required
        if event is not UNSET:
            field_dict["event"] = event
        if responsible_users is not UNSET:
            field_dict["responsible_users"] = responsible_users
        if user_type is not UNSET:
            field_dict["user_type"] = user_type
        if lifecycle_state is not UNSET:
            field_dict["lifecycle_state"] = lifecycle_state
        if deactivated_at is not UNSET:
            field_dict["deactivated_at"] = deactivated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        account: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.account, Unset):
            account = (None, json.dumps(self.account.to_dict()).encode(), "application/json")

        last_login: Union[None, Unset, datetime.datetime]
        if isinstance(self.last_login, Unset):
            last_login = UNSET
        elif isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat().encode()
        else:
            last_login = self.last_login

        is_superuser = (
            self.is_superuser
            if isinstance(self.is_superuser, Unset)
            else (None, str(self.is_superuser).encode(), "text/plain")
        )

        username = (
            self.username if isinstance(self.username, Unset) else (None, str(self.username).encode(), "text/plain")
        )

        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")

        is_staff = (
            self.is_staff if isinstance(self.is_staff, Unset) else (None, str(self.is_staff).encode(), "text/plain")
        )

        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )

        date_joined: Union[Unset, bytes] = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat().encode()

        first_name = (
            self.first_name
            if isinstance(self.first_name, Unset)
            else (None, str(self.first_name).encode(), "text/plain")
        )

        last_name = (
            self.last_name if isinstance(self.last_name, Unset) else (None, str(self.last_name).encode(), "text/plain")
        )

        discipline: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.discipline, Unset):
            discipline = (None, str(self.discipline.value).encode(), "text/plain")

        degree: Union[BlankEnum, DegreeEnum, Unset]
        if isinstance(self.degree, Unset):
            degree = UNSET
        elif isinstance(self.degree, DegreeEnum):
            degree = (None, str(self.degree.value).encode(), "text/plain")
        else:
            degree = (None, str(self.degree.value).encode(), "text/plain")

        internal_comment = (
            self.internal_comment
            if isinstance(self.internal_comment, Unset)
            else (None, str(self.internal_comment).encode(), "text/plain")
        )

        service_user: Union[None, Unset, bool]
        if isinstance(self.service_user, Unset):
            service_user = UNSET
        else:
            service_user = self.service_user

        email_confirmed_at: Union[None, Unset, datetime.datetime]
        if isinstance(self.email_confirmed_at, Unset):
            email_confirmed_at = UNSET
        elif isinstance(self.email_confirmed_at, datetime.datetime):
            email_confirmed_at = self.email_confirmed_at.isoformat().encode()
        else:
            email_confirmed_at = self.email_confirmed_at

        conditions_accepted_at: Union[None, Unset, datetime.datetime]
        if isinstance(self.conditions_accepted_at, Unset):
            conditions_accepted_at = UNSET
        elif isinstance(self.conditions_accepted_at, datetime.datetime):
            conditions_accepted_at = self.conditions_accepted_at.isoformat().encode()
        else:
            conditions_accepted_at = self.conditions_accepted_at

        approved_for_root_at: Union[None, Unset, datetime.datetime]
        if isinstance(self.approved_for_root_at, Unset):
            approved_for_root_at = UNSET
        elif isinstance(self.approved_for_root_at, datetime.datetime):
            approved_for_root_at = self.approved_for_root_at.isoformat().encode()
        else:
            approved_for_root_at = self.approved_for_root_at

        user_reason = (
            self.user_reason
            if isinstance(self.user_reason, Unset)
            else (None, str(self.user_reason).encode(), "text/plain")
        )

        internal_reason = (
            self.internal_reason
            if isinstance(self.internal_reason, Unset)
            else (None, str(self.internal_reason).encode(), "text/plain")
        )

        institution: Union[None, Tuple[None, bytes, str], Unset]
        if isinstance(self.institution, Unset):
            institution = UNSET
        elif isinstance(self.institution, InstitutionList):
            institution = (None, json.dumps(self.institution.to_dict()).encode(), "application/json")
        else:
            institution = self.institution

        otp_required: Union[None, Unset, bool]
        if isinstance(self.otp_required, Unset):
            otp_required = UNSET
        else:
            otp_required = self.otp_required

        event: Union[None, Unset, str]
        if isinstance(self.event, Unset):
            event = UNSET
        else:
            event = self.event

        responsible_users: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.responsible_users, Unset):
            _temp_responsible_users = []
            for responsible_users_item_data in self.responsible_users:
                responsible_users_item = responsible_users_item_data.to_dict()
                _temp_responsible_users.append(responsible_users_item)
            responsible_users = (None, json.dumps(_temp_responsible_users).encode(), "application/json")

        user_type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = (None, str(self.user_type.value).encode(), "text/plain")

        lifecycle_state: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.lifecycle_state, Unset):
            lifecycle_state = (None, str(self.lifecycle_state.value).encode(), "text/plain")

        deactivated_at: Union[None, Unset, datetime.datetime]
        if isinstance(self.deactivated_at, Unset):
            deactivated_at = UNSET
        elif isinstance(self.deactivated_at, datetime.datetime):
            deactivated_at = self.deactivated_at.isoformat().encode()
        else:
            deactivated_at = self.deactivated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account is not UNSET:
            field_dict["account"] = account
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if discipline is not UNSET:
            field_dict["discipline"] = discipline
        if degree is not UNSET:
            field_dict["degree"] = degree
        if internal_comment is not UNSET:
            field_dict["internal_comment"] = internal_comment
        if service_user is not UNSET:
            field_dict["service_user"] = service_user
        if email_confirmed_at is not UNSET:
            field_dict["email_confirmed_at"] = email_confirmed_at
        if conditions_accepted_at is not UNSET:
            field_dict["conditions_accepted_at"] = conditions_accepted_at
        if approved_for_root_at is not UNSET:
            field_dict["approved_for_root_at"] = approved_for_root_at
        if user_reason is not UNSET:
            field_dict["user_reason"] = user_reason
        if internal_reason is not UNSET:
            field_dict["internal_reason"] = internal_reason
        if institution is not UNSET:
            field_dict["institution"] = institution
        if otp_required is not UNSET:
            field_dict["otp_required"] = otp_required
        if event is not UNSET:
            field_dict["event"] = event
        if responsible_users is not UNSET:
            field_dict["responsible_users"] = responsible_users
        if user_type is not UNSET:
            field_dict["user_type"] = user_type
        if lifecycle_state is not UNSET:
            field_dict["lifecycle_state"] = lifecycle_state
        if deactivated_at is not UNSET:
            field_dict["deactivated_at"] = deactivated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account
        from ..models.institution_list import InstitutionList
        from ..models.user_list import UserList

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _account = d.pop("account", UNSET)
        account: Union[Unset, Account]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = Account.from_dict(_account)

        def _parse_last_login(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = isoparse(data)

                return last_login_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_login = _parse_last_login(d.pop("last_login", UNSET))

        is_superuser = d.pop("is_superuser", UNSET)

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        is_active = d.pop("is_active", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: Union[Unset, datetime.datetime]
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _discipline = d.pop("discipline", UNSET)
        discipline: Union[Unset, DisciplineEnum]
        if isinstance(_discipline, Unset):
            discipline = UNSET
        else:
            discipline = DisciplineEnum(_discipline)

        def _parse_degree(data: object) -> Union[BlankEnum, DegreeEnum, Unset]:
            if isinstance(data, Unset):
                return data
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

        degree = _parse_degree(d.pop("degree", UNSET))

        internal_comment = d.pop("internal_comment", UNSET)

        def _parse_service_user(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        service_user = _parse_service_user(d.pop("service_user", UNSET))

        def _parse_email_confirmed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                email_confirmed_at_type_0 = isoparse(data)

                return email_confirmed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        email_confirmed_at = _parse_email_confirmed_at(d.pop("email_confirmed_at", UNSET))

        def _parse_conditions_accepted_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conditions_accepted_at_type_0 = isoparse(data)

                return conditions_accepted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        conditions_accepted_at = _parse_conditions_accepted_at(d.pop("conditions_accepted_at", UNSET))

        def _parse_approved_for_root_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_for_root_at_type_0 = isoparse(data)

                return approved_for_root_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        approved_for_root_at = _parse_approved_for_root_at(d.pop("approved_for_root_at", UNSET))

        user_reason = d.pop("user_reason", UNSET)

        internal_reason = d.pop("internal_reason", UNSET)

        def _parse_institution(data: object) -> Union["InstitutionList", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                institution_type_1 = InstitutionList.from_dict(data)

                return institution_type_1
            except:  # noqa: E722
                pass
            return cast(Union["InstitutionList", None, Unset], data)

        institution = _parse_institution(d.pop("institution", UNSET))

        def _parse_otp_required(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        otp_required = _parse_otp_required(d.pop("otp_required", UNSET))

        def _parse_event(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        event = _parse_event(d.pop("event", UNSET))

        responsible_users = []
        _responsible_users = d.pop("responsible_users", UNSET)
        for responsible_users_item_data in _responsible_users or []:
            responsible_users_item = UserList.from_dict(responsible_users_item_data)

            responsible_users.append(responsible_users_item)

        _user_type = d.pop("user_type", UNSET)
        user_type: Union[Unset, UserTypeEnum]
        if isinstance(_user_type, Unset):
            user_type = UNSET
        else:
            user_type = UserTypeEnum(_user_type)

        _lifecycle_state = d.pop("lifecycle_state", UNSET)
        lifecycle_state: Union[Unset, LifecycleStateEnum]
        if isinstance(_lifecycle_state, Unset):
            lifecycle_state = UNSET
        else:
            lifecycle_state = LifecycleStateEnum(_lifecycle_state)

        def _parse_deactivated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deactivated_at_type_0 = isoparse(data)

                return deactivated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deactivated_at = _parse_deactivated_at(d.pop("deactivated_at", UNSET))

        patched_user = cls(
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
            lifecycle_state=lifecycle_state,
            deactivated_at=deactivated_at,
        )

        patched_user.additional_properties = d
        return patched_user

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
