# MemberBenefitEventMembersInnerCoveragesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | Plan ID | [optional] 
**events** | [**List[MemberBenefitEventMembersInnerCoveragesInnerEventsInner]**](MemberBenefitEventMembersInnerCoveragesInnerEventsInner.md) | Events | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefit_event_members_inner_coverages_inner import MemberBenefitEventMembersInnerCoveragesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitEventMembersInnerCoveragesInner from a JSON string
member_benefit_event_members_inner_coverages_inner_instance = MemberBenefitEventMembersInnerCoveragesInner.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitEventMembersInnerCoveragesInner.to_json())

# convert the object into a dict
member_benefit_event_members_inner_coverages_inner_dict = member_benefit_event_members_inner_coverages_inner_instance.to_dict()
# create an instance of MemberBenefitEventMembersInnerCoveragesInner from a dict
member_benefit_event_members_inner_coverages_inner_from_dict = MemberBenefitEventMembersInnerCoveragesInner.from_dict(member_benefit_event_members_inner_coverages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


