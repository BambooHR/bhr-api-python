# MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the enrollment period (YYYY-MM-DD). | [optional] 
**end_date** | **date** | End date of the enrollment period (YYYY-MM-DD), or null if the enrollment has no calculated end date. | [optional] 
**status** | **str** | The enrollment status for this date range. | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefits_get_success_response_data_inner_plans_inner_date_ranges_inner import MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner from a JSON string
member_benefits_get_success_response_data_inner_plans_inner_date_ranges_inner_instance = MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner.to_json())

# convert the object into a dict
member_benefits_get_success_response_data_inner_plans_inner_date_ranges_inner_dict = member_benefits_get_success_response_data_inner_plans_inner_date_ranges_inner_instance.to_dict()
# create an instance of MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner from a dict
member_benefits_get_success_response_data_inner_plans_inner_date_ranges_inner_from_dict = MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner.from_dict(member_benefits_get_success_response_data_inner_plans_inner_date_ranges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


