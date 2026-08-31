# PayGradesAndBandsConfigurationStatusLevelsErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | Compensation level group ID. | [optional] 
**level_id** | **int** | Level ID. A value of &#x60;0&#x60; is a sentinel meaning the issue applies to the group as a whole rather than to a specific level. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_configuration_status_levels_errors_inner import PayGradesAndBandsConfigurationStatusLevelsErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsConfigurationStatusLevelsErrorsInner from a JSON string
pay_grades_and_bands_configuration_status_levels_errors_inner_instance = PayGradesAndBandsConfigurationStatusLevelsErrorsInner.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsConfigurationStatusLevelsErrorsInner.to_json())

# convert the object into a dict
pay_grades_and_bands_configuration_status_levels_errors_inner_dict = pay_grades_and_bands_configuration_status_levels_errors_inner_instance.to_dict()
# create an instance of PayGradesAndBandsConfigurationStatusLevelsErrorsInner from a dict
pay_grades_and_bands_configuration_status_levels_errors_inner_from_dict = PayGradesAndBandsConfigurationStatusLevelsErrorsInner.from_dict(pay_grades_and_bands_configuration_status_levels_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


