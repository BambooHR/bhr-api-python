# LevelsAndBandsGroupStatusCounts

Schema for levels and bands group status counts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | **int** | Number of levels/bands in draft status | [optional] 
**historic** | **int** | Number of levels/bands in historic status | [optional] 
**published** | **int** | Number of levels/bands in published status | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_group_status_counts import LevelsAndBandsGroupStatusCounts

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsGroupStatusCounts from a JSON string
levels_and_bands_group_status_counts_instance = LevelsAndBandsGroupStatusCounts.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsGroupStatusCounts.to_json())

# convert the object into a dict
levels_and_bands_group_status_counts_dict = levels_and_bands_group_status_counts_instance.to_dict()
# create an instance of LevelsAndBandsGroupStatusCounts from a dict
levels_and_bands_group_status_counts_from_dict = LevelsAndBandsGroupStatusCounts.from_dict(levels_and_bands_group_status_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


