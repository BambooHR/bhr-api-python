# LevelsAndBandsLevel

Represents a single compensation level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_id** | **int** |  | [optional] 
**level_name** | **str** |  | [optional] 
**pay_band** | [**LevelsAndBandsPayBand**](LevelsAndBandsPayBand.md) | Pay band associated with this level | [optional] 
**job_titles** | [**List[LevelsAndBandsJobTitle]**](LevelsAndBandsJobTitle.md) | Array of job titles associated with this level | [optional] 
**errors** | **List[str]** | Array of validation errors for this level | [optional] 
**warnings** | **List[str]** | Array of validation warnings for this level | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_level import LevelsAndBandsLevel

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsLevel from a JSON string
levels_and_bands_level_instance = LevelsAndBandsLevel.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsLevel.to_json())

# convert the object into a dict
levels_and_bands_level_dict = levels_and_bands_level_instance.to_dict()
# create an instance of LevelsAndBandsLevel from a dict
levels_and_bands_level_from_dict = LevelsAndBandsLevel.from_dict(levels_and_bands_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


