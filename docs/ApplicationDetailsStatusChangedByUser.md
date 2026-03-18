# ApplicationDetailsStatusChangedByUser

The user who last changed the status, or null if changed by the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**avatar** | **str** | URL to avatar image | [optional] 
**job_title** | [**ApplicationDetailsStatusChangedByUserJobTitle**](ApplicationDetailsStatusChangedByUserJobTitle.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_status_changed_by_user import ApplicationDetailsStatusChangedByUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsStatusChangedByUser from a JSON string
application_details_status_changed_by_user_instance = ApplicationDetailsStatusChangedByUser.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsStatusChangedByUser.to_json())

# convert the object into a dict
application_details_status_changed_by_user_dict = application_details_status_changed_by_user_instance.to_dict()
# create an instance of ApplicationDetailsStatusChangedByUser from a dict
application_details_status_changed_by_user_from_dict = ApplicationDetailsStatusChangedByUser.from_dict(application_details_status_changed_by_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


