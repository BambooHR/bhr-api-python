# GetEmployeesEmployeeResponse

Employee data response object containing basic employee information and optionally requested fields. When the `fields` parameter is provided, additional requested fields will be included. Field values are subject to permission checks — restricted fields are returned as `null` and their names are listed in `_restrictedFields`.

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
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**age** | **str** |  | [optional] 
**allergies** | **str** |  | [optional] 
**best_email** | **str** |  | [optional] 
**birth_date** | **str** |  | [optional] 
**birthplace** | **str** |  | [optional] 
**citizenship** | **str** |  | [optional] 
**citizenship_id** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**compensation_change_reason** | **str** |  | [optional] 
**compensation_change_reason_id** | **str** |  | [optional] 
**compensation_comment** | **str** |  | [optional] 
**compensation_effective_date** | **str** |  | [optional] 
**compensation_end_date** | **str** |  | [optional] 
**contract_end_date** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**department_id** | **str** |  | [optional] 
**department_name** | **str** |  | [optional] 
**dietary_restrictions** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**division_id** | **str** |  | [optional] 
**division_name** | **str** |  | [optional] 
**eeo_job_category** | **str** |  | [optional] 
**eeo_job_category_id** | **str** |  | [optional] 
**ein** | **str** |  | [optional] 
**eligible_for_rehire** | **str** |  | [optional] 
**eligible_for_rehire_id** | **str** |  | [optional] 
**employee_name** | **str** |  | [optional] 
**employee_number** | **str** |  | [optional] 
**employment_status_comment** | **str** |  | [optional] 
**employment_status_effective_date** | **str** |  | [optional] 
**employment_status_id** | **str** |  | [optional] 
**employment_status_name** | **str** |  | [optional] 
**employment_type** | **str** |  | [optional] 
**employment_type_id** | **str** |  | [optional] 
**ethnicity** | **str** |  | [optional] 
**ethnicity_id** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**final_dose_administration_date** | **str** |  | [optional] 
**final_pay_date** | **str** |  | [optional] 
**first_name_last_name** | **str** |  | [optional] 
**first_name_middle_initial** | **str** |  | [optional] 
**flsa_code** | **str** |  | [optional] 
**flsa_code_id** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**gender_identity** | **str** |  | [optional] 
**gender_identity_id** | **List[int]** | Employee&#39;s gender identity ID. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**hire_date** | **str** |  | [optional] 
**home_email** | **str** |  | [optional] 
**home_phone** | **str** |  | [optional] 
**hours_per_pay_cycle** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**is_manager** | **bool** |  | [optional] 
**jacket_size** | **str** |  | [optional] 
**jacket_size_id** | **str** |  | [optional] 
**job_information_effective_date** | **str** |  | [optional] 
**job_title_id** | **str** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**location_name** | **str** |  | [optional] 
**marital_status** | **str** |  | [optional] 
**middle_initial** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**national_id** | **str** |  | [optional] 
**national_insurance_category** | **str** |  | [optional] 
**national_insurance_category_id** | **str** |  | [optional] 
**nationality** | **str** |  | [optional] 
**nationality_id** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**nin** | **str** |  | [optional] 
**notice_period** | **str** |  | [optional] 
**notice_period_id** | **str** |  | [optional] 
**original_hire_date** | **str** |  | [optional] 
**overtime** | **str** |  | [optional] 
**overtime_rate** | [**GetEmployeesEmployeeResponseAllOfOvertimeRate**](GetEmployeesEmployeeResponseAllOfOvertimeRate.md) |  | [optional] 
**paid_per** | **str** |  | [optional] 
**pay_rate** | [**GetEmployeesEmployeeResponseAllOfPayRate**](GetEmployeesEmployeeResponseAllOfPayRate.md) |  | [optional] 
**pay_schedule** | **str** |  | [optional] 
**pay_schedule_id** | **str** |  | [optional] 
**pay_type** | **str** |  | [optional] 
**pinterest_url** | **str** |  | [optional] 
**preferred_name_last_name** | **str** |  | [optional] 
**probation_end_date** | **str** |  | [optional] 
**pronouns** | **str** |  | [optional] 
**pronouns_id** | **str** |  | [optional] 
**proof_of_vaccination** | **bool** |  | [optional] 
**reports_to_id** | **str** |  | [optional] 
**reports_to_name** | **str** |  | [optional] 
**secondary_language** | **str** |  | [optional] 
**shirt_size** | **str** |  | [optional] 
**shirt_size_id** | **str** |  | [optional] 
**sin** | **str** |  | [optional] 
**skype_username** | **str** |  | [optional] 
**ssn** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**tax_type_id** | **str** |  | [optional] 
**teams** | [**List[GetEmployeesEmployeeResponseAllOfTeams]**](GetEmployeesEmployeeResponseAllOfTeams.md) | Employee&#39;s teams. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**tenure** | **str** |  | [optional] 
**termination_date** | **str** |  | [optional] 
**termination_reason** | **str** |  | [optional] 
**termination_reason_id** | **str** |  | [optional] 
**termination_regrettable** | **str** |  | [optional] 
**termination_regrettable_id** | **str** |  | [optional] 
**termination_type** | **str** |  | [optional] 
**termination_type_id** | **str** |  | [optional] 
**t_shirt_size** | **str** |  | [optional] 
**t_shirt_size_id** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**vaccination_status** | **str** |  | [optional] 
**vaccination_status_id** | **str** |  | [optional] 
**vaccine_received** | **str** |  | [optional] 
**vaccine_received_id** | **str** |  | [optional] 
**veteran_status** | **str** |  | [optional] 
**veteran_status_id** | **List[int]** | Employee&#39;s veteran status ID. Only included when requested via the &#x60;fields&#x60; parameter. | [optional] 
**work_email** | **str** |  | [optional] 
**work_phone** | **str** |  | [optional] 
**work_phone_extension** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 

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


