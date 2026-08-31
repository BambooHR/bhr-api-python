# PayGradesAndBandsConfigurationStatusReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_complete** | **bool** | Whether the review step has been completed. | 
**errors** | [**List[PayGradesAndBandsConfigurationStatusLevelsErrorsInner]**](PayGradesAndBandsConfigurationStatusLevelsErrorsInner.md) | Blocking issues preventing this step from completing. Empty when there are none, and also empty when this step has not yet been visited, so an empty array does not necessarily mean there are no outstanding issues. | 
**warnings** | [**List[PayGradesAndBandsConfigurationStatusLevelsErrorsInner]**](PayGradesAndBandsConfigurationStatusLevelsErrorsInner.md) | Non-blocking issues flagged for this step. Empty when there are none, and also empty when this step has not yet been visited, so an empty array does not necessarily mean there are no outstanding issues. | 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_configuration_status_review import PayGradesAndBandsConfigurationStatusReview

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsConfigurationStatusReview from a JSON string
pay_grades_and_bands_configuration_status_review_instance = PayGradesAndBandsConfigurationStatusReview.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsConfigurationStatusReview.to_json())

# convert the object into a dict
pay_grades_and_bands_configuration_status_review_dict = pay_grades_and_bands_configuration_status_review_instance.to_dict()
# create an instance of PayGradesAndBandsConfigurationStatusReview from a dict
pay_grades_and_bands_configuration_status_review_from_dict = PayGradesAndBandsConfigurationStatusReview.from_dict(pay_grades_and_bands_configuration_status_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


