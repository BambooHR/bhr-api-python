# Employee

A dictionary of employee field names and their new values. The properties listed below are commonly used fields, but any valid writable employee field name can be used as a key. To discover all available field names, call the List Fields endpoint (operationId: list-fields, GET /api/v1/meta/fields). Only the fields you include will be updated; omitted fields are left unchanged. Some string-valued fields are backed by lists or lookups, so callers should use valid option values from BambooHR metadata rather than assuming any free-text string will persist as entered. **Important for AI agents:** Unknown or misspelled field names are silently ignored — the endpoint returns 200 but the field is not updated. Always use the exact alias from the schema properties below or from the list-fields endpoint; do not invent aliases by adding prefixes such as `home` (e.g., `homeCity` is wrong — the correct alias is `city`). Photo data is not writable through this schema: photo-related keys are silently ignored. Use the Upload Employee Photo endpoint (operationId: upload-employee-photo) to change a profile photo.

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
**address1** | **str** | Home street address line 1. The correct alias is &#x60;address1&#x60; — do not use &#x60;homeAddress1&#x60;, &#x60;homeStreet1&#x60;, or &#x60;street1&#x60;. | [optional] 
**address2** | **str** | Home street address line 2 (apartment, suite, etc.). The correct alias is &#x60;address2&#x60; — do not use &#x60;homeAddress2&#x60; or &#x60;homeStreet2&#x60;. | [optional] 
**city** | **str** | Home city. The correct alias is &#x60;city&#x60; — do not use &#x60;homeCity&#x60;. | [optional] 
**state** | **str** | Home state or province. The correct alias is &#x60;state&#x60; — do not use &#x60;homeState&#x60;. Values are normalized to standard abbreviations (e.g., \&quot;Pennsylvania\&quot; becomes \&quot;PA\&quot;). | [optional] 
**zipcode** | **str** | Home ZIP or postal code. The correct alias is &#x60;zipcode&#x60; — do not use &#x60;homeZipcode&#x60; or &#x60;homeZip&#x60;. | [optional] 
**country** | **str** | Home country name. The correct alias is &#x60;country&#x60; — do not use &#x60;homeCountry&#x60;. | [optional] 

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


