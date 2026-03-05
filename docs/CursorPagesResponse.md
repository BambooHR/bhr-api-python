# CursorPagesResponse

Pagination information for employee list responses including limit and cursor-based navigation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of items per page | 
**next_cursor** | **str** | Cursor for the next page of results, null if no more pages. This should be used with the after pagination parameter. | 
**prev_cursor** | **str** | Cursor for the previous page of results, null if on first page. This should be used with the before pagination parameter. | 

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


