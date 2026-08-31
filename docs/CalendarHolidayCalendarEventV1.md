# CalendarHolidayCalendarEventV1

A company holiday shown on the calendar. Holiday events are not affected by per-employee filters or directReportsOnly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The company holiday id. | 
**type** | **str** | Event type discriminator. | 
**start** | **date** | Inclusive first day of the holiday (YYYY-MM-DD). | 
**end** | **date** | Inclusive last day of the holiday (YYYY-MM-DD). Same as start for single-day holidays. | 
**name** | **str** | The holiday name. | 

## Example

```python
from bamboohr_sdk.models.calendar_holiday_calendar_event_v1 import CalendarHolidayCalendarEventV1

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarHolidayCalendarEventV1 from a JSON string
calendar_holiday_calendar_event_v1_instance = CalendarHolidayCalendarEventV1.from_json(json)
# print the JSON string representation of the object
print(CalendarHolidayCalendarEventV1.to_json())

# convert the object into a dict
calendar_holiday_calendar_event_v1_dict = calendar_holiday_calendar_event_v1_instance.to_dict()
# create an instance of CalendarHolidayCalendarEventV1 from a dict
calendar_holiday_calendar_event_v1_from_dict = CalendarHolidayCalendarEventV1.from_dict(calendar_holiday_calendar_event_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


