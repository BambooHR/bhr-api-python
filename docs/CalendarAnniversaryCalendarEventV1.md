# CalendarAnniversaryCalendarEventV1

An employee work anniversary occurrence on the calendar.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deterministic synthetic id in the form anniversary-{employeeId}-{year}, where year is the year of this occurrence. | 
**type** | **str** | Event type discriminator. | 
**start** | **date** | The day of the anniversary occurrence (YYYY-MM-DD). | 
**end** | **date** | Same as start; anniversary events are single-day. | 
**employee_id** | **int** | The employee whose anniversary it is. | 
**years** | **int** | The number of years being celebrated. | 

## Example

```python
from bamboohr_sdk.models.calendar_anniversary_calendar_event_v1 import CalendarAnniversaryCalendarEventV1

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarAnniversaryCalendarEventV1 from a JSON string
calendar_anniversary_calendar_event_v1_instance = CalendarAnniversaryCalendarEventV1.from_json(json)
# print the JSON string representation of the object
print(CalendarAnniversaryCalendarEventV1.to_json())

# convert the object into a dict
calendar_anniversary_calendar_event_v1_dict = calendar_anniversary_calendar_event_v1_instance.to_dict()
# create an instance of CalendarAnniversaryCalendarEventV1 from a dict
calendar_anniversary_calendar_event_v1_from_dict = CalendarAnniversaryCalendarEventV1.from_dict(calendar_anniversary_calendar_event_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


