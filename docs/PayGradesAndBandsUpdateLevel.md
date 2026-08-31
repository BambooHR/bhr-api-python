# PayGradesAndBandsUpdateLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_id** | **int** |  | [optional] 
**level_name** | **str** |  | [optional] 
**compensation_type** | **str** | Not applied by this endpoint. A newly created level derives its compensation type from the group&#39;s existing compensation type (or &#x60;Salary&#x60; when the group has none); existing levels keep their compensation type unchanged. | [optional] 
**min** | **float** |  | [optional] 
**mid** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**percentage_range** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_update_level import PayGradesAndBandsUpdateLevel

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsUpdateLevel from a JSON string
pay_grades_and_bands_update_level_instance = PayGradesAndBandsUpdateLevel.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsUpdateLevel.to_json())

# convert the object into a dict
pay_grades_and_bands_update_level_dict = pay_grades_and_bands_update_level_instance.to_dict()
# create an instance of PayGradesAndBandsUpdateLevel from a dict
pay_grades_and_bands_update_level_from_dict = PayGradesAndBandsUpdateLevel.from_dict(pay_grades_and_bands_update_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


