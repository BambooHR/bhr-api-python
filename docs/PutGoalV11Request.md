# PutGoalV11Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the goal | 
**description** | **str** | A detailed description of the goal | [optional] 
**due_date** | **date** | The due date for the goal in YYYY-MM-DD format | 
**percent_complete** | **int** | The percentage of completion for the goal (0-100). Required when milestonesEnabled is not true. | [optional] 
**completion_date** | **date** | The date when the goal was completed in YYYY-MM-DD format. Required when percentComplete is 100. | [optional] 
**shared_with_employee_ids** | **List[int]** | List of employee IDs with whom the goal is shared. Must include the employee ID of the goal owner. | 
**aligns_with_option_id** | **int** | ID of the option this goal aligns with | [optional] 
**milestones_enabled** | **bool** | Flag indicating whether milestones are enabled for this goal | [optional] 
**deleted_milestone_ids** | **List[int]** | List of milestone IDs to be deleted from the goal | [optional] 
**milestones** | [**List[PutGoalV11RequestMilestonesInner]**](PutGoalV11RequestMilestonesInner.md) | List of milestones to add to this goal | [optional] 

## Example

```python
from bamboohr_sdk.models.put_goal_v11_request import PutGoalV11Request

# TODO update the JSON string below
json = "{}"
# create an instance of PutGoalV11Request from a JSON string
put_goal_v11_request_instance = PutGoalV11Request.from_json(json)
# print the JSON string representation of the object
print(PutGoalV11Request.to_json())

# convert the object into a dict
put_goal_v11_request_dict = put_goal_v11_request_instance.to_dict()
# create an instance of PutGoalV11Request from a dict
put_goal_v11_request_from_dict = PutGoalV11Request.from_dict(put_goal_v11_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


