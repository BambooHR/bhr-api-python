# MemberBenefitsGetValidationErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefits_get_validation_error_response import MemberBenefitsGetValidationErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitsGetValidationErrorResponse from a JSON string
member_benefits_get_validation_error_response_instance = MemberBenefitsGetValidationErrorResponse.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitsGetValidationErrorResponse.to_json())

# convert the object into a dict
member_benefits_get_validation_error_response_dict = member_benefits_get_validation_error_response_instance.to_dict()
# create an instance of MemberBenefitsGetValidationErrorResponse from a dict
member_benefits_get_validation_error_response_from_dict = MemberBenefitsGetValidationErrorResponse.from_dict(member_benefits_get_validation_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


