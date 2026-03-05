# GoalsAggregateV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_align** | **bool** | The selected user can align goals with other users. | [optional] 
**can_create_goals** | **bool** | The selected user can create a goal. | [optional] 
**filters** | [**GoalFiltersV1**](GoalFiltersV1.md) |  | [optional] 
**selected_filter** | **str** | The id of the current selected filter. | [optional] 
**goals** | [**List[TransformedApiGoal]**](TransformedApiGoal.md) | All goals in selected filter. | [optional] 
**persons** | [**List[GoalsAggregateV1PersonsInner]**](GoalsAggregateV1PersonsInner.md) | A list of people with access to the goal. | [optional] 
**comments** | [**List[GoalsAggregateV1CommentsInner]**](GoalsAggregateV1CommentsInner.md) | A list of how many comments belong to each goal. | [optional] 

## Example

```python
from bamboohr_sdk.models.goals_aggregate_v1 import GoalsAggregateV1

# TODO update the JSON string below
json = "{}"
# create an instance of GoalsAggregateV1 from a JSON string
goals_aggregate_v1_instance = GoalsAggregateV1.from_json(json)
# print the JSON string representation of the object
print(GoalsAggregateV1.to_json())

# convert the object into a dict
goals_aggregate_v1_dict = goals_aggregate_v1_instance.to_dict()
# create an instance of GoalsAggregateV1 from a dict
goals_aggregate_v1_from_dict = GoalsAggregateV1.from_dict(goals_aggregate_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


