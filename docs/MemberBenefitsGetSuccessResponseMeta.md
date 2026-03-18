# MemberBenefitsGetSuccessResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The current page number. | [optional] 
**page_size** | **int** | The number of items per page. | [optional] 
**total_pages** | **int** | Total number of pages available. | [optional] 
**total_items** | **int** | Total number of member records across all pages. | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefits_get_success_response_meta import MemberBenefitsGetSuccessResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitsGetSuccessResponseMeta from a JSON string
member_benefits_get_success_response_meta_instance = MemberBenefitsGetSuccessResponseMeta.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitsGetSuccessResponseMeta.to_json())

# convert the object into a dict
member_benefits_get_success_response_meta_dict = member_benefits_get_success_response_meta_instance.to_dict()
# create an instance of MemberBenefitsGetSuccessResponseMeta from a dict
member_benefits_get_success_response_meta_from_dict = MemberBenefitsGetSuccessResponseMeta.from_dict(member_benefits_get_success_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


