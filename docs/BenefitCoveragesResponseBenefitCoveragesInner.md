# BenefitCoveragesResponseBenefitCoveragesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The coverage level ID. | [optional] 
**short_name** | **str** | The short display name for this coverage level (e.g. \&quot;Employee + Spouse\&quot;). | [optional] 
**description** | **str** | An optional longer description of the coverage level. Null if not set. | [optional] 
**sort_order** | **str** | The sort order used when displaying coverage levels. | [optional] 
**benefit_plan_id** | **str** | The benefit plan this coverage level belongs to, or null for company-wide coverage levels. | [optional] 

## Example

```python
from bamboohr_sdk.models.benefit_coverages_response_benefit_coverages_inner import BenefitCoveragesResponseBenefitCoveragesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitCoveragesResponseBenefitCoveragesInner from a JSON string
benefit_coverages_response_benefit_coverages_inner_instance = BenefitCoveragesResponseBenefitCoveragesInner.from_json(json)
# print the JSON string representation of the object
print(BenefitCoveragesResponseBenefitCoveragesInner.to_json())

# convert the object into a dict
benefit_coverages_response_benefit_coverages_inner_dict = benefit_coverages_response_benefit_coverages_inner_instance.to_dict()
# create an instance of BenefitCoveragesResponseBenefitCoveragesInner from a dict
benefit_coverages_response_benefit_coverages_inner_from_dict = BenefitCoveragesResponseBenefitCoveragesInner.from_dict(benefit_coverages_response_benefit_coverages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


