# LevelsAndBandsGroup

Represents a compensation level group with its levels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**levels** | [**List[LevelsAndBandsLevel]**](LevelsAndBandsLevel.md) | Array of levels in this group | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_group import LevelsAndBandsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsGroup from a JSON string
levels_and_bands_group_instance = LevelsAndBandsGroup.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsGroup.to_json())

# convert the object into a dict
levels_and_bands_group_dict = levels_and_bands_group_instance.to_dict()
# create an instance of LevelsAndBandsGroup from a dict
levels_and_bands_group_from_dict = LevelsAndBandsGroup.from_dict(levels_and_bands_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


