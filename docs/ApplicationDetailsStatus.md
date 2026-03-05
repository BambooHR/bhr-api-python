# ApplicationDetailsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Status ID | [optional] 
**label** | **str** | Status name | [optional] 
**date_changed** | **datetime** | Date when status was last changed | [optional] 
**changed_by_user** | **int** | ID of the user who changed the status | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_status import ApplicationDetailsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsStatus from a JSON string
application_details_status_instance = ApplicationDetailsStatus.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsStatus.to_json())

# convert the object into a dict
application_details_status_dict = application_details_status_instance.to_dict()
# create an instance of ApplicationDetailsStatus from a dict
application_details_status_from_dict = ApplicationDetailsStatus.from_dict(application_details_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


