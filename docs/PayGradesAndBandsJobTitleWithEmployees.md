# PayGradesAndBandsJobTitleWithEmployees


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job title identifier. | [optional] 
**title** | **str** | Job title name. | [optional] 
**employees** | [**List[PayGradesAndBandsJobTitleEmployee]**](PayGradesAndBandsJobTitleEmployee.md) | Employees currently holding this job title. May be empty either because no one holds the title or because the authenticated caller lacks permission to view a required field (name, job title, or id) for the employees who do. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_job_title_with_employees import PayGradesAndBandsJobTitleWithEmployees

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsJobTitleWithEmployees from a JSON string
pay_grades_and_bands_job_title_with_employees_instance = PayGradesAndBandsJobTitleWithEmployees.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsJobTitleWithEmployees.to_json())

# convert the object into a dict
pay_grades_and_bands_job_title_with_employees_dict = pay_grades_and_bands_job_title_with_employees_instance.to_dict()
# create an instance of PayGradesAndBandsJobTitleWithEmployees from a dict
pay_grades_and_bands_job_title_with_employees_from_dict = PayGradesAndBandsJobTitleWithEmployees.from_dict(pay_grades_and_bands_job_title_with_employees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


