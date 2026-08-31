# CalendarBirthdayCalendarEventV1

An employee birthday occurrence on the calendar.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deterministic synthetic id in the form birthday-{employeeId}-{year}, where year is the year of this occurrence. | 
**type** | **str** | Event type discriminator. | 
**start** | **date** | The day of the birthday occurrence (YYYY-MM-DD). | 
**end** | **date** | Same as start; birthday events are single-day. | 
**employee_id** | **int** | The employee whose birthday it is. | 

## Example

```python
from bamboohr_sdk.models.calendar_birthday_calendar_event_v1 import CalendarBirthdayCalendarEventV1

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarBirthdayCalendarEventV1 from a JSON string
calendar_birthday_calendar_event_v1_instance = CalendarBirthdayCalendarEventV1.from_json(json)
# print the JSON string representation of the object
print(CalendarBirthdayCalendarEventV1.to_json())

# convert the object into a dict
calendar_birthday_calendar_event_v1_dict = calendar_birthday_calendar_event_v1_instance.to_dict()
# create an instance of CalendarBirthdayCalendarEventV1 from a dict
calendar_birthday_calendar_event_v1_from_dict = CalendarBirthdayCalendarEventV1.from_dict(calendar_birthday_calendar_event_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


