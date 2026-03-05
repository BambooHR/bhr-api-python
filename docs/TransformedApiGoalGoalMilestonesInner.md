# TransformedApiGoalGoalMilestonesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the milestone. | [optional] 
**employee_goal_id** | **int** | The id of the goal which encompasses this milestone. | [optional] 
**title** | **str** | The title of the milestone. | [optional] 
**current_value** | **float** | The current value for a numeric milestone. This number will be rounded to the nearest hundredth. On the creation of a numeric milestone this value will automatically be set to the start value of the milestone. If the milestone is a simple checkbox milestone, this value will always be null. | [optional] 
**start_value** | **float** | The starting value for a numeric milestone. This number will be rounded to the nearest hundredth. If the milestone is a simple checkbox milestone, this value will always be null. | [optional] 
**end_value** | **float** | The end goal for a numeric milestone. This number will be rounded to the nearest hundredth. If the milestone is a simple checkbox milestone, this value will always be null. | [optional] 
**completed_date_time** | **str** | The date and time in which the goal has been completed. If the goal is not completed the value will be null. | [optional] 
**last_update_date_date_time** | **str** | The date and time in which the goal was last updated. | [optional] 
**last_update_user_id** | **int** | The ID of the user who last updated this milestone. | [optional] 

## Example

```python
from bamboohr_sdk.models.transformed_api_goal_goal_milestones_inner import TransformedApiGoalGoalMilestonesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransformedApiGoalGoalMilestonesInner from a JSON string
transformed_api_goal_goal_milestones_inner_instance = TransformedApiGoalGoalMilestonesInner.from_json(json)
# print the JSON string representation of the object
print(TransformedApiGoalGoalMilestonesInner.to_json())

# convert the object into a dict
transformed_api_goal_goal_milestones_inner_dict = transformed_api_goal_goal_milestones_inner_instance.to_dict()
# create an instance of TransformedApiGoalGoalMilestonesInner from a dict
transformed_api_goal_goal_milestones_inner_from_dict = TransformedApiGoalGoalMilestonesInner.from_dict(transformed_api_goal_goal_milestones_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


