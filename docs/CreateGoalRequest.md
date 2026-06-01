# CreateGoalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the goal | 
**description** | **str** | A detailed description of the goal | [optional] 
**due_date** | **date** | The due date for the goal in YYYY-MM-DD format | 
**percent_complete** | **int** | Initial percentage of completion for a simple goal (0-100). Defaults to 0 if omitted. Ignored when &#x60;milestones&#x60; is provided; milestone-based goals derive percent complete from milestone completion and should be updated via &#x60;update-goal-milestone-progress&#x60;. | [optional] 
**completion_date** | **date** |  | [optional] 
**shared_with_employee_ids** | **List[Optional[int]]** | List of employee IDs with whom the goal is shared. Must include the employee ID of the goal owner. | 
**aligns_with_option_id** | **int** |  | [optional] 
**milestones** | [**List[CreateGoalRequestMilestonesInner]**](CreateGoalRequestMilestonesInner.md) | Optional. Provide a non-empty array of milestone objects to create a milestone-based goal. Omit this field (or send &#x60;null&#x60;) to create a simple goal. | [optional] 

## Example

```python
from bamboohr_sdk.models.create_goal_request import CreateGoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGoalRequest from a JSON string
create_goal_request_instance = CreateGoalRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGoalRequest.to_json())

# convert the object into a dict
create_goal_request_dict = create_goal_request_instance.to_dict()
# create an instance of CreateGoalRequest from a dict
create_goal_request_from_dict = CreateGoalRequest.from_dict(create_goal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


