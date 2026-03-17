# ApplicationsListApplicationsInnerJob

Information about the job position

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job position ID | [optional] 
**title** | [**ApplicationsListApplicationsInnerJobTitle**](ApplicationsListApplicationsInnerJobTitle.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list_applications_inner_job import ApplicationsListApplicationsInnerJob

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsListApplicationsInnerJob from a JSON string
applications_list_applications_inner_job_instance = ApplicationsListApplicationsInnerJob.from_json(json)
# print the JSON string representation of the object
print(ApplicationsListApplicationsInnerJob.to_json())

# convert the object into a dict
applications_list_applications_inner_job_dict = applications_list_applications_inner_job_instance.to_dict()
# create an instance of ApplicationsListApplicationsInnerJob from a dict
applications_list_applications_inner_job_from_dict = ApplicationsListApplicationsInnerJob.from_dict(applications_list_applications_inner_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


