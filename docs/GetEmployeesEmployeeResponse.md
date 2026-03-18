# GetEmployeesEmployeeResponse

Employee data response object containing basic employee information and permission-restricted fields. When the `fields` parameter is provided, additional requested fields will be included in the response. Invalid field names are silently ignored. Field values are subject to permission checks - restricted fields will be null and their names will appear in `_restrictedFields`. The `_restrictedFields` property is only present when at least one field is restricted; it is omitted entirely on records with no restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Unique identifier for the employee | 
**first_name** | **str** | Employee&#39;s first name | 
**last_name** | **str** | Employee&#39;s last name | 
**preferred_name** | **str** | Employee&#39;s preferred name | 
**photo_url** | **str** | URL to employee&#39;s profile photo | 
**job_title_name** | **str** | Employee&#39;s current job title | 
**status** | **str** | Employee&#39;s current status (Active or Inactive). | 
**restricted_fields** | **List[str]** | Array of field names that are restricted due to permission checks | [optional] 
**work_email** | **str** | Employee&#39;s work email address. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**home_email** | **str** | Employee&#39;s home email address. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**best_email** | **str** | Employee&#39;s best email address. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**middle_name** | **str** | Employee&#39;s middle name. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**work_phone** | **str** | Employee&#39;s work phone number. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**work_phone_extension** | **str** | Employee&#39;s work phone extension. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**mobile_phone** | **str** | Employee&#39;s mobile phone number. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**home_phone** | **str** | Employee&#39;s home phone number. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**skype_username** | **str** | Employee&#39;s Skype username. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**linkedin_url** | **str** | Employee&#39;s LinkedIn profile URL. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**facebook_url** | **str** | Employee&#39;s Facebook profile URL. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**instagram_url** | **str** | Employee&#39;s Instagram profile URL. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**twitter_url** | **str** | Employee&#39;s Twitter/X profile URL. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**pinterest_url** | **str** | Employee&#39;s Pinterest profile URL. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 

## Example

```python
from bamboohr_sdk.models.get_employees_employee_response import GetEmployeesEmployeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeesEmployeeResponse from a JSON string
get_employees_employee_response_instance = GetEmployeesEmployeeResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmployeesEmployeeResponse.to_json())

# convert the object into a dict
get_employees_employee_response_dict = get_employees_employee_response_instance.to_dict()
# create an instance of GetEmployeesEmployeeResponse from a dict
get_employees_employee_response_from_dict = GetEmployeesEmployeeResponse.from_dict(get_employees_employee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


