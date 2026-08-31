# CalendarCalendarEventsListResponseV1Links

Pagination links. prev is omitted on the first page; next is omitted on the last page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**CalendarCalendarEventsListResponseV1LinksPrev**](CalendarCalendarEventsListResponseV1LinksPrev.md) |  | [optional] 
**next** | [**CalendarCalendarEventsListResponseV1LinksNext**](CalendarCalendarEventsListResponseV1LinksNext.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.calendar_calendar_events_list_response_v1_links import CalendarCalendarEventsListResponseV1Links

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarCalendarEventsListResponseV1Links from a JSON string
calendar_calendar_events_list_response_v1_links_instance = CalendarCalendarEventsListResponseV1Links.from_json(json)
# print the JSON string representation of the object
print(CalendarCalendarEventsListResponseV1Links.to_json())

# convert the object into a dict
calendar_calendar_events_list_response_v1_links_dict = calendar_calendar_events_list_response_v1_links_instance.to_dict()
# create an instance of CalendarCalendarEventsListResponseV1Links from a dict
calendar_calendar_events_list_response_v1_links_from_dict = CalendarCalendarEventsListResponseV1Links.from_dict(calendar_calendar_events_list_response_v1_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


