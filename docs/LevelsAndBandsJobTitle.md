# LevelsAndBandsJobTitle

Job Titles Job Title Data Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job title id | [optional] 
**job_title** | **str** | Job title name | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_job_title import LevelsAndBandsJobTitle

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsJobTitle from a JSON string
levels_and_bands_job_title_instance = LevelsAndBandsJobTitle.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsJobTitle.to_json())

# convert the object into a dict
levels_and_bands_job_title_dict = levels_and_bands_job_title_instance.to_dict()
# create an instance of LevelsAndBandsJobTitle from a dict
levels_and_bands_job_title_from_dict = LevelsAndBandsJobTitle.from_dict(levels_and_bands_job_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


