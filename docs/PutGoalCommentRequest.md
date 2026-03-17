# PutGoalCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The updated text content of the comment. | 

## Example

```python
from bamboohr_sdk.models.put_goal_comment_request import PutGoalCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutGoalCommentRequest from a JSON string
put_goal_comment_request_instance = PutGoalCommentRequest.from_json(json)
# print the JSON string representation of the object
print(PutGoalCommentRequest.to_json())

# convert the object into a dict
put_goal_comment_request_dict = put_goal_comment_request_instance.to_dict()
# create an instance of PutGoalCommentRequest from a dict
put_goal_comment_request_from_dict = PutGoalCommentRequest.from_dict(put_goal_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


