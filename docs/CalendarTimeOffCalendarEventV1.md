# CalendarTimeOffCalendarEventV1

An approved time off request shown on the calendar. Pending, denied, and cancelled requests are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The time off request id. | 
**type** | **str** | Event type discriminator. | 
**start** | **date** | Inclusive first day of the time off (YYYY-MM-DD). | 
**end** | **date** | Inclusive last day of the time off (YYYY-MM-DD). Same as start for single-day requests. | 
**employee_id** | **int** | The employee taking time off. | 
**time_off_type_id** | **int** |  | 

## Example

```python
from bamboohr_sdk.models.calendar_time_off_calendar_event_v1 import CalendarTimeOffCalendarEventV1

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarTimeOffCalendarEventV1 from a JSON string
calendar_time_off_calendar_event_v1_instance = CalendarTimeOffCalendarEventV1.from_json(json)
# print the JSON string representation of the object
print(CalendarTimeOffCalendarEventV1.to_json())

# convert the object into a dict
calendar_time_off_calendar_event_v1_dict = calendar_time_off_calendar_event_v1_instance.to_dict()
# create an instance of CalendarTimeOffCalendarEventV1 from a dict
calendar_time_off_calendar_event_v1_from_dict = CalendarTimeOffCalendarEventV1.from_dict(calendar_time_off_calendar_event_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


