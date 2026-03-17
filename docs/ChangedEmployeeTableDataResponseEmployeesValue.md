# ChangedEmployeeTableDataResponseEmployeesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_changed** | **datetime** | ISO 8601 timestamp of the last change for this employee. | [optional] 
**rows** | **List[Dict[str, ChangedEmployeeTableDataResponseEmployeesValueRowsInnerValue]]** | The table rows for this employee. | [optional] 

## Example

```python
from bamboohr_sdk.models.changed_employee_table_data_response_employees_value import ChangedEmployeeTableDataResponseEmployeesValue

# TODO update the JSON string below
json = "{}"
# create an instance of ChangedEmployeeTableDataResponseEmployeesValue from a JSON string
changed_employee_table_data_response_employees_value_instance = ChangedEmployeeTableDataResponseEmployeesValue.from_json(json)
# print the JSON string representation of the object
print(ChangedEmployeeTableDataResponseEmployeesValue.to_json())

# convert the object into a dict
changed_employee_table_data_response_employees_value_dict = changed_employee_table_data_response_employees_value_instance.to_dict()
# create an instance of ChangedEmployeeTableDataResponseEmployeesValue from a dict
changed_employee_table_data_response_employees_value_from_dict = ChangedEmployeeTableDataResponseEmployeesValue.from_dict(changed_employee_table_data_response_employees_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


