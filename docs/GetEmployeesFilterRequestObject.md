# GetEmployeesFilterRequestObject

Filter criteria for the employee list endpoint, supplied as `filter[fieldName]=value` query parameters. All filter fields are optional, and multiple fields are combined with AND logic.  Three matching strategies are used depending on the field:  - **Substring** (case-insensitive `LIKE`) — applied to free-text fields such as names, addresses, social URLs, and free-form labels. - **Equality** — applied to IDs (integer), enumerated string values, booleans (`true`/`false`), numeric values, and ISO 8601 dates (`YYYY-MM-DD`). - **Special** — `ids` accepts a list of employee IDs (`filter[ids][]=123&filter[ids][]=124` or `filter[ids]=123,124`).  Filtering is **not supported** for the following fields and will return a 422: `bestEmail`, `ein`, `genderIdentity`, `genderIdentityId`, `nationalId`, `nin`, `overtime`, `overtimeRate`, `payRate`, `sin`, `ssn`, `teams`, `userId`, `veteranStatus`, `veteranStatusId`. Any unrecognized filter key will also return a 422.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | Substring match (case-insensitive). | [optional] 
**address_line2** | **str** | Substring match (case-insensitive). | [optional] 
**allergies** | **str** | Substring match (case-insensitive). | [optional] 
**birthplace** | **str** | Substring match (case-insensitive). | [optional] 
**citizenship** | **str** | Substring match (case-insensitive). | [optional] 
**city** | **str** | Substring match (case-insensitive). | [optional] 
**compensation_change_reason** | **str** | Substring match (case-insensitive). | [optional] 
**compensation_comment** | **str** | Substring match (case-insensitive). | [optional] 
**country** | **str** | Substring match (case-insensitive). | [optional] 
**department_name** | **str** | Substring match (case-insensitive). | [optional] 
**dietary_restrictions** | **str** | Substring match (case-insensitive). | [optional] 
**display_name** | **str** | Substring match (case-insensitive). | [optional] 
**division_name** | **str** | Substring match (case-insensitive). | [optional] 
**eeo_job_category** | **str** | Substring match (case-insensitive). | [optional] 
**eligible_for_rehire** | **str** | Substring match (case-insensitive). | [optional] 
**employee_name** | **str** | Substring match (case-insensitive). | [optional] 
**employee_number** | **str** | Substring match (case-insensitive). | [optional] 
**employment_status_name** | **str** | Substring match (case-insensitive). | [optional] 
**employment_status_comment** | **str** | Substring match (case-insensitive). | [optional] 
**employment_type** | **str** | Substring match (case-insensitive). | [optional] 
**ethnicity** | **str** | Substring match (case-insensitive). | [optional] 
**facebook_url** | **str** | Substring match (case-insensitive). | [optional] 
**first_name_last_name** | **str** | Substring match (case-insensitive). | [optional] 
**first_name_middle_initial** | **str** | Substring match (case-insensitive). | [optional] 
**flsa_code** | **str** | Substring match (case-insensitive). | [optional] 
**home_email** | **str** | Substring match (case-insensitive). | [optional] 
**home_phone** | **str** | Substring match (case-insensitive). | [optional] 
**instagram_url** | **str** | Substring match (case-insensitive). | [optional] 
**jacket_size** | **str** | Substring match (case-insensitive). | [optional] 
**linkedin_url** | **str** | Substring match (case-insensitive). | [optional] 
**location_name** | **str** | Substring match (case-insensitive). | [optional] 
**marital_status** | **str** | Substring match (case-insensitive). | [optional] 
**middle_initial** | **str** | Substring match (case-insensitive). | [optional] 
**middle_name** | **str** | Substring match (case-insensitive). | [optional] 
**mobile_phone** | **str** | Substring match (case-insensitive). | [optional] 
**national_insurance_category** | **str** | Substring match (case-insensitive). | [optional] 
**nationality** | **str** | Substring match (case-insensitive). | [optional] 
**nick_name** | **str** | Substring match (case-insensitive). | [optional] 
**notice_period** | **str** | Substring match (case-insensitive). | [optional] 
**pay_schedule** | **str** | Substring match (case-insensitive). | [optional] 
**pinterest_url** | **str** | Substring match (case-insensitive). | [optional] 
**preferred_name_last_name** | **str** | Substring match (case-insensitive). | [optional] 
**pronouns** | **str** | Substring match (case-insensitive). | [optional] 
**reports_to_name** | **str** | Substring match (case-insensitive). | [optional] 
**secondary_language** | **str** | Substring match (case-insensitive). | [optional] 
**shirt_size** | **str** | Substring match (case-insensitive). | [optional] 
**skype_username** | **str** | Substring match (case-insensitive). | [optional] 
**state** | **str** | Substring match (case-insensitive). | [optional] 
**termination_reason** | **str** | Substring match (case-insensitive). | [optional] 
**termination_regrettable** | **str** | Substring match (case-insensitive). | [optional] 
**termination_type** | **str** | Substring match (case-insensitive). | [optional] 
**t_shirt_size** | **str** | Substring match (case-insensitive). | [optional] 
**twitter_url** | **str** | Substring match (case-insensitive). | [optional] 
**vaccination_status** | **str** | Substring match (case-insensitive). | [optional] 
**vaccine_received** | **str** | Substring match (case-insensitive). | [optional] 
**work_email** | **str** | Substring match (case-insensitive). | [optional] 
**work_phone** | **str** | Substring match (case-insensitive). | [optional] 
**work_phone_extension** | **str** | Substring match (case-insensitive). | [optional] 
**zipcode** | **str** | Substring match (case-insensitive). | [optional] 
**gender** | **str** | Exact match. | [optional] 
**paid_per** | **str** | Exact match. | [optional] 
**pay_type** | **str** | Exact match. | [optional] 
**citizenship_id** | **int** | Exact match against an integer ID. | [optional] 
**compensation_change_reason_id** | **int** | Exact match against an integer ID. | [optional] 
**country_id** | **int** | Exact match against an integer ID. | [optional] 
**department_id** | **int** | Exact match against an integer ID. | [optional] 
**division_id** | **int** | Exact match against an integer ID. | [optional] 
**eeo_job_category_id** | **int** | Exact match against an integer ID. | [optional] 
**eligible_for_rehire_id** | **int** | Exact match against an integer ID. | [optional] 
**employment_status_id** | **int** | Exact match against an integer ID. | [optional] 
**employment_type_id** | **int** | Exact match against an integer ID. | [optional] 
**ethnicity_id** | **int** | Exact match against an integer ID. | [optional] 
**flsa_code_id** | **int** | Exact match against an integer ID. | [optional] 
**jacket_size_id** | **int** | Exact match against an integer ID. | [optional] 
**job_title_id** | **int** | Exact match against an integer ID. | [optional] 
**location_id** | **int** | Exact match against an integer ID. | [optional] 
**national_insurance_category_id** | **int** | Exact match against an integer ID. | [optional] 
**nationality_id** | **int** | Exact match against an integer ID. | [optional] 
**notice_period_id** | **int** | Exact match against an integer ID. | [optional] 
**pay_schedule_id** | **int** | Exact match against an integer ID. | [optional] 
**pronouns_id** | **int** | Exact match against an integer ID. | [optional] 
**reports_to_id** | **int** | Exact match against an integer ID. | [optional] 
**shirt_size_id** | **int** | Exact match against an integer ID. | [optional] 
**state_id** | **int** | Exact match against an integer ID. | [optional] 
**tax_type_id** | **int** | Exact match against an integer ID. | [optional] 
**termination_reason_id** | **int** | Exact match against an integer ID. | [optional] 
**termination_regrettable_id** | **int** | Exact match against an integer ID. | [optional] 
**termination_type_id** | **int** | Exact match against an integer ID. | [optional] 
**t_shirt_size_id** | **int** | Exact match against an integer ID. | [optional] 
**vaccination_status_id** | **int** | Exact match against an integer ID. | [optional] 
**vaccine_received_id** | **int** | Exact match against an integer ID. | [optional] 
**is_manager** | **bool** | Exact match (true/false). | [optional] 
**proof_of_vaccination** | **bool** | Exact match (true/false). | [optional] 
**age** | **float** | Exact numeric match. | [optional] 
**tenure** | **float** | Exact numeric match. | [optional] 
**hours_per_pay_cycle** | **float** | Exact numeric match. | [optional] 
**birth_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**compensation_effective_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**compensation_end_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**contract_end_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**employment_status_effective_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**final_dose_administration_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**final_pay_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**hire_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**job_information_effective_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**original_hire_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**probation_end_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**termination_date** | **date** | Exact match against an ISO 8601 date (YYYY-MM-DD). | [optional] 
**first_name** | **str** | This will match any employees whose first name contains this string (case insensitive) | [optional] 
**last_name** | **str** | This will match any employees whose last name contains this string (case insensitive) | [optional] 
**job_title_name** | **str** | This will match any employees whose current job title descriptor contains this string (case insensitive) | [optional] 
**status** | **str** | Employee status | [optional] 
**ids** | **List[int]** | List of employee IDs for batch fetch. Documented form: repeated keys (&#x60;filter[ids][]&#x3D;123&amp;filter[ids][]&#x3D;124&#x60;). For backward compatibility, the endpoint also accepts a single comma-separated string (&#x60;filter[ids]&#x3D;123,124&#x60;). | [optional] 

## Example

```python
from bamboohr_sdk.models.get_employees_filter_request_object import GetEmployeesFilterRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeesFilterRequestObject from a JSON string
get_employees_filter_request_object_instance = GetEmployeesFilterRequestObject.from_json(json)
# print the JSON string representation of the object
print(GetEmployeesFilterRequestObject.to_json())

# convert the object into a dict
get_employees_filter_request_object_dict = get_employees_filter_request_object_instance.to_dict()
# create an instance of GetEmployeesFilterRequestObject from a dict
get_employees_filter_request_object_from_dict = GetEmployeesFilterRequestObject.from_dict(get_employees_filter_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


