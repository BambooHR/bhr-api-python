# CreatedTimeOffRequestStatus

The current status of the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The current status value (e.g. &#x60;approved&#x60;, &#x60;denied&#x60;, &#x60;requested&#x60;). | [optional] 
**last_changed** | **str** | The date and time the status was last changed, formatted as &#x60;YYYY-MM-DD HH:MM:SS&#x60; in the company timezone. | [optional] 
**last_changed_by_user_id** | **int** | The user ID who last changed the status. | [optional] 

## Example

```python
from bamboohr_sdk.models.created_time_off_request_status import CreatedTimeOffRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedTimeOffRequestStatus from a JSON string
created_time_off_request_status_instance = CreatedTimeOffRequestStatus.from_json(json)
# print the JSON string representation of the object
print(CreatedTimeOffRequestStatus.to_json())

# convert the object into a dict
created_time_off_request_status_dict = created_time_off_request_status_instance.to_dict()
# create an instance of CreatedTimeOffRequestStatus from a dict
created_time_off_request_status_from_dict = CreatedTimeOffRequestStatus.from_dict(created_time_off_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


