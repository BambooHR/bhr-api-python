# CursorPagesResponse

Pagination information for employee list responses including limit and cursor-based navigation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**next_cursor** | **str** |  | 
**prev_cursor** | **str** |  | 

## Example

```python
from bamboohr_sdk.models.cursor_pages_response import CursorPagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPagesResponse from a JSON string
cursor_pages_response_instance = CursorPagesResponse.from_json(json)
# print the JSON string representation of the object
print(CursorPagesResponse.to_json())

# convert the object into a dict
cursor_pages_response_dict = cursor_pages_response_instance.to_dict()
# create an instance of CursorPagesResponse from a dict
cursor_pages_response_from_dict = CursorPagesResponse.from_dict(cursor_pages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


