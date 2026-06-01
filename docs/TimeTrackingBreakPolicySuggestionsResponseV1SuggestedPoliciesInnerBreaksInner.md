# TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**duration** | **int** |  | 
**paid** | **bool** |  | 
**availability_type** | **str** |  | 
**availability_min_hours_worked** | **float** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_breaks_inner import TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner from a JSON string
time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_breaks_inner_instance = TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner.to_json())

# convert the object into a dict
time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_breaks_inner_dict = time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_breaks_inner_instance.to_dict()
# create an instance of TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner from a dict
time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_breaks_inner_from_dict = TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner.from_dict(time_tracking_break_policy_suggestions_response_v1_suggested_policies_inner_breaks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


