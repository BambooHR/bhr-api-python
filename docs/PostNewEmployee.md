# PostNewEmployee

A dictionary of employee field names and their values for the new employee. At minimum, firstName and lastName are required. The properties listed below are commonly used fields, but any valid employee field name can be used as a key. To discover all available field names, call the list-fields endpoint (operationId: list-fields, GET /api/v1/meta/fields). Additional fields may use string, number, boolean, array, object, or null values depending on the field type. Some string-valued fields are backed by lists or lookups, so callers should use valid option values from BambooHR metadata rather than assuming any free-text string will persist as entered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Legal first name (required). | 
**last_name** | **str** | Legal last name (required). | 
**work_email** | **str** | Work email address. | [optional] 
**job_title** | **str** | Job title. | [optional] 
**department** | **str** | Department name. | [optional] 
**hire_date** | **date** | Hire date in YYYY-MM-DD format. | [optional] 

## Example

```python
from bamboohr_sdk.models.post_new_employee import PostNewEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of PostNewEmployee from a JSON string
post_new_employee_instance = PostNewEmployee.from_json(json)
# print the JSON string representation of the object
print(PostNewEmployee.to_json())

# convert the object into a dict
post_new_employee_dict = post_new_employee_instance.to_dict()
# create an instance of PostNewEmployee from a dict
post_new_employee_from_dict = PostNewEmployee.from_dict(post_new_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


