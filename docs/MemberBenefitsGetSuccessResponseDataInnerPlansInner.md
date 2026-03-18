# MemberBenefitsGetSuccessResponseDataInnerPlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | The benefit plan ID. | [optional] 
**date_ranges** | [**List[MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner]**](MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefits_get_success_response_data_inner_plans_inner import MemberBenefitsGetSuccessResponseDataInnerPlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitsGetSuccessResponseDataInnerPlansInner from a JSON string
member_benefits_get_success_response_data_inner_plans_inner_instance = MemberBenefitsGetSuccessResponseDataInnerPlansInner.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitsGetSuccessResponseDataInnerPlansInner.to_json())

# convert the object into a dict
member_benefits_get_success_response_data_inner_plans_inner_dict = member_benefits_get_success_response_data_inner_plans_inner_instance.to_dict()
# create an instance of MemberBenefitsGetSuccessResponseDataInnerPlansInner from a dict
member_benefits_get_success_response_data_inner_plans_inner_from_dict = MemberBenefitsGetSuccessResponseDataInnerPlansInner.from_dict(member_benefits_get_success_response_data_inner_plans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


