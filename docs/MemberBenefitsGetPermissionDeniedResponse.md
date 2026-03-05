# MemberBenefitsGetPermissionDeniedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefits_get_permission_denied_response import MemberBenefitsGetPermissionDeniedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitsGetPermissionDeniedResponse from a JSON string
member_benefits_get_permission_denied_response_instance = MemberBenefitsGetPermissionDeniedResponse.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitsGetPermissionDeniedResponse.to_json())

# convert the object into a dict
member_benefits_get_permission_denied_response_dict = member_benefits_get_permission_denied_response_instance.to_dict()
# create an instance of MemberBenefitsGetPermissionDeniedResponse from a dict
member_benefits_get_permission_denied_response_from_dict = MemberBenefitsGetPermissionDeniedResponse.from_dict(member_benefits_get_permission_denied_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


