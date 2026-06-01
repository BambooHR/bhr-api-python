# TimeTrackingBreakPolicySuggestionsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_policies** | [**List[TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner]**](TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_break_policy_suggestions_response_v1 import TimeTrackingBreakPolicySuggestionsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingBreakPolicySuggestionsResponseV1 from a JSON string
time_tracking_break_policy_suggestions_response_v1_instance = TimeTrackingBreakPolicySuggestionsResponseV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingBreakPolicySuggestionsResponseV1.to_json())

# convert the object into a dict
time_tracking_break_policy_suggestions_response_v1_dict = time_tracking_break_policy_suggestions_response_v1_instance.to_dict()
# create an instance of TimeTrackingBreakPolicySuggestionsResponseV1 from a dict
time_tracking_break_policy_suggestions_response_v1_from_dict = TimeTrackingBreakPolicySuggestionsResponseV1.from_dict(time_tracking_break_policy_suggestions_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


