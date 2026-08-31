# CreateGoalCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text content of the comment. | 

## Example

```python
from bamboohr_sdk.models.create_goal_comment_request import CreateGoalCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGoalCommentRequest from a JSON string
create_goal_comment_request_instance = CreateGoalCommentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGoalCommentRequest.to_json())

# convert the object into a dict
create_goal_comment_request_dict = create_goal_comment_request_instance.to_dict()
# create an instance of CreateGoalCommentRequest from a dict
create_goal_comment_request_from_dict = CreateGoalCommentRequest.from_dict(create_goal_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


