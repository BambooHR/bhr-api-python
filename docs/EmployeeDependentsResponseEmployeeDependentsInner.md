# EmployeeDependentsResponseEmployeeDependentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the dependent record. | [optional] 
**employee_id** | **str** | The ID of the employee this dependent belongs to. | [optional] 
**first_name** | **str** | The dependent&#39;s first name. | [optional] 
**middle_name** | **str** | The dependent&#39;s middle name. Null if not set. | [optional] 
**last_name** | **str** | The dependent&#39;s last name. | [optional] 
**relationship** | **str** | The dependent&#39;s relationship to the employee. | [optional] 
**gender** | **str** | The dependent&#39;s gender. | [optional] 
**masked_ssn** | **str** | The dependent&#39;s masked SSN (e.g. \&quot;xxx-xx-1234\&quot;). Null if no SSN on file. | [optional] 
**masked_sin** | **str** | The dependent&#39;s masked SIN. Null if no SIN on file. | [optional] 
**date_of_birth** | **date** | The dependent&#39;s date of birth in YYYY-MM-DD format. | [optional] 
**address_line1** | **str** | The first line of the dependent&#39;s address. Null if not set. | [optional] 
**address_line2** | **str** | The second line of the dependent&#39;s address. Null if not set. | [optional] 
**city** | **str** | The dependent&#39;s city. Null if not set. | [optional] 
**state** | **str** | The dependent&#39;s state as a full name (e.g. \&quot;Utah\&quot;). Null if not set. | [optional] 
**zip_code** | **str** | The dependent&#39;s ZIP or postal code. Null if not set. | [optional] 
**home_phone** | **str** | The dependent&#39;s home phone number. Null if not set. | [optional] 
**country** | **str** | The dependent&#39;s country as a full name (e.g. \&quot;United States\&quot;). Null if not set. | [optional] 
**is_us_citizen** | **str** | Whether the dependent is a US citizen. \&quot;yes\&quot; or \&quot;no\&quot;. | [optional] 
**is_student** | **str** | Whether the dependent is currently a student. \&quot;yes\&quot; or \&quot;no\&quot;. | [optional] 

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


