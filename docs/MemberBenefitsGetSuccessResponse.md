# MemberBenefitsGetSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MemberBenefitsGetSuccessResponseDataInner]**](MemberBenefitsGetSuccessResponseDataInner.md) |  | [optional] 
**meta** | [**MemberBenefitsGetSuccessResponseMeta**](MemberBenefitsGetSuccessResponseMeta.md) |  | [optional] 
**links** | [**MemberBenefitsGetSuccessResponseLinks**](MemberBenefitsGetSuccessResponseLinks.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefits_get_success_response import MemberBenefitsGetSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitsGetSuccessResponse from a JSON string
member_benefits_get_success_response_instance = MemberBenefitsGetSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitsGetSuccessResponse.to_json())

# convert the object into a dict
member_benefits_get_success_response_dict = member_benefits_get_success_response_instance.to_dict()
# create an instance of MemberBenefitsGetSuccessResponse from a dict
member_benefits_get_success_response_from_dict = MemberBenefitsGetSuccessResponse.from_dict(member_benefits_get_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


