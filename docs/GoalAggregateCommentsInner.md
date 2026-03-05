# GoalAggregateCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the comment. | [optional] 
**author_user_id** | **int** | Id of the author of the comment. | [optional] 
**created_at** | **str** | The date and time that the comment was created. | [optional] 
**text** | **str** | The actual text of the comment. | [optional] 
**can_edit** | **bool** | Can the comment be edited. | [optional] 
**can_delete** | **bool** | Can the comment be deleted. | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_aggregate_comments_inner import GoalAggregateCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoalAggregateCommentsInner from a JSON string
goal_aggregate_comments_inner_instance = GoalAggregateCommentsInner.from_json(json)
# print the JSON string representation of the object
print(GoalAggregateCommentsInner.to_json())

# convert the object into a dict
goal_aggregate_comments_inner_dict = goal_aggregate_comments_inner_instance.to_dict()
# create an instance of GoalAggregateCommentsInner from a dict
goal_aggregate_comments_inner_from_dict = GoalAggregateCommentsInner.from_dict(goal_aggregate_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


