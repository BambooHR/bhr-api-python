# LevelsAndBandsJobTitleAssignmentsRequest

Request to bulk assign job titles to levels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_titles** | [**List[LevelsAndBandsJobTitleAssignment]**](LevelsAndBandsJobTitleAssignment.md) | Array of job title assignments | 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_job_title_assignments_request import LevelsAndBandsJobTitleAssignmentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsJobTitleAssignmentsRequest from a JSON string
levels_and_bands_job_title_assignments_request_instance = LevelsAndBandsJobTitleAssignmentsRequest.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsJobTitleAssignmentsRequest.to_json())

# convert the object into a dict
levels_and_bands_job_title_assignments_request_dict = levels_and_bands_job_title_assignments_request_instance.to_dict()
# create an instance of LevelsAndBandsJobTitleAssignmentsRequest from a dict
levels_and_bands_job_title_assignments_request_from_dict = LevelsAndBandsJobTitleAssignmentsRequest.from_dict(levels_and_bands_job_title_assignments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


