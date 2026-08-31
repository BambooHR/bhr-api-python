# UpdateGoalCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The updated text content of the comment. | 

## Example

```python
from bamboohr_sdk.models.update_goal_comment_request import UpdateGoalCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalCommentRequest from a JSON string
update_goal_comment_request_instance = UpdateGoalCommentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGoalCommentRequest.to_json())

# convert the object into a dict
update_goal_comment_request_dict = update_goal_comment_request_instance.to_dict()
# create an instance of UpdateGoalCommentRequest from a dict
update_goal_comment_request_from_dict = UpdateGoalCommentRequest.from_dict(update_goal_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


