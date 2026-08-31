# PayGradesAndBandsJobTitleEmployee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal employee ID (the same identifier is &#x60;employeeId&#x60; on List Employees and &#x60;eeid&#x60; on the employee dataset). This is not the editable Employee # (&#x60;employeeNumber&#x60;). | [optional] 
**name** | **str** | Employee display name. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_job_title_employee import PayGradesAndBandsJobTitleEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsJobTitleEmployee from a JSON string
pay_grades_and_bands_job_title_employee_instance = PayGradesAndBandsJobTitleEmployee.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsJobTitleEmployee.to_json())

# convert the object into a dict
pay_grades_and_bands_job_title_employee_dict = pay_grades_and_bands_job_title_employee_instance.to_dict()
# create an instance of PayGradesAndBandsJobTitleEmployee from a dict
pay_grades_and_bands_job_title_employee_from_dict = PayGradesAndBandsJobTitleEmployee.from_dict(pay_grades_and_bands_job_title_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


