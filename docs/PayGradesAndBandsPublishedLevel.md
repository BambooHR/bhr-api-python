# PayGradesAndBandsPublishedLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_id** | **int** | Compensation level identifier. | [optional] 
**level_name** | **str** |  | [optional] 
**min** | **float** |  | [optional] 
**mid** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**percentage_range** | [**LevelsAndBandsPayBandValue**](LevelsAndBandsPayBandValue.md) | Percentage-range pay band value object; its &#x60;value&#x60; is null for min-mid-max bands. | [optional] 
**compensation_type** | **str** | Compensation type for the level. | [optional] 
**job_titles** | [**List[PayGradesAndBandsPublishedJobTitle]**](PayGradesAndBandsPublishedJobTitle.md) | Job titles assigned to this level. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_published_level import PayGradesAndBandsPublishedLevel

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsPublishedLevel from a JSON string
pay_grades_and_bands_published_level_instance = PayGradesAndBandsPublishedLevel.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsPublishedLevel.to_json())

# convert the object into a dict
pay_grades_and_bands_published_level_dict = pay_grades_and_bands_published_level_instance.to_dict()
# create an instance of PayGradesAndBandsPublishedLevel from a dict
pay_grades_and_bands_published_level_from_dict = PayGradesAndBandsPublishedLevel.from_dict(pay_grades_and_bands_published_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


