# GetEmployeesEmployeeResponseAllOfOvertimeRate

Employee's overtime rate. Only included when requested via the `fields` parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.get_employees_employee_response_all_of_overtime_rate import GetEmployeesEmployeeResponseAllOfOvertimeRate

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeesEmployeeResponseAllOfOvertimeRate from a JSON string
get_employees_employee_response_all_of_overtime_rate_instance = GetEmployeesEmployeeResponseAllOfOvertimeRate.from_json(json)
# print the JSON string representation of the object
print(GetEmployeesEmployeeResponseAllOfOvertimeRate.to_json())

# convert the object into a dict
get_employees_employee_response_all_of_overtime_rate_dict = get_employees_employee_response_all_of_overtime_rate_instance.to_dict()
# create an instance of GetEmployeesEmployeeResponseAllOfOvertimeRate from a dict
get_employees_employee_response_all_of_overtime_rate_from_dict = GetEmployeesEmployeeResponseAllOfOvertimeRate.from_dict(get_employees_employee_response_all_of_overtime_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


