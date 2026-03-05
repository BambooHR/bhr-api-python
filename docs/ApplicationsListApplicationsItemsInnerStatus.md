# ApplicationsListApplicationsItemsInnerStatus

Current status of the application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Status ID | [optional] 
**label** | **str** | Status name | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list_applications_items_inner_status import ApplicationsListApplicationsItemsInnerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsListApplicationsItemsInnerStatus from a JSON string
applications_list_applications_items_inner_status_instance = ApplicationsListApplicationsItemsInnerStatus.from_json(json)
# print the JSON string representation of the object
print(ApplicationsListApplicationsItemsInnerStatus.to_json())

# convert the object into a dict
applications_list_applications_items_inner_status_dict = applications_list_applications_items_inner_status_instance.to_dict()
# create an instance of ApplicationsListApplicationsItemsInnerStatus from a dict
applications_list_applications_items_inner_status_from_dict = ApplicationsListApplicationsItemsInnerStatus.from_dict(applications_list_applications_items_inner_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


