# LevelsAndBandsJobTitleWithEmployees

Levels and bands job titles with employees object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job id | [optional] 
**title** | **str** | Job title | [optional] 
**employees** | [**List[LevelsAndBandsEmployee]**](LevelsAndBandsEmployee.md) | Employees with this job title | [optional] 
**level_id** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_job_title_with_employees import LevelsAndBandsJobTitleWithEmployees

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsJobTitleWithEmployees from a JSON string
levels_and_bands_job_title_with_employees_instance = LevelsAndBandsJobTitleWithEmployees.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsJobTitleWithEmployees.to_json())

# convert the object into a dict
levels_and_bands_job_title_with_employees_dict = levels_and_bands_job_title_with_employees_instance.to_dict()
# create an instance of LevelsAndBandsJobTitleWithEmployees from a dict
levels_and_bands_job_title_with_employees_from_dict = LevelsAndBandsJobTitleWithEmployees.from_dict(levels_and_bands_job_title_with_employees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


