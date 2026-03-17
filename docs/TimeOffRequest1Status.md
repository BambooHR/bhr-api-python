# TimeOffRequest1Status

The current status of the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_changed** | **date** | The date the status was last changed (company timezone). | [optional] 
**last_changed_by_user_id** | **int** | The user ID who last changed the status. | [optional] 
**status** | **str** | The current status value. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request1_status import TimeOffRequest1Status

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequest1Status from a JSON string
time_off_request1_status_instance = TimeOffRequest1Status.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequest1Status.to_json())

# convert the object into a dict
time_off_request1_status_dict = time_off_request1_status_instance.to_dict()
# create an instance of TimeOffRequest1Status from a dict
time_off_request1_status_from_dict = TimeOffRequest1Status.from_dict(time_off_request1_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


