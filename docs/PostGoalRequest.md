# PostGoalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the goal | 
**description** | **str** | A detailed description of the goal | [optional] 
**due_date** | **date** | The due date for the goal in YYYY-MM-DD format | 
**percent_complete** | **int** | The percentage of completion for the goal (0-100) | 
**completion_date** | **date** | The date when the goal was completed in YYYY-MM-DD format. Required when percentComplete is 100. | [optional] 
**shared_with_employee_ids** | **List[int]** | List of employee IDs with whom the goal is shared. Must include the employee ID of the goal owner. | 
**aligns_with_option_id** | **int** | ID of the option this goal aligns with | [optional] 
**milestones** | [**List[PostGoalRequestMilestonesInner]**](PostGoalRequestMilestonesInner.md) | List of milestones for this goal | [optional] 

## Example

```python
from bamboohr_sdk.models.post_goal_request import PostGoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGoalRequest from a JSON string
post_goal_request_instance = PostGoalRequest.from_json(json)
# print the JSON string representation of the object
print(PostGoalRequest.to_json())

# convert the object into a dict
post_goal_request_dict = post_goal_request_instance.to_dict()
# create an instance of PostGoalRequest from a dict
post_goal_request_from_dict = PostGoalRequest.from_dict(post_goal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


