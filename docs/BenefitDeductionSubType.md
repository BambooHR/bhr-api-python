# BenefitDeductionSubType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The sub-type deduction type ID (always an integer). | [optional] 
**deduction_type_name** | **str** | The display name of the sub-type. | [optional] 
**default_deduction_code** | **str** | The default payroll deduction code for this sub-type. | [optional] 
**allowable_benefit_types** | **List[str]** | Benefit plan types this sub-type applies to. | [optional] 
**non_benefit_deduction_type** | **bool** | Whether this is a non-benefit deduction type. | [optional] 
**can_be_collected_by_trax** | **bool** | Whether this sub-type can be collected via Trax Payroll. | [optional] 
**additional_description** | **str** | Additional description for display purposes. | [optional] 
**hide_annual_max** | **bool** | Whether the annual maximum field should be hidden. | [optional] 
**managed_deduction_type** | **str** | The managed deduction type identifier, if applicable. Null if not managed. | [optional] 
**sub_types** | **List[object]** | Always an empty array for sub-types. | [optional] 
**sub_type_text** | **str** | Sub-type selection label. Empty string for leaf types. | [optional] 
**deduction_note** | **str** | Informational note for this sub-type. | [optional] 
**deduction_note_link** | **str** | URL for the deduction note link. | [optional] 
**deduction_note_link_text** | **str** | Display text for the deduction note link. | [optional] 

## Example

```python
from bamboohr_sdk.models.benefit_deduction_sub_type import BenefitDeductionSubType

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitDeductionSubType from a JSON string
benefit_deduction_sub_type_instance = BenefitDeductionSubType.from_json(json)
# print the JSON string representation of the object
print(BenefitDeductionSubType.to_json())

# convert the object into a dict
benefit_deduction_sub_type_dict = benefit_deduction_sub_type_instance.to_dict()
# create an instance of BenefitDeductionSubType from a dict
benefit_deduction_sub_type_from_dict = BenefitDeductionSubType.from_dict(benefit_deduction_sub_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


