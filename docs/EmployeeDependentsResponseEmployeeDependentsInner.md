# EmployeeDependentsResponseEmployeeDependentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the dependent record. | [optional] 
**employee_id** | **str** | The ID of the employee this dependent belongs to. | [optional] 
**first_name** | **str** | The dependent&#39;s first name. | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** | The dependent&#39;s last name. | [optional] 
**relationship** | **str** | The dependent&#39;s relationship to the employee. | [optional] 
**gender** | **str** | The dependent&#39;s gender. | [optional] 
**masked_ssn** | **str** |  | [optional] 
**masked_sin** | **str** |  | [optional] 
**date_of_birth** | **date** | The dependent&#39;s date of birth in YYYY-MM-DD format. | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**home_phone** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**is_us_citizen** | **str** |  | [optional] 
**is_student** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_dependents_response_employee_dependents_inner import EmployeeDependentsResponseEmployeeDependentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeDependentsResponseEmployeeDependentsInner from a JSON string
employee_dependents_response_employee_dependents_inner_instance = EmployeeDependentsResponseEmployeeDependentsInner.from_json(json)
# print the JSON string representation of the object
print(EmployeeDependentsResponseEmployeeDependentsInner.to_json())

# convert the object into a dict
employee_dependents_response_employee_dependents_inner_dict = employee_dependents_response_employee_dependents_inner_instance.to_dict()
# create an instance of EmployeeDependentsResponseEmployeeDependentsInner from a dict
employee_dependents_response_employee_dependents_inner_from_dict = EmployeeDependentsResponseEmployeeDependentsInner.from_dict(employee_dependents_response_employee_dependents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


