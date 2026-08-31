# LevelsAndBandsColumnMap

Schema for levels and bands column map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_column_key** | **str** |  | [optional] 
**column_name** | **str** | Column name | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_column_map import LevelsAndBandsColumnMap

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsColumnMap from a JSON string
levels_and_bands_column_map_instance = LevelsAndBandsColumnMap.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsColumnMap.to_json())

# convert the object into a dict
levels_and_bands_column_map_dict = levels_and_bands_column_map_instance.to_dict()
# create an instance of LevelsAndBandsColumnMap from a dict
levels_and_bands_column_map_from_dict = LevelsAndBandsColumnMap.from_dict(levels_and_bands_column_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


