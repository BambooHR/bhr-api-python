# PostApplicationCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Always the value \&quot;comment\&quot;. | 
**comment** | **str** | The comment being posted. | 

## Example

```python
from bamboohr_sdk.models.post_application_comment_request import PostApplicationCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApplicationCommentRequest from a JSON string
post_application_comment_request_instance = PostApplicationCommentRequest.from_json(json)
# print the JSON string representation of the object
print(PostApplicationCommentRequest.to_json())

# convert the object into a dict
post_application_comment_request_dict = post_application_comment_request_instance.to_dict()
# create an instance of PostApplicationCommentRequest from a dict
post_application_comment_request_from_dict = PostApplicationCommentRequest.from_dict(post_application_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


