# TransformedApiGoal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the goal. | [optional] 
**title** | **str** | Title of the goal. | [optional] 
**description** | **str** | A description of the goal. | [optional] 
**percent_complete** | **int** | A percentage (0-100) that denotes how complete the goal is. | [optional] 
**aligns_with_option_id** | **str** | The ID of the goal this goal is aligned with. Returns null when not aligned, or an empty string when the goal has no parent set. | [optional] 
**shared_with_employee_ids** | **List[int]** | Ids of the employees that have access to this goal. | [optional] 
**due_date** | **str** | The due date of the goal. | [optional] 
**completion_date** | **str** | The date the goal was completed. | [optional] 
**last_changed_date_time** | **str** | ISO 8601 UTC timestamp of when the goal was last modified. | [optional] 
**status** | **str** | The status of the goal. | [optional] 
**milestones** | [**List[TransformedApiGoalMilestonesInner]**](TransformedApiGoalMilestonesInner.md) | All milestones for the individual goal. This array will not exist if milestones are not selected for this goal. | [optional] 
**actions** | [**TransformedApiGoalActions**](TransformedApiGoalActions.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.transformed_api_goal import TransformedApiGoal

# TODO update the JSON string below
json = "{}"
# create an instance of TransformedApiGoal from a JSON string
transformed_api_goal_instance = TransformedApiGoal.from_json(json)
# print the JSON string representation of the object
print(TransformedApiGoal.to_json())

# convert the object into a dict
transformed_api_goal_dict = transformed_api_goal_instance.to_dict()
# create an instance of TransformedApiGoal from a dict
transformed_api_goal_from_dict = TransformedApiGoal.from_dict(transformed_api_goal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


