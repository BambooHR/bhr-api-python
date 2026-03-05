# PutGoalProgressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent_complete** | **int** | The percentage of completion for the goal (0-100) | 
**completion_date** | **date** | The date when the goal was completed in YYYY-MM-DD format. Required when percentComplete is 100. | [optional] 

## Example

```python
from bamboohr_sdk.models.put_goal_progress_request import PutGoalProgressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutGoalProgressRequest from a JSON string
put_goal_progress_request_instance = PutGoalProgressRequest.from_json(json)
# print the JSON string representation of the object
print(PutGoalProgressRequest.to_json())

# convert the object into a dict
put_goal_progress_request_dict = put_goal_progress_request_instance.to_dict()
# create an instance of PutGoalProgressRequest from a dict
put_goal_progress_request_from_dict = PutGoalProgressRequest.from_dict(put_goal_progress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


