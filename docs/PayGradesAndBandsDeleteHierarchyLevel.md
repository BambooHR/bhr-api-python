# PayGradesAndBandsDeleteHierarchyLevel


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
**job_titles** | [**List[PayGradesAndBandsDeleteHierarchyJobTitle]**](PayGradesAndBandsDeleteHierarchyJobTitle.md) | Job titles assigned to this level. | [optional] 
**errors** | **List[str]** | Validation errors for this level. | [optional] 
**warnings** | **List[str]** | Validation warnings for this level. | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_delete_hierarchy_level import PayGradesAndBandsDeleteHierarchyLevel

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsDeleteHierarchyLevel from a JSON string
pay_grades_and_bands_delete_hierarchy_level_instance = PayGradesAndBandsDeleteHierarchyLevel.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsDeleteHierarchyLevel.to_json())

# convert the object into a dict
pay_grades_and_bands_delete_hierarchy_level_dict = pay_grades_and_bands_delete_hierarchy_level_instance.to_dict()
# create an instance of PayGradesAndBandsDeleteHierarchyLevel from a dict
pay_grades_and_bands_delete_hierarchy_level_from_dict = PayGradesAndBandsDeleteHierarchyLevel.from_dict(pay_grades_and_bands_delete_hierarchy_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


