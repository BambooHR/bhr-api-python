# MemberBenefitEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[MemberBenefitEventMembersInner]**](MemberBenefitEventMembersInner.md) | Members | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefit_event import MemberBenefitEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitEvent from a JSON string
member_benefit_event_instance = MemberBenefitEvent.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitEvent.to_json())

# convert the object into a dict
member_benefit_event_dict = member_benefit_event_instance.to_dict()
# create an instance of MemberBenefitEvent from a dict
member_benefit_event_from_dict = MemberBenefitEvent.from_dict(member_benefit_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


