# GetEmployeesEmployeeBaseResponse

Base employee fields that are always included in the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Unique identifier for the employee | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**preferred_name** | **str** |  | 
**photo_url** | **str** |  | 
**job_title_name** | **str** |  | 
**status** | **str** |  | 
**restricted_fields** | **List[str]** | Array of field names that are restricted due to permission checks | 

## Example

```python
from bamboohr_sdk.models.get_employees_employee_base_response import GetEmployeesEmployeeBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeesEmployeeBaseResponse from a JSON string
get_employees_employee_base_response_instance = GetEmployeesEmployeeBaseResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmployeesEmployeeBaseResponse.to_json())

# convert the object into a dict
get_employees_employee_base_response_dict = get_employees_employee_base_response_instance.to_dict()
# create an instance of GetEmployeesEmployeeBaseResponse from a dict
get_employees_employee_base_response_from_dict = GetEmployeesEmployeeBaseResponse.from_dict(get_employees_employee_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


