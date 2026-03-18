# GoalCommentsResponseCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The comment ID. | [optional] 
**author_user_id** | **int** | The user ID of the comment author. | [optional] 
**created_at** | **str** | ISO 8601 UTC timestamp when the comment was created. | [optional] 
**text** | **str** | The text content of the comment. | [optional] 
**can_edit** | **bool** | Whether the API user can edit this comment. | [optional] 
**can_delete** | **bool** | Whether the API user can delete this comment. | [optional] 

## Example

```python
from bamboohr_sdk.models.goal_comments_response_comments_inner import GoalCommentsResponseCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoalCommentsResponseCommentsInner from a JSON string
goal_comments_response_comments_inner_instance = GoalCommentsResponseCommentsInner.from_json(json)
# print the JSON string representation of the object
print(GoalCommentsResponseCommentsInner.to_json())

# convert the object into a dict
goal_comments_response_comments_inner_dict = goal_comments_response_comments_inner_instance.to_dict()
# create an instance of GoalCommentsResponseCommentsInner from a dict
goal_comments_response_comments_inner_from_dict = GoalCommentsResponseCommentsInner.from_dict(goal_comments_response_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


