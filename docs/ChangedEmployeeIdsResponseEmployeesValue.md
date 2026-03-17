# ChangedEmployeeIdsResponseEmployeesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The employee ID. | [optional] 
**action** | **str** | The type of change: Inserted, Updated, or Deleted. | [optional] 
**last_changed** | **datetime** | ISO 8601 timestamp of the last change. | [optional] 

## Example

```python
from bamboohr_sdk.models.changed_employee_ids_response_employees_value import ChangedEmployeeIdsResponseEmployeesValue

# TODO update the JSON string below
json = "{}"
# create an instance of ChangedEmployeeIdsResponseEmployeesValue from a JSON string
changed_employee_ids_response_employees_value_instance = ChangedEmployeeIdsResponseEmployeesValue.from_json(json)
# print the JSON string representation of the object
print(ChangedEmployeeIdsResponseEmployeesValue.to_json())

# convert the object into a dict
changed_employee_ids_response_employees_value_dict = changed_employee_ids_response_employees_value_instance.to_dict()
# create an instance of ChangedEmployeeIdsResponseEmployeesValue from a dict
changed_employee_ids_response_employees_value_from_dict = ChangedEmployeeIdsResponseEmployeesValue.from_dict(changed_employee_ids_response_employees_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


