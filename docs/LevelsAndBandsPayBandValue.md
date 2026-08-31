# LevelsAndBandsPayBandValue

Represents a single compensation pay band value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**errors** | **List[str]** | Array of validation errors for this pay band | [optional] 
**warnings** | **List[str]** | Array of validation warnings for this pay band | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_pay_band_value import LevelsAndBandsPayBandValue

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsPayBandValue from a JSON string
levels_and_bands_pay_band_value_instance = LevelsAndBandsPayBandValue.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsPayBandValue.to_json())

# convert the object into a dict
levels_and_bands_pay_band_value_dict = levels_and_bands_pay_band_value_instance.to_dict()
# create an instance of LevelsAndBandsPayBandValue from a dict
levels_and_bands_pay_band_value_from_dict = LevelsAndBandsPayBandValue.from_dict(levels_and_bands_pay_band_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


