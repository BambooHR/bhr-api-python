# TransformedApiGoalGoalActions

Actions that are available to a goal with milestones enabled. This object will not appear on a goal without milestones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_edit_goal_progress_bar** | **bool** | Can the user edit the progress bar of this goal. | [optional] 
**can_edit_goal_milestone_progress_bar** | **bool** | can the user edit the progress of a milestone in this goal. | [optional] 

## Example

```python
from bamboohr_sdk.models.transformed_api_goal_goal_actions import TransformedApiGoalGoalActions

# TODO update the JSON string below
json = "{}"
# create an instance of TransformedApiGoalGoalActions from a JSON string
transformed_api_goal_goal_actions_instance = TransformedApiGoalGoalActions.from_json(json)
# print the JSON string representation of the object
print(TransformedApiGoalGoalActions.to_json())

# convert the object into a dict
transformed_api_goal_goal_actions_dict = transformed_api_goal_goal_actions_instance.to_dict()
# create an instance of TransformedApiGoalGoalActions from a dict
transformed_api_goal_goal_actions_from_dict = TransformedApiGoalGoalActions.from_dict(transformed_api_goal_goal_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


