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
    from ..models.root_sdtmig_dataset_variable_ref import RootSdtmigDatasetVariableRef
    from ..models.sdtmig_dataset_variable_ref_version import (
        SdtmigDatasetVariableRefVersion,
    )


T = TypeVar("T", bound="RootSdtmigDatasetVariableLinks")


@_attrs_define
class RootSdtmigDatasetVariableLinks:
    """
    Attributes:
        self_ (Union[Unset, RootSdtmigDatasetVariableRef]):
        versions (Union[Unset, list['SdtmigDatasetVariableRefVersion']]):
    """

    self_: Union[Unset, "RootSdtmigDatasetVariableRef"] = UNSET
    versions: Union[Unset, list["SdtmigDatasetVariableRefVersion"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        versions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.root_sdtmig_dataset_variable_ref import (
            RootSdtmigDatasetVariableRef,
        )
        from ..models.sdtmig_dataset_variable_ref_version import (
            SdtmigDatasetVariableRefVersion,
        )

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, RootSdtmigDatasetVariableRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = RootSdtmigDatasetVariableRef.from_dict(_self_)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            versions_item = SdtmigDatasetVariableRefVersion.from_dict(
                versions_item_data
            )

            versions.append(versions_item)

        root_sdtmig_dataset_variable_links = cls(
            self_=self_,
            versions=versions,
        )

        root_sdtmig_dataset_variable_links.additional_properties = d
        return root_sdtmig_dataset_variable_links

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
