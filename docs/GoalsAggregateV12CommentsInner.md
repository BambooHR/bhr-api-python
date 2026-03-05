# GoalsAggregateV12CommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal_id** | **int** | The goalId that the comments are linked to. | [optional] 
**comment_count** | **int** | How many comments are linked to the goal | [optional] 

## Example

```python
from bamboohr_sdk.models.goals_aggregate_v12_comments_inner import GoalsAggregateV12CommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoalsAggregateV12CommentsInner from a JSON string
goals_aggregate_v12_comments_inner_instance = GoalsAggregateV12CommentsInner.from_json(json)
# print the JSON string representation of the object
print(GoalsAggregateV12CommentsInner.to_json())

# convert the object into a dict
goals_aggregate_v12_comments_inner_dict = goals_aggregate_v12_comments_inner_instance.to_dict()
# create an instance of GoalsAggregateV12CommentsInner from a dict
goals_aggregate_v12_comments_inner_from_dict = GoalsAggregateV12CommentsInner.from_dict(goals_aggregate_v12_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


