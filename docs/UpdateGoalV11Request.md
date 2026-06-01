# UpdateGoalV11Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the goal | 
**description** | **str** | A detailed description of the goal | [optional] 
**due_date** | **date** | The due date for the goal in YYYY-MM-DD format | 
**percent_complete** | **int** | The percentage of completion for the goal (0-100). Defaults to 0 if omitted. Ignored when milestonesEnabled is true. | [optional] 
**completion_date** | **date** |  | [optional] 
**shared_with_employee_ids** | **List[Optional[int]]** | List of employee IDs with whom the goal is shared. Must include the employee ID of the goal owner. | 
**aligns_with_option_id** | **int** |  | [optional] 
**milestones_enabled** | **bool** | Flag indicating whether milestones are enabled for this goal | [optional] 
**deleted_milestone_ids** | **List[Optional[int]]** | List of milestone IDs to be deleted from the goal | [optional] 
**milestones** | [**List[UpdateGoalV11RequestMilestonesInner]**](UpdateGoalV11RequestMilestonesInner.md) | Optional. New milestones to add to the goal. Each object in this array creates a new milestone — even if its title matches an existing milestone. Do not include existing milestones here unless you intentionally want duplicates. To remove milestones, use &#x60;deletedMilestoneIds&#x60;. | [optional] 

## Example

```python
from bamboohr_sdk.models.update_goal_v11_request import UpdateGoalV11Request

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalV11Request from a JSON string
update_goal_v11_request_instance = UpdateGoalV11Request.from_json(json)
# print the JSON string representation of the object
print(UpdateGoalV11Request.to_json())

# convert the object into a dict
update_goal_v11_request_dict = update_goal_v11_request_instance.to_dict()
# create an instance of UpdateGoalV11Request from a dict
update_goal_v11_request_from_dict = UpdateGoalV11Request.from_dict(update_goal_v11_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


