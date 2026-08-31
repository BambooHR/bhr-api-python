# PayGradesAndBandsConfigurationStatusLevels


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_complete** | **bool** | Whether the levels setup step has been completed. | 
**errors** | [**List[PayGradesAndBandsConfigurationStatusLevelsErrorsInner]**](PayGradesAndBandsConfigurationStatusLevelsErrorsInner.md) | Blocking issues preventing this step from completing. Empty when there are none, and also empty when this step has not yet been visited, so an empty array does not necessarily mean there are no outstanding issues. | 
**warnings** | [**List[PayGradesAndBandsConfigurationStatusLevelsErrorsInner]**](PayGradesAndBandsConfigurationStatusLevelsErrorsInner.md) | Non-blocking issues flagged for this step. Empty when there are none, and also empty when this step has not yet been visited, so an empty array does not necessarily mean there are no outstanding issues. | 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_configuration_status_levels import PayGradesAndBandsConfigurationStatusLevels

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsConfigurationStatusLevels from a JSON string
pay_grades_and_bands_configuration_status_levels_instance = PayGradesAndBandsConfigurationStatusLevels.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsConfigurationStatusLevels.to_json())

# convert the object into a dict
pay_grades_and_bands_configuration_status_levels_dict = pay_grades_and_bands_configuration_status_levels_instance.to_dict()
# create an instance of PayGradesAndBandsConfigurationStatusLevels from a dict
pay_grades_and_bands_configuration_status_levels_from_dict = PayGradesAndBandsConfigurationStatusLevels.from_dict(pay_grades_and_bands_configuration_status_levels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


