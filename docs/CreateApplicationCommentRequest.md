# CreateApplicationCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The comment type. Defaults to &#x60;comment&#x60; if omitted. | [optional] 
**comment** | **str** | The comment being posted. | 

## Example

```python
from bamboohr_sdk.models.create_application_comment_request import CreateApplicationCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationCommentRequest from a JSON string
create_application_comment_request_instance = CreateApplicationCommentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationCommentRequest.to_json())

# convert the object into a dict
create_application_comment_request_dict = create_application_comment_request_instance.to_dict()
# create an instance of CreateApplicationCommentRequest from a dict
create_application_comment_request_from_dict = CreateApplicationCommentRequest.from_dict(create_application_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


