# TimeOffHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | The date the request should be added in history. This will usually be the first date of the request. Should be in ISO8601 date format (YYYY-MM-DD). | 
**time_off_request_id** | **int** | The ID of the time off request. | 
**note** | **str** | This is an optional note to show in history. | [optional] 

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


