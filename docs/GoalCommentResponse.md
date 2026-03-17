# GoalCommentResponse


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
from bamboohr_sdk.models.goal_comment_response import GoalCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoalCommentResponse from a JSON string
goal_comment_response_instance = GoalCommentResponse.from_json(json)
# print the JSON string representation of the object
print(GoalCommentResponse.to_json())

# convert the object into a dict
goal_comment_response_dict = goal_comment_response_instance.to_dict()
# create an instance of GoalCommentResponse from a dict
goal_comment_response_from_dict = GoalCommentResponse.from_dict(goal_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


