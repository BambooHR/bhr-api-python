# GoalAggregate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | [**TransformedApiGoal**](TransformedApiGoal.md) |  | [optional] 
**can_align** | **bool** | The selected user can align goals with other users. | [optional] 
**can_create_goals** | **bool** | The selected user can create a goal. | [optional] 
**aligns_with_options** | [**List[GoalAggregateAlignsWithOptionsInner]**](GoalAggregateAlignsWithOptionsInner.md) | All possible goals that this goal could be aligned with. | [optional] 
**comments** | [**List[GoalAggregateCommentsInner]**](GoalAggregateCommentsInner.md) | Comments linked to selected goal. | [optional] 
**persons** | [**List[GoalAggregatePersonsInner]**](GoalAggregatePersonsInner.md) | A list of people with access to the goal. | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_aggregate import GoalAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of GoalAggregate from a JSON string
goal_aggregate_instance = GoalAggregate.from_json(json)
# print the JSON string representation of the object
print(GoalAggregate.to_json())

# convert the object into a dict
goal_aggregate_dict = goal_aggregate_instance.to_dict()
# create an instance of GoalAggregate from a dict
goal_aggregate_from_dict = GoalAggregate.from_dict(goal_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


