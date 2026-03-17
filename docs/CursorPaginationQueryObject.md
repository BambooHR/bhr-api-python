# CursorPaginationQueryObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **str** | Cursor pointing to the start of the previous page. Use the &#x60;prevCursor&#x60; value from the last response to paginate backward. | [optional] 
**after** | **str** | Cursor pointing to the start of the next page. Use the &#x60;nextCursor&#x60; value from the last response to paginate forward. | [optional] 
**limit** | **int** | Maximum number of items to return. This can be at most 100. | [optional] [default to 50]

## Example

```python
from bamboohr_sdk.models.cursor_pagination_query_object import CursorPaginationQueryObject

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaginationQueryObject from a JSON string
cursor_pagination_query_object_instance = CursorPaginationQueryObject.from_json(json)
# print the JSON string representation of the object
print(CursorPaginationQueryObject.to_json())

# convert the object into a dict
cursor_pagination_query_object_dict = cursor_pagination_query_object_instance.to_dict()
# create an instance of CursorPaginationQueryObject from a dict
cursor_pagination_query_object_from_dict = CursorPaginationQueryObject.from_dict(cursor_pagination_query_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


