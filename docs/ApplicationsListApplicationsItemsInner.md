# ApplicationsListApplicationsItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Application ID | [optional] 
**applied_date** | **date** | Date when the application was submitted (yyyy-mm-dd) | [optional] 
**status** | [**ApplicationsListApplicationsItemsInnerStatus**](ApplicationsListApplicationsItemsInnerStatus.md) |  | [optional] 
**rating** | **int** | Candidate rating (1-5) or null if not rated | [optional] 
**applicant** | [**ApplicationsListApplicationsItemsInnerApplicant**](ApplicationsListApplicationsItemsInnerApplicant.md) |  | [optional] 
**job** | [**ApplicationsListApplicationsItemsInnerJob**](ApplicationsListApplicationsItemsInnerJob.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list_applications_items_inner import ApplicationsListApplicationsItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsListApplicationsItemsInner from a JSON string
applications_list_applications_items_inner_instance = ApplicationsListApplicationsItemsInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationsListApplicationsItemsInner.to_json())

# convert the object into a dict
applications_list_applications_items_inner_dict = applications_list_applications_items_inner_instance.to_dict()
# create an instance of ApplicationsListApplicationsItemsInner from a dict
applications_list_applications_items_inner_from_dict = ApplicationsListApplicationsItemsInner.from_dict(applications_list_applications_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


