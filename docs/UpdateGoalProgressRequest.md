# UpdateGoalProgressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent_complete** | **int** | The percentage of completion for the goal (0-100) | 
**completion_date** | **date** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_goal_progress_request import UpdateGoalProgressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalProgressRequest from a JSON string
update_goal_progress_request_instance = UpdateGoalProgressRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGoalProgressRequest.to_json())

# convert the object into a dict
update_goal_progress_request_dict = update_goal_progress_request_instance.to_dict()
# create an instance of UpdateGoalProgressRequest from a dict
update_goal_progress_request_from_dict = UpdateGoalProgressRequest.from_dict(update_goal_progress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


