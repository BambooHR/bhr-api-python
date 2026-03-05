# MemberBenefitsGetSuccessResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**MemberBenefitsGetSuccessResponseLinksNext**](MemberBenefitsGetSuccessResponseLinksNext.md) |  | [optional] 
**prev** | [**MemberBenefitsGetSuccessResponseLinksPrev**](MemberBenefitsGetSuccessResponseLinksPrev.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefits_get_success_response_links import MemberBenefitsGetSuccessResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitsGetSuccessResponseLinks from a JSON string
member_benefits_get_success_response_links_instance = MemberBenefitsGetSuccessResponseLinks.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitsGetSuccessResponseLinks.to_json())

# convert the object into a dict
member_benefits_get_success_response_links_dict = member_benefits_get_success_response_links_instance.to_dict()
# create an instance of MemberBenefitsGetSuccessResponseLinks from a dict
member_benefits_get_success_response_links_from_dict = MemberBenefitsGetSuccessResponseLinks.from_dict(member_benefits_get_success_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


