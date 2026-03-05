# TimeOffRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**time_off_type_id** | **int** |  | [optional] 
**amount** | **int** |  | [optional] 
**notes** | [**List[TimeOffRequestNotesInner]**](TimeOffRequestNotesInner.md) |  | [optional] 
**dates** | [**List[TimeOffRequestDatesInner]**](TimeOffRequestDatesInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request import TimeOffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequest from a JSON string
time_off_request_instance = TimeOffRequest.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequest.to_json())

# convert the object into a dict
time_off_request_dict = time_off_request_instance.to_dict()
# create an instance of TimeOffRequest from a dict
time_off_request_from_dict = TimeOffRequest.from_dict(time_off_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


