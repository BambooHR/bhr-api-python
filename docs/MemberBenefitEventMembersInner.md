# MemberBenefitEventMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | Member ID | [optional] 
**coverages** | [**List[MemberBenefitEventMembersInnerCoveragesInner]**](MemberBenefitEventMembersInnerCoveragesInner.md) | Coverages | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefit_event_members_inner import MemberBenefitEventMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitEventMembersInner from a JSON string
member_benefit_event_members_inner_instance = MemberBenefitEventMembersInner.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitEventMembersInner.to_json())

# convert the object into a dict
member_benefit_event_members_inner_dict = member_benefit_event_members_inner_instance.to_dict()
# create an instance of MemberBenefitEventMembersInner from a dict
member_benefit_event_members_inner_from_dict = MemberBenefitEventMembersInner.from_dict(member_benefit_event_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


