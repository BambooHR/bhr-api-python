# PayGradesAndBandsConfigurationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**levels** | [**PayGradesAndBandsConfigurationStatusLevels**](PayGradesAndBandsConfigurationStatusLevels.md) |  | 
**pay_bands** | [**PayGradesAndBandsConfigurationStatusPayBands**](PayGradesAndBandsConfigurationStatusPayBands.md) |  | 
**job_titles** | [**PayGradesAndBandsConfigurationStatusJobTitles**](PayGradesAndBandsConfigurationStatusJobTitles.md) |  | 
**review** | [**PayGradesAndBandsConfigurationStatusReview**](PayGradesAndBandsConfigurationStatusReview.md) |  | 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_configuration_status import PayGradesAndBandsConfigurationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsConfigurationStatus from a JSON string
pay_grades_and_bands_configuration_status_instance = PayGradesAndBandsConfigurationStatus.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsConfigurationStatus.to_json())

# convert the object into a dict
pay_grades_and_bands_configuration_status_dict = pay_grades_and_bands_configuration_status_instance.to_dict()
# create an instance of PayGradesAndBandsConfigurationStatus from a dict
pay_grades_and_bands_configuration_status_from_dict = PayGradesAndBandsConfigurationStatus.from_dict(pay_grades_and_bands_configuration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


