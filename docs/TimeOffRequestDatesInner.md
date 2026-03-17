# TimeOffRequestDatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ymd** | **date** | Date in YYYY-MM-DD format. | [optional] 
**amount** | **float** | Hours or days for this date. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request_dates_inner import TimeOffRequestDatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequestDatesInner from a JSON string
time_off_request_dates_inner_instance = TimeOffRequestDatesInner.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequestDatesInner.to_json())

# convert the object into a dict
time_off_request_dates_inner_dict = time_off_request_dates_inner_instance.to_dict()
# create an instance of TimeOffRequestDatesInner from a dict
time_off_request_dates_inner_from_dict = TimeOffRequestDatesInner.from_dict(time_off_request_dates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


