# CalendarCalendarEventsListResponseV1Meta

Pagination metadata. totalItems sums the four event sources within the requested range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_size** | **int** |  | 
**total_pages** | **int** |  | 
**total_items** | **int** |  | 

## Example

```python
from bamboohr_sdk.models.calendar_calendar_events_list_response_v1_meta import CalendarCalendarEventsListResponseV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarCalendarEventsListResponseV1Meta from a JSON string
calendar_calendar_events_list_response_v1_meta_instance = CalendarCalendarEventsListResponseV1Meta.from_json(json)
# print the JSON string representation of the object
print(CalendarCalendarEventsListResponseV1Meta.to_json())

# convert the object into a dict
calendar_calendar_events_list_response_v1_meta_dict = calendar_calendar_events_list_response_v1_meta_instance.to_dict()
# create an instance of CalendarCalendarEventsListResponseV1Meta from a dict
calendar_calendar_events_list_response_v1_meta_from_dict = CalendarCalendarEventsListResponseV1Meta.from_dict(calendar_calendar_events_list_response_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


