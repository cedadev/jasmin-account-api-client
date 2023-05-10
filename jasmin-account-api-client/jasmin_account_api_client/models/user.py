import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.degree_enum import DegreeEnum
from ..models.discipline_enum import DisciplineEnum
from ..models.user_type_enum import UserTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.institution_list import InstitutionList
    from ..models.user_list import UserList


T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        id (int):
        account (Account):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
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
        institution (InstitutionList):
        responsible_users (List['UserList']):
        last_login (Optional[datetime.datetime]):
        is_superuser (Union[Unset, bool]): Designates that this user has all permissions without explicitly assigning
            them.
        email (Union[Unset, str]):
        is_staff (Union[Unset, bool]): Designates whether the user can log into this admin site.
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        degree (Union[BlankEnum, DegreeEnum, Unset]): The type of degree you are studying for, if applicable

            * `` - Not studying for a degree
            * `First degree` - First Degree (Bachelor's / Undergraduate Master's)
            * `Postgraduate Master's` - Postgraduate Master's
            * `Doctorate` - Doctorate
            * `Other` - Other
        internal_comment (Union[Unset, str]): Internal notes about the user that will not be displayed to the user
        service_user (Optional[bool]):
        email_confirmed_at (Optional[datetime.datetime]):
        conditions_accepted_at (Optional[datetime.datetime]):
        approved_for_root_at (Optional[datetime.datetime]):
        user_reason (Union[Unset, str]): Indicate why the user has been suspended
        internal_reason (Union[Unset, str]): Any internal details about the user's suspension that should not be
            displayed to the user
        otp_required (Union[Unset, bool]): Indicates if OTP verification is required at all times for this user.
        event (Union[Unset, None, str]): Training event account has been set up for.
        user_type (Union[Unset, UserTypeEnum]): * `STANDARD` - Standard
            * `SERVICE` - Service User
            * `TRAINING` - Training Account
            * `SHARED` - Shared User
        deactivated_at (Union[Unset, None, datetime.datetime]): Date on which this account was deactivated.
    """

    id: int
    account: "Account"
    username: str
    date_joined: datetime.datetime
    first_name: str
    last_name: str
    discipline: DisciplineEnum
    institution: "InstitutionList"
    responsible_users: List["UserList"]
    last_login: Optional[datetime.datetime]
    service_user: Optional[bool]
    email_confirmed_at: Optional[datetime.datetime]
    conditions_accepted_at: Optional[datetime.datetime]
    approved_for_root_at: Optional[datetime.datetime]
    is_superuser: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    is_staff: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    degree: Union[BlankEnum, DegreeEnum, Unset] = UNSET
    internal_comment: Union[Unset, str] = UNSET
    user_reason: Union[Unset, str] = UNSET
    internal_reason: Union[Unset, str] = UNSET
    otp_required: Union[Unset, bool] = UNSET
    event: Union[Unset, None, str] = UNSET
    user_type: Union[Unset, UserTypeEnum] = UNSET
    deactivated_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account = self.account.to_dict()

        username = self.username
        date_joined = self.date_joined.isoformat()

        first_name = self.first_name
        last_name = self.last_name
        discipline = self.discipline.value

        institution = self.institution.to_dict()

        responsible_users = []
        for responsible_users_item_data in self.responsible_users:
            responsible_users_item = responsible_users_item_data.to_dict()

            responsible_users.append(responsible_users_item)

        last_login = self.last_login.isoformat() if self.last_login else None

        is_superuser = self.is_superuser
        email = self.email
        is_staff = self.is_staff
        is_active = self.is_active
        degree: Union[Unset, str]
        if isinstance(self.degree, Unset):
            degree = UNSET

        elif isinstance(self.degree, DegreeEnum):
            degree = UNSET
            if not isinstance(self.degree, Unset):
                degree = self.degree.value

        else:
            degree = UNSET
            if not isinstance(self.degree, Unset):
                degree = self.degree.value

        internal_comment = self.internal_comment
        service_user = self.service_user
        email_confirmed_at = self.email_confirmed_at.isoformat() if self.email_confirmed_at else None

        conditions_accepted_at = self.conditions_accepted_at.isoformat() if self.conditions_accepted_at else None

        approved_for_root_at = self.approved_for_root_at.isoformat() if self.approved_for_root_at else None

        user_reason = self.user_reason
        internal_reason = self.internal_reason
        otp_required = self.otp_required
        event = self.event
        user_type: Union[Unset, str] = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = self.user_type.value

        deactivated_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.deactivated_at, Unset):
            deactivated_at = self.deactivated_at.isoformat() if self.deactivated_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "account": account,
                "username": username,
                "date_joined": date_joined,
                "first_name": first_name,
                "last_name": last_name,
                "discipline": discipline,
                "institution": institution,
                "responsible_users": responsible_users,
                "last_login": last_login,
                "service_user": service_user,
                "email_confirmed_at": email_confirmed_at,
                "conditions_accepted_at": conditions_accepted_at,
                "approved_for_root_at": approved_for_root_at,
            }
        )
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if email is not UNSET:
            field_dict["email"] = email
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if degree is not UNSET:
            field_dict["degree"] = degree
        if internal_comment is not UNSET:
            field_dict["internal_comment"] = internal_comment
        if user_reason is not UNSET:
            field_dict["user_reason"] = user_reason
        if internal_reason is not UNSET:
            field_dict["internal_reason"] = internal_reason
        if otp_required is not UNSET:
            field_dict["otp_required"] = otp_required
        if event is not UNSET:
            field_dict["event"] = event
        if user_type is not UNSET:
            field_dict["user_type"] = user_type
        if deactivated_at is not UNSET:
            field_dict["deactivated_at"] = deactivated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account
        from ..models.institution_list import InstitutionList
        from ..models.user_list import UserList

        d = src_dict.copy()
        id = d.pop("id")

        account = Account.from_dict(d.pop("account"))

        username = d.pop("username")

        date_joined = isoparse(d.pop("date_joined"))

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        discipline = DisciplineEnum(d.pop("discipline"))

        institution = InstitutionList.from_dict(d.pop("institution"))

        responsible_users = []
        _responsible_users = d.pop("responsible_users")
        for responsible_users_item_data in _responsible_users:
            responsible_users_item = UserList.from_dict(responsible_users_item_data)

            responsible_users.append(responsible_users_item)

        _last_login = d.pop("last_login")
        last_login: Optional[datetime.datetime]
        if _last_login is None:
            last_login = None
        else:
            last_login = isoparse(_last_login)

        is_superuser = d.pop("is_superuser", UNSET)

        email = d.pop("email", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_degree(data: object) -> Union[BlankEnum, DegreeEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _degree_type_0 = data
                degree_type_0: Union[Unset, DegreeEnum]
                if isinstance(_degree_type_0, Unset):
                    degree_type_0 = UNSET
                else:
                    degree_type_0 = DegreeEnum(_degree_type_0)

                return degree_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _degree_type_1 = data
            degree_type_1: Union[Unset, BlankEnum]
            if isinstance(_degree_type_1, Unset):
                degree_type_1 = UNSET
            else:
                degree_type_1 = BlankEnum(_degree_type_1)

            return degree_type_1

        degree = _parse_degree(d.pop("degree", UNSET))

        internal_comment = d.pop("internal_comment", UNSET)

        service_user = d.pop("service_user")

        _email_confirmed_at = d.pop("email_confirmed_at")
        email_confirmed_at: Optional[datetime.datetime]
        if _email_confirmed_at is None:
            email_confirmed_at = None
        else:
            email_confirmed_at = isoparse(_email_confirmed_at)

        _conditions_accepted_at = d.pop("conditions_accepted_at")
        conditions_accepted_at: Optional[datetime.datetime]
        if _conditions_accepted_at is None:
            conditions_accepted_at = None
        else:
            conditions_accepted_at = isoparse(_conditions_accepted_at)

        _approved_for_root_at = d.pop("approved_for_root_at")
        approved_for_root_at: Optional[datetime.datetime]
        if _approved_for_root_at is None:
            approved_for_root_at = None
        else:
            approved_for_root_at = isoparse(_approved_for_root_at)

        user_reason = d.pop("user_reason", UNSET)

        internal_reason = d.pop("internal_reason", UNSET)

        otp_required = d.pop("otp_required", UNSET)

        event = d.pop("event", UNSET)

        _user_type = d.pop("user_type", UNSET)
        user_type: Union[Unset, UserTypeEnum]
        if isinstance(_user_type, Unset):
            user_type = UNSET
        else:
            user_type = UserTypeEnum(_user_type)

        _deactivated_at = d.pop("deactivated_at", UNSET)
        deactivated_at: Union[Unset, None, datetime.datetime]
        if _deactivated_at is None:
            deactivated_at = None
        elif isinstance(_deactivated_at, Unset):
            deactivated_at = UNSET
        else:
            deactivated_at = isoparse(_deactivated_at)

        user = cls(
            id=id,
            account=account,
            username=username,
            date_joined=date_joined,
            first_name=first_name,
            last_name=last_name,
            discipline=discipline,
            institution=institution,
            responsible_users=responsible_users,
            last_login=last_login,
            is_superuser=is_superuser,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            degree=degree,
            internal_comment=internal_comment,
            service_user=service_user,
            email_confirmed_at=email_confirmed_at,
            conditions_accepted_at=conditions_accepted_at,
            approved_for_root_at=approved_for_root_at,
            user_reason=user_reason,
            internal_reason=internal_reason,
            otp_required=otp_required,
            event=event,
            user_type=user_type,
            deactivated_at=deactivated_at,
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
