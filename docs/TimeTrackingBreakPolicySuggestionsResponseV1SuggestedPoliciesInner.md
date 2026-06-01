# TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**breaks** | [**List[TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner]**](TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner.md) |  | 

## Example

```python
from bamboohr_sdk.models.time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner import TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner from a JSON string
time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_instance = TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner.to_json())

# convert the object into a dict
time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_dict = time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_instance.to_dict()
# create an instance of TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner from a dict
time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_from_dict = TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner.from_dict(time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


