# MemberBenefitsGetSuccessResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The member identifier. Formatted as \&quot;employee.{id}\&quot; for employees and \&quot;dependent.{id}\&quot; for dependents. | [optional] 
**subscriber_id** | **str** | The employee ID of the plan subscriber as a string. For dependent members, this is the ID of the employee they are enrolled under. | [optional] 
**plans** | [**List[MemberBenefitsGetSuccessResponseDataInnerPlansInner]**](MemberBenefitsGetSuccessResponseDataInnerPlansInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefits_get_success_response_data_inner import MemberBenefitsGetSuccessResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitsGetSuccessResponseDataInner from a JSON string
member_benefits_get_success_response_data_inner_instance = MemberBenefitsGetSuccessResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitsGetSuccessResponseDataInner.to_json())

# convert the object into a dict
member_benefits_get_success_response_data_inner_dict = member_benefits_get_success_response_data_inner_instance.to_dict()
# create an instance of MemberBenefitsGetSuccessResponseDataInner from a dict
member_benefits_get_success_response_data_inner_from_dict = MemberBenefitsGetSuccessResponseDataInner.from_dict(member_benefits_get_success_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


