# MemberBenefitEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[MemberBenefitEvent]**](MemberBenefitEvent.md) | List of member benefit event records, one entry per employee or dependent. | [optional] 

## Example

```python
from bamboohr_sdk.models.member_benefit_events_response import MemberBenefitEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBenefitEventsResponse from a JSON string
member_benefit_events_response_instance = MemberBenefitEventsResponse.from_json(json)
# print the JSON string representation of the object
print(MemberBenefitEventsResponse.to_json())

# convert the object into a dict
member_benefit_events_response_dict = member_benefit_events_response_instance.to_dict()
# create an instance of MemberBenefitEventsResponse from a dict
member_benefit_events_response_from_dict = MemberBenefitEventsResponse.from_dict(member_benefit_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


