# GoalsAggregateV11


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_align** | **bool** | The selected user can align goals with other users. | [optional] 
**can_create_goals** | **bool** | The selected user can create a goal. | [optional] 
**filters** | [**GoalFiltersV11**](GoalFiltersV11.md) |  | [optional] 
**selected_filter** | **str** | The id of the current selected filter. | [optional] 
**goals** | [**List[TransformedApiGoal]**](TransformedApiGoal.md) | All goals in selected filter. | [optional] 
**persons** | [**List[GoalsAggregateV1PersonsInner]**](GoalsAggregateV1PersonsInner.md) | A list of people with access to the goal. | [optional] 
**comments** | [**List[GoalsAggregateV11CommentsInner]**](GoalsAggregateV11CommentsInner.md) | A list of how many comments belong to each goal. | [optional] 

## Example

```python
from bamboohr_sdk.models.goals_aggregate_v11 import GoalsAggregateV11

# TODO update the JSON string below
json = "{}"
# create an instance of GoalsAggregateV11 from a JSON string
goals_aggregate_v11_instance = GoalsAggregateV11.from_json(json)
# print the JSON string representation of the object
print(GoalsAggregateV11.to_json())

# convert the object into a dict
goals_aggregate_v11_dict = goals_aggregate_v11_instance.to_dict()
# create an instance of GoalsAggregateV11 from a dict
goals_aggregate_v11_from_dict = GoalsAggregateV11.from_dict(goals_aggregate_v11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


