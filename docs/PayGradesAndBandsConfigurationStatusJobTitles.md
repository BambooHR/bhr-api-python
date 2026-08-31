# PayGradesAndBandsConfigurationStatusJobTitles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_complete** | **bool** | Whether the job titles setup step has been completed. | 
**errors** | **List[Optional[str]]** | Blocking issues for the job titles step. Empty when there are none, and also empty when this step has not yet been visited, so an empty array does not necessarily mean there are no outstanding issues. | 
**warnings** | [**List[PayGradesAndBandsConfigurationStatusJobTitlesWarningsInner]**](PayGradesAndBandsConfigurationStatusJobTitlesWarningsInner.md) | Job titles that are not yet assigned to a level. Empty when there are none, and also empty when this step has not yet been visited, so an empty array does not necessarily mean there are no outstanding issues. | 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_configuration_status_job_titles import PayGradesAndBandsConfigurationStatusJobTitles

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsConfigurationStatusJobTitles from a JSON string
pay_grades_and_bands_configuration_status_job_titles_instance = PayGradesAndBandsConfigurationStatusJobTitles.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsConfigurationStatusJobTitles.to_json())

# convert the object into a dict
pay_grades_and_bands_configuration_status_job_titles_dict = pay_grades_and_bands_configuration_status_job_titles_instance.to_dict()
# create an instance of PayGradesAndBandsConfigurationStatusJobTitles from a dict
pay_grades_and_bands_configuration_status_job_titles_from_dict = PayGradesAndBandsConfigurationStatusJobTitles.from_dict(pay_grades_and_bands_configuration_status_job_titles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


