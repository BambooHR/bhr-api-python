# GetGoalsAlignmentOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal_id** | **int** | The goal ID to get alignment options for | [optional] 

## Example

```python
from bamboohr_sdk.models.get_goals_alignment_options_request import GetGoalsAlignmentOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetGoalsAlignmentOptionsRequest from a JSON string
get_goals_alignment_options_request_instance = GetGoalsAlignmentOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetGoalsAlignmentOptionsRequest.to_json())

# convert the object into a dict
get_goals_alignment_options_request_dict = get_goals_alignment_options_request_instance.to_dict()
# create an instance of GetGoalsAlignmentOptionsRequest from a dict
get_goals_alignment_options_request_from_dict = GetGoalsAlignmentOptionsRequest.from_dict(get_goals_alignment_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


