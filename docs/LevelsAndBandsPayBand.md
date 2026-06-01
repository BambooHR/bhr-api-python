# LevelsAndBandsPayBand

Pay band data object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_id** | **int** |  | [optional] 
**min** | **float** | The minimum value for the level | [optional] 
**mid** | **float** | The middle value for the level | [optional] 
**max** | **float** | The maximum value for the level | [optional] 
**currency_code** | **str** |  | [optional] 
**percentage_range** | **float** | The percentage range for the level | [optional] 
**compensation_type** | **str** | The compensation type for the level | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_pay_band import LevelsAndBandsPayBand

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsPayBand from a JSON string
levels_and_bands_pay_band_instance = LevelsAndBandsPayBand.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsPayBand.to_json())

# convert the object into a dict
levels_and_bands_pay_band_dict = levels_and_bands_pay_band_instance.to_dict()
# create an instance of LevelsAndBandsPayBand from a dict
levels_and_bands_pay_band_from_dict = LevelsAndBandsPayBand.from_dict(levels_and_bands_pay_band_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


