# CloseGoalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.close_goal_request import CloseGoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseGoalRequest from a JSON string
close_goal_request_instance = CloseGoalRequest.from_json(json)
# print the JSON string representation of the object
print(CloseGoalRequest.to_json())

# convert the object into a dict
close_goal_request_dict = close_goal_request_instance.to_dict()
# create an instance of CloseGoalRequest from a dict
close_goal_request_from_dict = CloseGoalRequest.from_dict(close_goal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


