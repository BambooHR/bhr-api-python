# GetEmployeeResponse

Employee data returned by the Get Employee endpoint.  The `id` field is always present; all other named properties are included only when explicitly requested via the `fields` query parameter.  Additional custom or company-configured fields may also appear.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the employee | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**preferred_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**job_title_name** | **str** |  | [optional] 
**job_title_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**work_email** | **str** |  | [optional] 
**home_email** | **str** |  | [optional] 
**best_email** | **str** |  | [optional] 
**work_phone** | **str** |  | [optional] 
**work_phone_extension** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**home_phone** | **str** |  | [optional] 
**skype_username** | **str** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**pinterest_url** | **str** |  | [optional] 
**birth_date** | **str** |  | [optional] 
**hire_date** | **str** |  | [optional] 
**original_hire_date** | **str** |  | [optional] 
**termination_date** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**marital** | **str** |  | [optional] 
**pay_rate** | **str** |  | [optional] 
**pay_type** | **str** |  | [optional] 
**pay_period** | **str** |  | [optional] 
**exempt** | **str** |  | [optional] 
**can_upload_photo** | **bool** |  | [optional] 
**division** | **str** |  | [optional] 
**division_id** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**department_id** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**employment_status** | **str** |  | [optional] 
**employment_status_id** | **str** |  | [optional] 
**reports_to_name** | **str** |  | [optional] 
**reports_to_id** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.get_employee_response import GetEmployeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeeResponse from a JSON string
get_employee_response_instance = GetEmployeeResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmployeeResponse.to_json())

# convert the object into a dict
get_employee_response_dict = get_employee_response_instance.to_dict()
# create an instance of GetEmployeeResponse from a dict
get_employee_response_from_dict = GetEmployeeResponse.from_dict(get_employee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


