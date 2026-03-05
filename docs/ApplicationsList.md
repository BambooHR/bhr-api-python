# ApplicationsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_complete** | **bool** | Indicates whether there are more pages of results available | [optional] 
**next_page_url** | **str** | URL to fetch the next page of results, or null if there are no more results | [optional] 
**applications** | [**ApplicationsListApplications**](ApplicationsListApplications.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.applications_list import ApplicationsList

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsList from a JSON string
applications_list_instance = ApplicationsList.from_json(json)
# print the JSON string representation of the object
print(ApplicationsList.to_json())

# convert the object into a dict
applications_list_dict = applications_list_instance.to_dict()
# create an instance of ApplicationsList from a dict
applications_list_from_dict = ApplicationsList.from_dict(applications_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


