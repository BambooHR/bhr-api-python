# CalendarCalendarEventPersonV1

Display subset of an employee, embedded under `persons` when includePersons=true.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Employee id. | 
**first_name** | **str** | The employee&#39;s first name. | 
**last_name** | **str** | The employee&#39;s last name. | 
**display_name** | **str** | Preferred display name (preferred name if set, else first and last name). | 
**job_title** | **str** |  | 
**photo_url** | **str** |  | 

## Example

```python
from bamboohr_sdk.models.calendar_calendar_event_person_v1 import CalendarCalendarEventPersonV1

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarCalendarEventPersonV1 from a JSON string
calendar_calendar_event_person_v1_instance = CalendarCalendarEventPersonV1.from_json(json)
# print the JSON string representation of the object
print(CalendarCalendarEventPersonV1.to_json())

# convert the object into a dict
calendar_calendar_event_person_v1_dict = calendar_calendar_event_person_v1_instance.to_dict()
# create an instance of CalendarCalendarEventPersonV1 from a dict
calendar_calendar_event_person_v1_from_dict = CalendarCalendarEventPersonV1.from_dict(calendar_calendar_event_person_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


