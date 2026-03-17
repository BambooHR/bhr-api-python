# MemberBenefitEventCoveragesInnerEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **date** | The date this event takes effect (YYYY-MM-DD). | [optional] 
**type** | **str** | The type of benefit event. | [optional] 
**premium_tier_id** | **str** | The premium tier ID for enrollment events. Only present on events with type &#39;enrollment&#39;. | [optional] 
**monthly_premium_in_cents** | **int** | The monthly premium amount in cents for enrollment events. Only present on events with type &#39;enrollment&#39;. | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefit_event_coverages_inner_events_inner import MemberBenefitEventCoveragesInnerEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitEventCoveragesInnerEventsInner from a JSON string
member_benefit_event_coverages_inner_events_inner_instance = MemberBenefitEventCoveragesInnerEventsInner.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitEventCoveragesInnerEventsInner.to_json())

# convert the object into a dict
member_benefit_event_coverages_inner_events_inner_dict = member_benefit_event_coverages_inner_events_inner_instance.to_dict()
# create an instance of MemberBenefitEventCoveragesInnerEventsInner from a dict
member_benefit_event_coverages_inner_events_inner_from_dict = MemberBenefitEventCoveragesInnerEventsInner.from_dict(member_benefit_event_coverages_inner_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


