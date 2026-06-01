# LevelsAndBandsLevelsAndBandsStatus

Object for compensation level groups and levels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**levels** | [**LevelsAndBandsStepStatus**](LevelsAndBandsStepStatus.md) | Object for compensation level groups and levels | 
**pay_bands** | [**LevelsAndBandsStepStatus**](LevelsAndBandsStepStatus.md) | Object for compensation level groups and levels | 
**job_titles** | [**LevelsAndBandsJobTitlesStatus**](LevelsAndBandsJobTitlesStatus.md) | Object for compensation level groups and levels | 
**review** | [**LevelsAndBandsStepStatus**](LevelsAndBandsStepStatus.md) | Object for compensation level groups and levels | 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_levels_and_bands_status import LevelsAndBandsLevelsAndBandsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsLevelsAndBandsStatus from a JSON string
levels_and_bands_levels_and_bands_status_instance = LevelsAndBandsLevelsAndBandsStatus.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsLevelsAndBandsStatus.to_json())

# convert the object into a dict
levels_and_bands_levels_and_bands_status_dict = levels_and_bands_levels_and_bands_status_instance.to_dict()
# create an instance of LevelsAndBandsLevelsAndBandsStatus from a dict
levels_and_bands_levels_and_bands_status_from_dict = LevelsAndBandsLevelsAndBandsStatus.from_dict(levels_and_bands_levels_and_bands_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


