from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.country_enum import CountryEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstitutionList")


@_attrs_define
class InstitutionList:
    """
    Attributes:
        id (int):
        url (str):
        name (str):
        standard_user_count (int):
        domains (List[str]):
        country (Union[BlankEnum, CountryEnum, None, Unset]):
    """

    id: int
    url: str
    name: str
    standard_user_count: int
    domains: List[str]
    country: Union[BlankEnum, CountryEnum, None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        url = self.url

        name = self.name

        standard_user_count = self.standard_user_count

        domains = self.domains

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, CountryEnum):
            country = self.country.value
        elif isinstance(self.country, BlankEnum):
            country = self.country.value
        else:
            country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
                "standard_user_count": standard_user_count,
                "domains": domains,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        standard_user_count = d.pop("standard_user_count")

        domains = cast(List[str], d.pop("domains"))

        def _parse_country(data: object) -> Union[BlankEnum, CountryEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_0 = CountryEnum(data)

                return country_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_1 = BlankEnum(data)

                return country_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, CountryEnum, None, Unset], data)

        country = _parse_country(d.pop("country", UNSET))

        institution_list = cls(
            id=id,
            url=url,
            name=name,
            standard_user_count=standard_user_count,
            domains=domains,
            country=country,
        )

        institution_list.additional_properties = d
        return institution_list

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
