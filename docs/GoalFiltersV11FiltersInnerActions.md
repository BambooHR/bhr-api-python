# GoalFiltersV11FiltersInnerActions

Available actions for goals in this state, defined by PerformanceDefinitions::GOAL_FILTER_ACTIONS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_close_goal** | **bool** | Whether goals in this state can be closed | [optional] 
**can_edit_goal** | **bool** | Whether goals in this state can be edited | [optional] 
**can_edit_goal_progress_bar** | **bool** | Whether progress bar can be edited for goals in this state | [optional] 
**can_reopen_goal** | **bool** | Whether goals in this state can be reopened | [optional] 
**can_share_goal** | **bool** | Whether goals in this state can be shared | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_filters_v11_filters_inner_actions import GoalFiltersV11FiltersInnerActions

# TODO update the JSON string below
json = "{}"
# create an instance of GoalFiltersV11FiltersInnerActions from a JSON string
goal_filters_v11_filters_inner_actions_instance = GoalFiltersV11FiltersInnerActions.from_json(json)
# print the JSON string representation of the object
print(GoalFiltersV11FiltersInnerActions.to_json())

# convert the object into a dict
goal_filters_v11_filters_inner_actions_dict = goal_filters_v11_filters_inner_actions_instance.to_dict()
# create an instance of GoalFiltersV11FiltersInnerActions from a dict
goal_filters_v11_filters_inner_actions_from_dict = GoalFiltersV11FiltersInnerActions.from_dict(goal_filters_v11_filters_inner_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


