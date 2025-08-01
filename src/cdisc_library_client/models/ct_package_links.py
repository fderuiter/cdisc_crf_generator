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
    from ..models.ct_package_ref import CtPackageRef


T = TypeVar("T", bound="CtPackageLinks")


@_attrs_define
class CtPackageLinks:
    """
    Attributes:
        self_ (Union[Unset, CtPackageRef]):
        prior_version (Union[Unset, CtPackageRef]):
    """

    self_: Union[Unset, "CtPackageRef"] = UNSET
    prior_version: Union[Unset, "CtPackageRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ct_package_ref import CtPackageRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CtPackageRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CtPackageRef.from_dict(_self_)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, CtPackageRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = CtPackageRef.from_dict(_prior_version)

        ct_package_links = cls(
            self_=self_,
            prior_version=prior_version,
        )

        ct_package_links.additional_properties = d
        return ct_package_links

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
