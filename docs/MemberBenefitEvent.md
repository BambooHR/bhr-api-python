# MemberBenefitEvent

A single member (employee or dependent) and their benefit coverage events across all enrolled plans.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The unique identifier of the member. Format: &#39;employee.{id}&#39; for employees, &#39;dependent.{id}&#39; for dependents. | [optional] 
**coverages** | [**List[MemberBenefitEventCoveragesInner]**](MemberBenefitEventCoveragesInner.md) | The benefit plan coverages for this member, one entry per plan. | [optional] 

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


