# GoalAggregatePersonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | The id of this employee. | [optional] 
**user_id** | **int** | The user id of the person if applicable. | [optional] 
**display_first_name** | **str** | First name of the person. | [optional] 
**last_name** | **str** | Last name of the person. | [optional] 
**photo_url** | **str** | url of the user profile image. | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_aggregate_persons_inner import GoalAggregatePersonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoalAggregatePersonsInner from a JSON string
goal_aggregate_persons_inner_instance = GoalAggregatePersonsInner.from_json(json)
# print the JSON string representation of the object
print(GoalAggregatePersonsInner.to_json())

# convert the object into a dict
goal_aggregate_persons_inner_dict = goal_aggregate_persons_inner_instance.to_dict()
# create an instance of GoalAggregatePersonsInner from a dict
goal_aggregate_persons_inner_from_dict = GoalAggregatePersonsInner.from_dict(goal_aggregate_persons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


