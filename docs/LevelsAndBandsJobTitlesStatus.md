# LevelsAndBandsJobTitlesStatus

Object for compensation level groups and levels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_complete** | **bool** | Is the job titles step complete | 
**errors** | **List[str]** | Array of errors | 
**warnings** | **List[object]** | Array of warnings | 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_job_titles_status import LevelsAndBandsJobTitlesStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsJobTitlesStatus from a JSON string
levels_and_bands_job_titles_status_instance = LevelsAndBandsJobTitlesStatus.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsJobTitlesStatus.to_json())

# convert the object into a dict
levels_and_bands_job_titles_status_dict = levels_and_bands_job_titles_status_instance.to_dict()
# create an instance of LevelsAndBandsJobTitlesStatus from a dict
levels_and_bands_job_titles_status_from_dict = LevelsAndBandsJobTitlesStatus.from_dict(levels_and_bands_job_titles_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


