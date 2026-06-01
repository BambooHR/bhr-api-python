# LevelsAndBandsJobTitleAssignment

Job title assignment to a level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_title_id** | **int** | Job title id | [optional] 
**level_id** | **int** | Compensation level id | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_job_title_assignment import LevelsAndBandsJobTitleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsJobTitleAssignment from a JSON string
levels_and_bands_job_title_assignment_instance = LevelsAndBandsJobTitleAssignment.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsJobTitleAssignment.to_json())

# convert the object into a dict
levels_and_bands_job_title_assignment_dict = levels_and_bands_job_title_assignment_instance.to_dict()
# create an instance of LevelsAndBandsJobTitleAssignment from a dict
levels_and_bands_job_title_assignment_from_dict = LevelsAndBandsJobTitleAssignment.from_dict(levels_and_bands_job_title_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


