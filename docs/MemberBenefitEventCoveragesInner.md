# MemberBenefitEventCoveragesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | The ID of the benefit plan. | [optional] 
**events** | [**List[MemberBenefitEventCoveragesInnerEventsInner]**](MemberBenefitEventCoveragesInnerEventsInner.md) | Chronological list of benefit events for this member and plan, covering the past year. Event type &#39;enrollment&#39; includes premiumTierId and monthlyPremiumInCents; &#39;eligibility&#39; and &#39;loss&#39; events include only effectiveDate and type. | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefit_event_coverages_inner import MemberBenefitEventCoveragesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitEventCoveragesInner from a JSON string
member_benefit_event_coverages_inner_instance = MemberBenefitEventCoveragesInner.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitEventCoveragesInner.to_json())

# convert the object into a dict
member_benefit_event_coverages_inner_dict = member_benefit_event_coverages_inner_instance.to_dict()
# create an instance of MemberBenefitEventCoveragesInner from a dict
member_benefit_event_coverages_inner_from_dict = MemberBenefitEventCoveragesInner.from_dict(member_benefit_event_coverages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


