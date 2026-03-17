# Employee

A dictionary of employee field names and their new values. The properties listed below are commonly used fields, but any valid employee field name can be used as a key. To discover all available field names, call the list-fields endpoint (operationId: list-fields, GET /api/v1/meta/fields). Only the fields you include will be updated; omitted fields are left unchanged. Some string-valued fields are backed by lists or lookups, so callers should use valid option values from BambooHR metadata rather than assuming any free-text string will persist as entered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Legal first name. | [optional] 
**last_name** | **str** | Legal last name. | [optional] 
**work_email** | **str** | Work email address. | [optional] 
**job_title** | **str** | Job title. | [optional] 
**department** | **str** | Department name. | [optional] 
**division** | **str** | Division name. | [optional] 
**location** | **str** | Location name. | [optional] 
**hire_date** | **date** | Hire date in YYYY-MM-DD format. | [optional] 
**mobile_phone** | **str** | Mobile phone number. | [optional] 
**home_phone** | **str** | Home phone number. | [optional] 
**work_phone** | **str** | Work phone number. | [optional] 
**address1** | **str** | Street address line 1. | [optional] 
**city** | **str** | City. | [optional] 
**state** | **str** | State or province. Values are normalized to standard abbreviations (e.g., \&quot;Pennsylvania\&quot; becomes \&quot;PA\&quot;). | [optional] 
**zipcode** | **str** | ZIP or postal code. | [optional] 
**country** | **str** | Country name. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee import Employee

# TODO update the JSON string below
json = "{}"
# create an instance of Employee from a JSON string
employee_instance = Employee.from_json(json)
# print the JSON string representation of the object
print(Employee.to_json())

# convert the object into a dict
employee_dict = employee_instance.to_dict()
# create an instance of Employee from a dict
employee_from_dict = Employee.from_dict(employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


