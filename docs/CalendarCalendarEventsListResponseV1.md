# CalendarCalendarEventsListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CalendarCalendarEventsListResponseV1DataInner]**](CalendarCalendarEventsListResponseV1DataInner.md) | Array of calendar event resource objects. | [optional] 
**persons** | [**Dict[str, CalendarCalendarEventPersonV1]**](CalendarCalendarEventPersonV1.md) | Present only when includePersons&#x3D;true. Map keyed by employee id. | [optional] 
**links** | [**CalendarCalendarEventsListResponseV1Links**](CalendarCalendarEventsListResponseV1Links.md) |  | [optional] 
**meta** | [**CalendarCalendarEventsListResponseV1Meta**](CalendarCalendarEventsListResponseV1Meta.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.calendar_calendar_events_list_response_v1 import CalendarCalendarEventsListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarCalendarEventsListResponseV1 from a JSON string
calendar_calendar_events_list_response_v1_instance = CalendarCalendarEventsListResponseV1.from_json(json)
# print the JSON string representation of the object
print(CalendarCalendarEventsListResponseV1.to_json())

# convert the object into a dict
calendar_calendar_events_list_response_v1_dict = calendar_calendar_events_list_response_v1_instance.to_dict()
# create an instance of CalendarCalendarEventsListResponseV1 from a dict
calendar_calendar_events_list_response_v1_from_dict = CalendarCalendarEventsListResponseV1.from_dict(calendar_calendar_events_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


