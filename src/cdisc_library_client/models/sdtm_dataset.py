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
    from ..models.sdtm_dataset_links import SdtmDatasetLinks
    from ..models.sdtm_dataset_variable import SdtmDatasetVariable


T = TypeVar("T", bound="SdtmDataset")


@_attrs_define
class SdtmDataset:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 1.
        name (Union[Unset, str]):  Example: DM.
        label (Union[Unset, str]):  Example: Demographics.
        description (Union[Unset, str]):  Example: A special-purpose domain that includes a set of essential standard
            variables that describe each subject in a clinical study. It is the parent domain for all other observations for
            human clinical subjects. (Source: CDISC Controlled Terminology, DOMAIN, C49572, 2018-06-29).
        dataset_structure (Union[Unset, str]):  Example: One record per subject.
        field_links (Union[Unset, SdtmDatasetLinks]):
        dataset_variables (Union[Unset, list['SdtmDatasetVariable']]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    dataset_structure: Union[Unset, str] = UNSET
    field_links: Union[Unset, "SdtmDatasetLinks"] = UNSET
    dataset_variables: Union[Unset, list["SdtmDatasetVariable"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        dataset_structure = self.dataset_structure

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        dataset_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dataset_variables, Unset):
            dataset_variables = []
            for dataset_variables_item_data in self.dataset_variables:
                dataset_variables_item = dataset_variables_item_data.to_dict()
                dataset_variables.append(dataset_variables_item)

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
        if dataset_structure is not UNSET:
            field_dict["datasetStructure"] = dataset_structure
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if dataset_variables is not UNSET:
            field_dict["datasetVariables"] = dataset_variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtm_dataset_links import SdtmDatasetLinks
        from ..models.sdtm_dataset_variable import SdtmDatasetVariable

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        dataset_structure = d.pop("datasetStructure", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, SdtmDatasetLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SdtmDatasetLinks.from_dict(_field_links)

        dataset_variables = []
        _dataset_variables = d.pop("datasetVariables", UNSET)
        for dataset_variables_item_data in _dataset_variables or []:
            dataset_variables_item = SdtmDatasetVariable.from_dict(
                dataset_variables_item_data
            )

            dataset_variables.append(dataset_variables_item)

        sdtm_dataset = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            dataset_structure=dataset_structure,
            field_links=field_links,
            dataset_variables=dataset_variables,
        )

        sdtm_dataset.additional_properties = d
        return sdtm_dataset

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
