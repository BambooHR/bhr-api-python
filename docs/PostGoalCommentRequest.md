# PostGoalCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text content of the comment. | 

## Example

```python
from bamboohr_sdk.models.post_goal_comment_request import PostGoalCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGoalCommentRequest from a JSON string
post_goal_comment_request_instance = PostGoalCommentRequest.from_json(json)
# print the JSON string representation of the object
print(PostGoalCommentRequest.to_json())

# convert the object into a dict
post_goal_comment_request_dict = post_goal_comment_request_instance.to_dict()
# create an instance of PostGoalCommentRequest from a dict
post_goal_comment_request_from_dict = PostGoalCommentRequest.from_dict(post_goal_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


