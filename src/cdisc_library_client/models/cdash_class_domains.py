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
    from ..models.cdash_class_domains_links import CdashClassDomainsLinks


T = TypeVar("T", bound="CdashClassDomains")


@_attrs_define
class CdashClassDomains:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 5.
        name (Union[Unset, str]):  Example: Special-Purpose.
        label (Union[Unset, str]):  Example: Special-Purpose.
        description (Union[Unset, str]):  Example: This SDTM class contains a set of domains which do not conform to the
            Findings, Events or Interventions observation classes. The domains included are DM, CO, SE and SV. (Source:
            CDISC Controlled Terminology, GNRLOBSC, C103377, 2018-06-29).
        field_links (Union[Unset, CdashClassDomainsLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CdashClassDomainsLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdash_class_domains_links import CdashClassDomainsLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CdashClassDomainsLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CdashClassDomainsLinks.from_dict(_field_links)

        cdash_class_domains = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            field_links=field_links,
        )

        cdash_class_domains.additional_properties = d
        return cdash_class_domains

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
