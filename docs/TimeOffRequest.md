# TimeOffRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The initial status of the request. | 
**start** | **date** | Start date in YYYY-MM-DD format. | 
**end** | **date** | End date in YYYY-MM-DD format. Must be on or after the start date. | 
**time_off_type_id** | **int** | The ID of the time off type for this request. | 
**amount** | **float** | Total hours or days requested. Ignored when &#x60;dates&#x60; array is provided (sum of daily amounts is used instead). | [optional] 
**previous_request** | **int** | The ID of a previous time off request to supersede. The previous request will be cancelled. | [optional] 
**notes** | [**List[TimeOffRequestNotesInner]**](TimeOffRequestNotesInner.md) | Optional notes from the employee or manager. | [optional] 
**dates** | [**List[TimeOffRequestDatesInner]**](TimeOffRequestDatesInner.md) | Optional per-day breakdown. When provided, the top-level &#x60;amount&#x60; is ignored and the sum of daily amounts is used. | [optional] 

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


