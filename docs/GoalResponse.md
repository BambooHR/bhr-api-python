# GoalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | [**TransformedApiGoal**](TransformedApiGoal.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_response import GoalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoalResponse from a JSON string
goal_response_instance = GoalResponse.from_json(json)
# print the JSON string representation of the object
print(GoalResponse.to_json())

# convert the object into a dict
goal_response_dict = goal_response_instance.to_dict()
# create an instance of GoalResponse from a dict
goal_response_from_dict = GoalResponse.from_dict(goal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


