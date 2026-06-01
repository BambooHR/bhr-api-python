# LevelsAndBandsErrorWarningIdentifier

Object for compensation level groups and levels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | Group ID | 
**level_id** | **int** | Level ID | 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_error_warning_identifier import LevelsAndBandsErrorWarningIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsErrorWarningIdentifier from a JSON string
levels_and_bands_error_warning_identifier_instance = LevelsAndBandsErrorWarningIdentifier.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsErrorWarningIdentifier.to_json())

# convert the object into a dict
levels_and_bands_error_warning_identifier_dict = levels_and_bands_error_warning_identifier_instance.to_dict()
# create an instance of LevelsAndBandsErrorWarningIdentifier from a dict
levels_and_bands_error_warning_identifier_from_dict = LevelsAndBandsErrorWarningIdentifier.from_dict(levels_and_bands_error_warning_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


