# EmployeeTableRow

A single row from the requested table. The returned fields depend on the table and the caller's field-level permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The table row ID. | [optional] 
**employee_id** | **str** | The employee ID that owns this row. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_table_row import EmployeeTableRow

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTableRow from a JSON string
employee_table_row_instance = EmployeeTableRow.from_json(json)
# print the JSON string representation of the object
print(EmployeeTableRow.to_json())

# convert the object into a dict
employee_table_row_dict = employee_table_row_instance.to_dict()
# create an instance of EmployeeTableRow from a dict
employee_table_row_from_dict = EmployeeTableRow.from_dict(employee_table_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


