# ChangedEmployeeTableDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | The requested table name. | 
**employees** | [**Dict[str, ChangedEmployeeTableDataResponseEmployeesValue]**](ChangedEmployeeTableDataResponseEmployeesValue.md) | Map of employee IDs to changed table data for that employee. | 

## Example

```python
from bamboohr_sdk.models.changed_employee_table_data_response import ChangedEmployeeTableDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangedEmployeeTableDataResponse from a JSON string
changed_employee_table_data_response_instance = ChangedEmployeeTableDataResponse.from_json(json)
# print the JSON string representation of the object
print(ChangedEmployeeTableDataResponse.to_json())

# convert the object into a dict
changed_employee_table_data_response_dict = changed_employee_table_data_response_instance.to_dict()
# create an instance of ChangedEmployeeTableDataResponse from a dict
changed_employee_table_data_response_from_dict = ChangedEmployeeTableDataResponse.from_dict(changed_employee_table_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


