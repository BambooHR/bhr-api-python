# PayGradesAndBandsJobTitleAssignmentsLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_id** | **int** |  | [optional] 
**level_name** | **str** |  | [optional] 
**min** | [**LevelsAndBandsPayBandValue**](LevelsAndBandsPayBandValue.md) | Minimum pay band value with its own validation state. | [optional] 
**mid** | [**LevelsAndBandsPayBandValue**](LevelsAndBandsPayBandValue.md) | Midpoint pay band value with its own validation state. | [optional] 
**max** | [**LevelsAndBandsPayBandValue**](LevelsAndBandsPayBandValue.md) | Maximum pay band value with its own validation state. | [optional] 
**percentage_range** | [**LevelsAndBandsPayBandValue**](LevelsAndBandsPayBandValue.md) | Percentage-range pay band value with its own validation state; its &#x60;value&#x60; is null for min-mid-max bands. | [optional] 
**currency_code** | **str** |  | [optional] 
**compensation_type** | **str** | Compensation type for the level. | [optional] 
**job_titles** | [**List[PayGradesAndBandsJobTitleAssignmentsJobTitle]**](PayGradesAndBandsJobTitleAssignmentsJobTitle.md) | Job titles assigned to this level. | [optional] 
**errors** | **List[str]** | Validation errors for this level. | [optional] 
**warnings** | **List[str]** | Validation warnings for this level. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_job_title_assignments_level import PayGradesAndBandsJobTitleAssignmentsLevel

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsJobTitleAssignmentsLevel from a JSON string
pay_grades_and_bands_job_title_assignments_level_instance = PayGradesAndBandsJobTitleAssignmentsLevel.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsJobTitleAssignmentsLevel.to_json())

# convert the object into a dict
pay_grades_and_bands_job_title_assignments_level_dict = pay_grades_and_bands_job_title_assignments_level_instance.to_dict()
# create an instance of PayGradesAndBandsJobTitleAssignmentsLevel from a dict
pay_grades_and_bands_job_title_assignments_level_from_dict = PayGradesAndBandsJobTitleAssignmentsLevel.from_dict(pay_grades_and_bands_job_title_assignments_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


