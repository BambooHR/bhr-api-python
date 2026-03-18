# TimeOffHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date for the history item in YYYY-MM-DD format. | 
**event_type** | **str** | The type of history event. Defaults to &#x60;used&#x60; for the /history path and &#x60;override&#x60; for the /balance_adjustment path when omitted. | [optional] 
**time_off_request_id** | **int** | The ID of an approved time off request. Required when eventType is &#x60;used&#x60;. | [optional] 
**time_off_type_id** | **int** | The ID of the time off type. Required when eventType is &#x60;override&#x60;. | [optional] 
**amount** | **float** | The number of hours/days to record. Required when eventType is &#x60;override&#x60;. | [optional] 
**note** | **str** | An optional note to show in history. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_history import TimeOffHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffHistory from a JSON string
time_off_history_instance = TimeOffHistory.from_json(json)
# print the JSON string representation of the object
print(TimeOffHistory.to_json())

# convert the object into a dict
time_off_history_dict = time_off_history_instance.to_dict()
# create an instance of TimeOffHistory from a dict
time_off_history_from_dict = TimeOffHistory.from_dict(time_off_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


