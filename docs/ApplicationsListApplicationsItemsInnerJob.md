# ApplicationsListApplicationsItemsInnerJob

Information about the job position

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job position ID | [optional] 
**title** | **str** | Job position title | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list_applications_items_inner_job import ApplicationsListApplicationsItemsInnerJob

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsListApplicationsItemsInnerJob from a JSON string
applications_list_applications_items_inner_job_instance = ApplicationsListApplicationsItemsInnerJob.from_json(json)
# print the JSON string representation of the object
print(ApplicationsListApplicationsItemsInnerJob.to_json())

# convert the object into a dict
applications_list_applications_items_inner_job_dict = applications_list_applications_items_inner_job_instance.to_dict()
# create an instance of ApplicationsListApplicationsItemsInnerJob from a dict
applications_list_applications_items_inner_job_from_dict = ApplicationsListApplicationsItemsInnerJob.from_dict(applications_list_applications_items_inner_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


