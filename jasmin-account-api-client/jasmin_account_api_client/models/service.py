from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.blank_enum import BlankEnum
from ..models.institution_countries_enum import InstitutionCountriesEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_list import CategoryList
    from ..models.role_list import RoleList


T = TypeVar("T", bound="Service")


@attr.s(auto_attribs=True)
class Service:
    """Full details of a service.

    Attributes:
        id (int):
        url (str):
        name (str): The name of the service. This is also used in URLs.
        category (CategoryList): Basic information about a service category.
        roles (List['RoleList']):
        summary (str): One-line description of the service, shown in listings. No special formatting allowed.
        description (Union[Unset, None, str]): Full description of the service, shown on the details page. Markdown
            formatting is allowed.
        approver_message (Union[Unset, None, str]): Service specific instructions to be added to the external approver
            message.
        institution_countries (Union[BlankEnum, InstitutionCountriesEnum, Unset]): Coutries a user's institute must be
            located to begin approval. Hold ctrl or cmd for mac to select multiple countries. Leave blank for any country.

            * `GB` - United Kingdom
            * `AF` - Afghanistan
            * `AX` - Åland Islands
            * `AL` - Albania
            * `DZ` - Algeria
            * `AS` - American Samoa
            * `AD` - Andorra
            * `AO` - Angola
            * `AI` - Anguilla
            * `AQ` - Antarctica
            * `AG` - Antigua and Barbuda
            * `AR` - Argentina
            * `AM` - Armenia
            * `AW` - Aruba
            * `AU` - Australia
            * `AT` - Austria
            * `AZ` - Azerbaijan
            * `BS` - Bahamas
            * `BH` - Bahrain
            * `BD` - Bangladesh
            * `BB` - Barbados
            * `BY` - Belarus
            * `BE` - Belgium
            * `BZ` - Belize
            * `BJ` - Benin
            * `BM` - Bermuda
            * `BT` - Bhutan
            * `BO` - Bolivia
            * `BQ` - Bonaire, Sint Eustatius and Saba
            * `BA` - Bosnia and Herzegovina
            * `BW` - Botswana
            * `BV` - Bouvet Island
            * `BR` - Brazil
            * `IO` - British Indian Ocean Territory
            * `BN` - Brunei
            * `BG` - Bulgaria
            * `BF` - Burkina Faso
            * `BI` - Burundi
            * `CV` - Cabo Verde
            * `KH` - Cambodia
            * `CM` - Cameroon
            * `CA` - Canada
            * `KY` - Cayman Islands
            * `CF` - Central African Republic
            * `TD` - Chad
            * `CL` - Chile
            * `CN` - China
            * `CX` - Christmas Island
            * `CC` - Cocos (Keeling) Islands
            * `CO` - Colombia
            * `KM` - Comoros
            * `CG` - Congo
            * `CD` - Congo (the Democratic Republic of the)
            * `CK` - Cook Islands
            * `CR` - Costa Rica
            * `CI` - Côte d'Ivoire
            * `HR` - Croatia
            * `CU` - Cuba
            * `CW` - Curaçao
            * `CY` - Cyprus
            * `CZ` - Czechia
            * `DK` - Denmark
            * `DJ` - Djibouti
            * `DM` - Dominica
            * `DO` - Dominican Republic
            * `EC` - Ecuador
            * `EG` - Egypt
            * `SV` - El Salvador
            * `GQ` - Equatorial Guinea
            * `ER` - Eritrea
            * `EE` - Estonia
            * `SZ` - Eswatini
            * `ET` - Ethiopia
            * `FK` - Falkland Islands (Malvinas)
            * `FO` - Faroe Islands
            * `FJ` - Fiji
            * `FI` - Finland
            * `FR` - France
            * `GF` - French Guiana
            * `PF` - French Polynesia
            * `TF` - French Southern Territories
            * `GA` - Gabon
            * `GM` - Gambia
            * `GE` - Georgia
            * `DE` - Germany
            * `GH` - Ghana
            * `GI` - Gibraltar
            * `GR` - Greece
            * `GL` - Greenland
            * `GD` - Grenada
            * `GP` - Guadeloupe
            * `GU` - Guam
            * `GT` - Guatemala
            * `GG` - Guernsey
            * `GN` - Guinea
            * `GW` - Guinea-Bissau
            * `GY` - Guyana
            * `HT` - Haiti
            * `HM` - Heard Island and McDonald Islands
            * `VA` - Holy See
            * `HN` - Honduras
            * `HK` - Hong Kong
            * `HU` - Hungary
            * `IS` - Iceland
            * `IN` - India
            * `ID` - Indonesia
            * `IR` - Iran
            * `IQ` - Iraq
            * `IE` - Ireland
            * `IM` - Isle of Man
            * `IL` - Israel
            * `IT` - Italy
            * `JM` - Jamaica
            * `JP` - Japan
            * `JE` - Jersey
            * `JO` - Jordan
            * `KZ` - Kazakhstan
            * `KE` - Kenya
            * `KI` - Kiribati
            * `KW` - Kuwait
            * `KG` - Kyrgyzstan
            * `LA` - Laos
            * `LV` - Latvia
            * `LB` - Lebanon
            * `LS` - Lesotho
            * `LR` - Liberia
            * `LY` - Libya
            * `LI` - Liechtenstein
            * `LT` - Lithuania
            * `LU` - Luxembourg
            * `MO` - Macao
            * `MG` - Madagascar
            * `MW` - Malawi
            * `MY` - Malaysia
            * `MV` - Maldives
            * `ML` - Mali
            * `MT` - Malta
            * `MH` - Marshall Islands
            * `MQ` - Martinique
            * `MR` - Mauritania
            * `MU` - Mauritius
            * `YT` - Mayotte
            * `MX` - Mexico
            * `FM` - Micronesia (Federated States of)
            * `MD` - Moldova
            * `MC` - Monaco
            * `MN` - Mongolia
            * `ME` - Montenegro
            * `MS` - Montserrat
            * `MA` - Morocco
            * `MZ` - Mozambique
            * `MM` - Myanmar
            * `NA` - Namibia
            * `NR` - Nauru
            * `NP` - Nepal
            * `NL` - Netherlands
            * `NC` - New Caledonia
            * `NZ` - New Zealand
            * `NI` - Nicaragua
            * `NE` - Niger
            * `NG` - Nigeria
            * `NU` - Niue
            * `NF` - Norfolk Island
            * `KP` - North Korea
            * `MK` - North Macedonia
            * `MP` - Northern Mariana Islands
            * `NO` - Norway
            * `OM` - Oman
            * `PK` - Pakistan
            * `PW` - Palau
            * `PS` - Palestine, State of
            * `PA` - Panama
            * `PG` - Papua New Guinea
            * `PY` - Paraguay
            * `PE` - Peru
            * `PH` - Philippines
            * `PN` - Pitcairn
            * `PL` - Poland
            * `PT` - Portugal
            * `PR` - Puerto Rico
            * `QA` - Qatar
            * `RE` - Réunion
            * `RO` - Romania
            * `RU` - Russia
            * `RW` - Rwanda
            * `BL` - Saint Barthélemy
            * `SH` - Saint Helena, Ascension and Tristan da Cunha
            * `KN` - Saint Kitts and Nevis
            * `LC` - Saint Lucia
            * `MF` - Saint Martin (French part)
            * `PM` - Saint Pierre and Miquelon
            * `VC` - Saint Vincent and the Grenadines
            * `WS` - Samoa
            * `SM` - San Marino
            * `ST` - Sao Tome and Principe
            * `SA` - Saudi Arabia
            * `SN` - Senegal
            * `RS` - Serbia
            * `SC` - Seychelles
            * `SL` - Sierra Leone
            * `SG` - Singapore
            * `SX` - Sint Maarten (Dutch part)
            * `SK` - Slovakia
            * `SI` - Slovenia
            * `SB` - Solomon Islands
            * `SO` - Somalia
            * `ZA` - South Africa
            * `GS` - South Georgia and the South Sandwich Islands
            * `KR` - South Korea
            * `SS` - South Sudan
            * `ES` - Spain
            * `LK` - Sri Lanka
            * `SD` - Sudan
            * `SR` - Suriname
            * `SJ` - Svalbard and Jan Mayen
            * `SE` - Sweden
            * `CH` - Switzerland
            * `SY` - Syria
            * `TW` - Taiwan
            * `TJ` - Tajikistan
            * `TZ` - Tanzania
            * `TH` - Thailand
            * `TL` - Timor-Leste
            * `TG` - Togo
            * `TK` - Tokelau
            * `TO` - Tonga
            * `TT` - Trinidad and Tobago
            * `TN` - Tunisia
            * `TR` - Türkiye
            * `TM` - Turkmenistan
            * `TC` - Turks and Caicos Islands
            * `TV` - Tuvalu
            * `UG` - Uganda
            * `UA` - Ukraine
            * `AE` - United Arab Emirates
            * `UM` - United States Minor Outlying Islands
            * `US` - United States of America
            * `UY` - Uruguay
            * `UZ` - Uzbekistan
            * `VU` - Vanuatu
            * `VE` - Venezuela
            * `VN` - Vietnam
            * `VG` - Virgin Islands (British)
            * `VI` - Virgin Islands (U.S.)
            * `WF` - Wallis and Futuna
            * `EH` - Western Sahara
            * `YE` - Yemen
            * `ZM` - Zambia
            * `ZW` - Zimbabwe
        hidden (Union[Unset, bool]): Prevents the service appearing in listings unless the user has an active grant or
            request for it. The service details page will still be accessible to anybody who knows the URL.
        position (Union[Unset, int]): Number defining where the service appears in listings. Services are ordered in
            ascending order by category, then by this field, then alphabetically by name.
        ceda_managed (Union[Unset, bool]): Whether the service is managed by CEDA.
    """

    id: int
    url: str
    name: str
    category: "CategoryList"
    roles: List["RoleList"]
    summary: str
    description: Union[Unset, None, str] = UNSET
    approver_message: Union[Unset, None, str] = UNSET
    institution_countries: Union[BlankEnum, InstitutionCountriesEnum, Unset] = UNSET
    hidden: Union[Unset, bool] = UNSET
    position: Union[Unset, int] = UNSET
    ceda_managed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        name = self.name
        category = self.category.to_dict()

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()

            roles.append(roles_item)

        summary = self.summary
        description = self.description
        approver_message = self.approver_message
        institution_countries: Union[Unset, str]
        if isinstance(self.institution_countries, Unset):
            institution_countries = UNSET

        elif isinstance(self.institution_countries, InstitutionCountriesEnum):
            institution_countries = UNSET
            if not isinstance(self.institution_countries, Unset):
                institution_countries = self.institution_countries.value

        else:
            institution_countries = UNSET
            if not isinstance(self.institution_countries, Unset):
                institution_countries = self.institution_countries.value

        hidden = self.hidden
        position = self.position
        ceda_managed = self.ceda_managed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
                "category": category,
                "roles": roles,
                "summary": summary,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if approver_message is not UNSET:
            field_dict["approver_message"] = approver_message
        if institution_countries is not UNSET:
            field_dict["institution_countries"] = institution_countries
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if position is not UNSET:
            field_dict["position"] = position
        if ceda_managed is not UNSET:
            field_dict["ceda_managed"] = ceda_managed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_list import CategoryList
        from ..models.role_list import RoleList

        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        category = CategoryList.from_dict(d.pop("category"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RoleList.from_dict(roles_item_data)

            roles.append(roles_item)

        summary = d.pop("summary")

        description = d.pop("description", UNSET)

        approver_message = d.pop("approver_message", UNSET)

        def _parse_institution_countries(data: object) -> Union[BlankEnum, InstitutionCountriesEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _institution_countries_type_0 = data
                institution_countries_type_0: Union[Unset, InstitutionCountriesEnum]
                if isinstance(_institution_countries_type_0, Unset):
                    institution_countries_type_0 = UNSET
                else:
                    institution_countries_type_0 = InstitutionCountriesEnum(_institution_countries_type_0)

                return institution_countries_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _institution_countries_type_1 = data
            institution_countries_type_1: Union[Unset, BlankEnum]
            if isinstance(_institution_countries_type_1, Unset):
                institution_countries_type_1 = UNSET
            else:
                institution_countries_type_1 = BlankEnum(_institution_countries_type_1)

            return institution_countries_type_1

        institution_countries = _parse_institution_countries(d.pop("institution_countries", UNSET))

        hidden = d.pop("hidden", UNSET)

        position = d.pop("position", UNSET)

        ceda_managed = d.pop("ceda_managed", UNSET)

        service = cls(
            id=id,
            url=url,
            name=name,
            category=category,
            roles=roles,
            summary=summary,
            description=description,
            approver_message=approver_message,
            institution_countries=institution_countries,
            hidden=hidden,
            position=position,
            ceda_managed=ceda_managed,
        )

        service.additional_properties = d
        return service

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
