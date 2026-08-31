# CalendarCalendarEventsListResponseV1DataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deterministic synthetic id in the form anniversary-{employeeId}-{year}, where year is the year of this occurrence. | 
**type** | **str** | Event type discriminator. | 
**start** | **date** | The day of the anniversary occurrence (YYYY-MM-DD). | 
**end** | **date** | Same as start; anniversary events are single-day. | 
**employee_id** | **int** | The employee whose anniversary it is. | 
**time_off_type_id** | **int** |  | 
**name** | **str** | The holiday name. | 
**years** | **int** | The number of years being celebrated. | 

## Example

```python
from bamboohr_sdk.models.calendar_calendar_events_list_response_v1_data_inner import CalendarCalendarEventsListResponseV1DataInner

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarCalendarEventsListResponseV1DataInner from a JSON string
calendar_calendar_events_list_response_v1_data_inner_instance = CalendarCalendarEventsListResponseV1DataInner.from_json(json)
# print the JSON string representation of the object
print(CalendarCalendarEventsListResponseV1DataInner.to_json())

# convert the object into a dict
calendar_calendar_events_list_response_v1_data_inner_dict = calendar_calendar_events_list_response_v1_data_inner_instance.to_dict()
# create an instance of CalendarCalendarEventsListResponseV1DataInner from a dict
calendar_calendar_events_list_response_v1_data_inner_from_dict = CalendarCalendarEventsListResponseV1DataInner.from_dict(calendar_calendar_events_list_response_v1_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


