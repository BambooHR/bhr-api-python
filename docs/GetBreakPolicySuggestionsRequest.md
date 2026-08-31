# GetBreakPolicySuggestionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | The user&#39;s request or question for break policy suggestions (e.g. \&quot;What policies do we need for our California employees?\&quot;) | 

## Example

```python
from bamboohr_sdk.models.get_break_policy_suggestions_request import GetBreakPolicySuggestionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBreakPolicySuggestionsRequest from a JSON string
get_break_policy_suggestions_request_instance = GetBreakPolicySuggestionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetBreakPolicySuggestionsRequest.to_json())

# convert the object into a dict
get_break_policy_suggestions_request_dict = get_break_policy_suggestions_request_instance.to_dict()
# create an instance of GetBreakPolicySuggestionsRequest from a dict
get_break_policy_suggestions_request_from_dict = GetBreakPolicySuggestionsRequest.from_dict(get_break_policy_suggestions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


