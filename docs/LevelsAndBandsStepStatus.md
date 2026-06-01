# LevelsAndBandsStepStatus

Object for compensation level groups and levels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_complete** | **bool** | Whether the step is complete | 
**errors** | [**List[LevelsAndBandsErrorWarningIdentifier]**](LevelsAndBandsErrorWarningIdentifier.md) | Array of errors | 
**warnings** | [**List[LevelsAndBandsErrorWarningIdentifier]**](LevelsAndBandsErrorWarningIdentifier.md) | Array of warnings | 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_step_status import LevelsAndBandsStepStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsStepStatus from a JSON string
levels_and_bands_step_status_instance = LevelsAndBandsStepStatus.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsStepStatus.to_json())

# convert the object into a dict
levels_and_bands_step_status_dict = levels_and_bands_step_status_instance.to_dict()
# create an instance of LevelsAndBandsStepStatus from a dict
levels_and_bands_step_status_from_dict = LevelsAndBandsStepStatus.from_dict(levels_and_bands_step_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


