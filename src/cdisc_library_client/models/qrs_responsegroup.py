from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qrs_responsegroup_links import QrsResponsegroupLinks


T = TypeVar("T", bound="QrsResponsegroup")


@_attrs_define
class QrsResponsegroup:
    """
    Attributes:
        label (Union[Unset, str]):  Example: 01 to 08.
        field_links (Union[Unset, QrsResponsegroupLinks]):
    """

    label: Union[Unset, str] = UNSET
    field_links: Union[Unset, "QrsResponsegroupLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qrs_responsegroup_links import QrsResponsegroupLinks

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, QrsResponsegroupLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = QrsResponsegroupLinks.from_dict(_field_links)

        qrs_responsegroup = cls(
            label=label,
            field_links=field_links,
        )

        qrs_responsegroup.additional_properties = d
        return qrs_responsegroup

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
