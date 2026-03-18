# ApplicationsListApplicationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Application ID | [optional] 
**applied_date** | **datetime** | ISO 8601 datetime when the application was submitted | [optional] 
**status** | [**ApplicationsListApplicationsInnerStatus**](ApplicationsListApplicationsInnerStatus.md) |  | [optional] 
**rating** | **int** | Candidate rating (1-5) or null if not rated | [optional] 
**applicant** | [**ApplicationsListApplicationsInnerApplicant**](ApplicationsListApplicationsInnerApplicant.md) |  | [optional] 
**job** | [**ApplicationsListApplicationsInnerJob**](ApplicationsListApplicationsInnerJob.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list_applications_inner import ApplicationsListApplicationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsListApplicationsInner from a JSON string
applications_list_applications_inner_instance = ApplicationsListApplicationsInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationsListApplicationsInner.to_json())

# convert the object into a dict
applications_list_applications_inner_dict = applications_list_applications_inner_instance.to_dict()
# create an instance of ApplicationsListApplicationsInner from a dict
applications_list_applications_inner_from_dict = ApplicationsListApplicationsInner.from_dict(applications_list_applications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


