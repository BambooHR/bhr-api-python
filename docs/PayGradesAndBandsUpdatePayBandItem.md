# PayGradesAndBandsUpdatePayBandItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_id** | **int** | The compensation level ID to apply pay band values to. Required and must not be null. | 
**min** | **float** |  | [optional] 
**mid** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**percentage_range** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**compensation_type** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.pay_grades_and_bands_update_pay_band_item import PayGradesAndBandsUpdatePayBandItem

# TODO update the JSON string below
json = "{}"
# create an instance of PayGradesAndBandsUpdatePayBandItem from a JSON string
pay_grades_and_bands_update_pay_band_item_instance = PayGradesAndBandsUpdatePayBandItem.from_json(json)
# print the JSON string representation of the object
print(PayGradesAndBandsUpdatePayBandItem.to_json())

# convert the object into a dict
pay_grades_and_bands_update_pay_band_item_dict = pay_grades_and_bands_update_pay_band_item_instance.to_dict()
# create an instance of PayGradesAndBandsUpdatePayBandItem from a dict
pay_grades_and_bands_update_pay_band_item_from_dict = PayGradesAndBandsUpdatePayBandItem.from_dict(pay_grades_and_bands_update_pay_band_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


