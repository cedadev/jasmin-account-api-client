from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.access import Access


T = TypeVar("T", bound="Role")


@_attrs_define
class Role:
    """Detail of role with holders.

    Attributes:
        id (int):
        name (str):
        accesses (List['Access']):
    """

    id: int
    name: str
    accesses: List["Access"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        accesses = []
        for accesses_item_data in self.accesses:
            accesses_item = accesses_item_data.to_dict()
            accesses.append(accesses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "accesses": accesses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access import Access

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        accesses = []
        _accesses = d.pop("accesses")
        for accesses_item_data in _accesses:
            accesses_item = Access.from_dict(accesses_item_data)

            accesses.append(accesses_item)

        role = cls(
            id=id,
            name=name,
            accesses=accesses,
        )

        role.additional_properties = d
        return role

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
