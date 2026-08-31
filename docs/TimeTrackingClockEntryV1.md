# TimeTrackingClockEntryV1

A clock in/out record with start/end timestamps, timezone, and optional geolocation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identifier for the clock entry. | [optional] 
**employee_id** | **int** | The employee who owns the entry. | [optional] 
**timesheet_id** | **int** | The timesheet (pay period) this entry rolls up to. | [optional] 
**var_date** | **date** | Calendar date the entry is attributed to (in the entry&#39;s timezone). | [optional] 
**start** | **datetime** | Clock-in timestamp, ISO 8601 with the offset of the entry&#39;s timezone. | [optional] 
**end** | **datetime** |  | [optional] 
**timezone** | **str** | IANA timezone name under which start / end were recorded. | [optional] 
**hours** | **float** | Computed elapsed hours between start and end. Zero while the entry is open. | [optional] 
**note** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 
**clock_in_location** | [**TimeTrackingClockEntryLocationV1**](TimeTrackingClockEntryLocationV1.md) | Geolocation captured at clock-in. Null when geolocation is disabled or none was captured. | [optional] 
**clock_out_location** | [**TimeTrackingClockEntryLocationV1**](TimeTrackingClockEntryLocationV1.md) | Geolocation captured at clock-out. Null while the entry is open or when geolocation is disabled. | [optional] 
**scheduling_shift_id** | **str** |  | [optional] 
**start_source** | **str** |  | [optional] 
**end_source** | **str** |  | [optional] 
**clocked_in_by** | **int** |  | [optional] 
**clocked_out_by** | **int** |  | [optional] 
**created_at** | **datetime** | When the entry was created. | [optional] 
**updated_at** | **datetime** | When the entry was last modified. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_clock_entry_v1 import TimeTrackingClockEntryV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingClockEntryV1 from a JSON string
time_tracking_clock_entry_v1_instance = TimeTrackingClockEntryV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingClockEntryV1.to_json())

# convert the object into a dict
time_tracking_clock_entry_v1_dict = time_tracking_clock_entry_v1_instance.to_dict()
# create an instance of TimeTrackingClockEntryV1 from a dict
time_tracking_clock_entry_v1_from_dict = TimeTrackingClockEntryV1.from_dict(time_tracking_clock_entry_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


