# EmployeeCursorPaginationQueryObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **str** | Cursor pointing to the start of the previous page. Use the &#x60;prevCursor&#x60; value from the last response to paginate backward. | [optional] 
**after** | **str** | Cursor pointing to the start of the next page. Use the &#x60;nextCursor&#x60; value from the last response to paginate forward. | [optional] 
**limit** | **int** | Maximum number of items to return. This can be at most 2500. | [optional] [default to 250]

## Example

```python
from bamboohr_sdk.models.employee_cursor_pagination_query_object import EmployeeCursorPaginationQueryObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeCursorPaginationQueryObject from a JSON string
employee_cursor_pagination_query_object_instance = EmployeeCursorPaginationQueryObject.from_json(json)
# print the JSON string representation of the object
print(EmployeeCursorPaginationQueryObject.to_json())

# convert the object into a dict
employee_cursor_pagination_query_object_dict = employee_cursor_pagination_query_object_instance.to_dict()
# create an instance of EmployeeCursorPaginationQueryObject from a dict
employee_cursor_pagination_query_object_from_dict = EmployeeCursorPaginationQueryObject.from_dict(employee_cursor_pagination_query_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


