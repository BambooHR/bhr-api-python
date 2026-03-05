# GoalsAggregateV12


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_align** | **bool** | The selected user can align goals with other users. | [optional] 
**can_create_goals** | **bool** | The selected user can create a goal. | [optional] 
**filters** | [**GoalFiltersV11**](GoalFiltersV11.md) |  | [optional] 
**selected_filter** | **str** | The id of the current selected filter. | [optional] 
**goals** | [**List[TransformedApiGoal]**](TransformedApiGoal.md) | All goals in selected filter. | [optional] 
**persons** | [**List[GoalAggregatePersonsInner]**](GoalAggregatePersonsInner.md) | A list of people with access to the goal. | [optional] 
**comments** | [**List[GoalsAggregateV12CommentsInner]**](GoalsAggregateV12CommentsInner.md) | A list of how many comments belong to each goal. | [optional] 

## Example

```python
from bamboohr_sdk.models.goals_aggregate_v12 import GoalsAggregateV12

# TODO update the JSON string below
json = "{}"
# create an instance of GoalsAggregateV12 from a JSON string
goals_aggregate_v12_instance = GoalsAggregateV12.from_json(json)
# print the JSON string representation of the object
print(GoalsAggregateV12.to_json())

# convert the object into a dict
goals_aggregate_v12_dict = goals_aggregate_v12_instance.to_dict()
# create an instance of GoalsAggregateV12 from a dict
goals_aggregate_v12_from_dict = GoalsAggregateV12.from_dict(goals_aggregate_v12_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


