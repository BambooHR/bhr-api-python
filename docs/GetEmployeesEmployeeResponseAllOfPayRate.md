# GetEmployeesEmployeeResponseAllOfPayRate

Employee's pay rate. Only included when requested via the `fields` parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.get_employees_employee_response_all_of_pay_rate import GetEmployeesEmployeeResponseAllOfPayRate

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeesEmployeeResponseAllOfPayRate from a JSON string
get_employees_employee_response_all_of_pay_rate_instance = GetEmployeesEmployeeResponseAllOfPayRate.from_json(json)
# print the JSON string representation of the object
print(GetEmployeesEmployeeResponseAllOfPayRate.to_json())

# convert the object into a dict
get_employees_employee_response_all_of_pay_rate_dict = get_employees_employee_response_all_of_pay_rate_instance.to_dict()
# create an instance of GetEmployeesEmployeeResponseAllOfPayRate from a dict
get_employees_employee_response_all_of_pay_rate_from_dict = GetEmployeesEmployeeResponseAllOfPayRate.from_dict(get_employees_employee_response_all_of_pay_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


