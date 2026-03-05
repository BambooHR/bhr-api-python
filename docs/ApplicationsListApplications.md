# ApplicationsListApplications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ApplicationsListApplicationsItemsInner]**](ApplicationsListApplicationsItemsInner.md) | List of application objects | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list_applications import ApplicationsListApplications

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsListApplications from a JSON string
applications_list_applications_instance = ApplicationsListApplications.from_json(json)
# print the JSON string representation of the object
print(ApplicationsListApplications.to_json())

# convert the object into a dict
applications_list_applications_dict = applications_list_applications_instance.to_dict()
# create an instance of ApplicationsListApplications from a dict
applications_list_applications_from_dict = ApplicationsListApplications.from_dict(applications_list_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


