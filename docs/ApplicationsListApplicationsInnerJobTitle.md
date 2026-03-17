# ApplicationsListApplicationsInnerJobTitle

Job position title

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Title ID, or null if not set | [optional] 
**label** | **str** | Title text | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list_applications_inner_job_title import ApplicationsListApplicationsInnerJobTitle

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsListApplicationsInnerJobTitle from a JSON string
applications_list_applications_inner_job_title_instance = ApplicationsListApplicationsInnerJobTitle.from_json(json)
# print the JSON string representation of the object
print(ApplicationsListApplicationsInnerJobTitle.to_json())

# convert the object into a dict
applications_list_applications_inner_job_title_dict = applications_list_applications_inner_job_title_instance.to_dict()
# create an instance of ApplicationsListApplicationsInnerJobTitle from a dict
applications_list_applications_inner_job_title_from_dict = ApplicationsListApplicationsInnerJobTitle.from_dict(applications_list_applications_inner_job_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


