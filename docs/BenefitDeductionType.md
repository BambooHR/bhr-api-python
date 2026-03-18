# BenefitDeductionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**BenefitDeductionTypeId**](BenefitDeductionTypeId.md) |  | [optional] 
**deduction_type_name** | **str** | The display name of the deduction type. | [optional] 
**default_deduction_code** | **str** | The default payroll deduction code for this type. | [optional] 
**allowable_benefit_types** | **List[str]** | The benefit plan types this deduction type can be applied to (e.g. \&quot;health\&quot;, \&quot;dental\&quot;, \&quot;retirement\&quot;). | [optional] 
**non_benefit_deduction_type** | **bool** | Whether this is a non-benefit deduction type (e.g. garnishments). | [optional] 
**can_be_collected_by_trax** | **bool** | Whether this deduction type can be collected via Trax Payroll. | [optional] 
**additional_description** | **str** | An optional additional description for display purposes. | [optional] 
**hide_annual_max** | **bool** | Whether the annual maximum field should be hidden for this deduction type. | [optional] 
**managed_deduction_type** | **str** | The managed deduction type identifier, if applicable. Null if not managed. | [optional] 
**sub_types** | [**List[BenefitDeductionSubType]**](BenefitDeductionSubType.md) | Child deduction types grouped under this parent. Each entry has the same shape as a top-level deduction type. Empty array if this type has no sub-types. | [optional] 
**sub_type_text** | **str** | A label or question displayed alongside sub-type selection (e.g. \&quot;Reportable on the W-2?\&quot;). Empty string for types without sub-types. | [optional] 
**deduction_note** | **str** | An informational note to display to the user when configuring this deduction type. | [optional] 
**deduction_note_link** | **str** | A URL for a \&quot;learn more\&quot; link associated with the deduction note. | [optional] 
**deduction_note_link_text** | **str** | The display text for the deduction note link. | [optional] 

## Example

```python
from bamboohr_sdk.models.benefit_deduction_type import BenefitDeductionType

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitDeductionType from a JSON string
benefit_deduction_type_instance = BenefitDeductionType.from_json(json)
# print the JSON string representation of the object
print(BenefitDeductionType.to_json())

# convert the object into a dict
benefit_deduction_type_dict = benefit_deduction_type_instance.to_dict()
# create an instance of BenefitDeductionType from a dict
benefit_deduction_type_from_dict = BenefitDeductionType.from_dict(benefit_deduction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


