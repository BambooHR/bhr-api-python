# BenefitDeductionTypeId

The deduction type ID. Integer for leaf types (e.g. 1 for 401(k)); string slug for grouped parent types (e.g. \"pretax_subtype\").

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from bamboohr_sdk.models.benefit_deduction_type_id import BenefitDeductionTypeId

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitDeductionTypeId from a JSON string
benefit_deduction_type_id_instance = BenefitDeductionTypeId.from_json(json)
# print the JSON string representation of the object
print(BenefitDeductionTypeId.to_json())

# convert the object into a dict
benefit_deduction_type_id_dict = benefit_deduction_type_id_instance.to_dict()
# create an instance of BenefitDeductionTypeId from a dict
benefit_deduction_type_id_from_dict = BenefitDeductionTypeId.from_dict(benefit_deduction_type_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


