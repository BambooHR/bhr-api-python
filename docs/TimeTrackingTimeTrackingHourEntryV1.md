# TimeTrackingTimeTrackingHourEntryV1

A time tracking hour entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The hour entry ID. | [optional] [readonly] 
**employee_id** | **int** | The employee ID. | [optional] 
**timesheet_id** | **int** | The parent timesheet ID. | [optional] 
**var_date** | **date** | The date of the hour entry. | [optional] 
**hours** | **float** | Hours worked. | [optional] 
**note** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 
**created_at** | **datetime** | When the hour entry was created. | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_hour_entry_v1 import TimeTrackingTimeTrackingHourEntryV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingHourEntryV1 from a JSON string
time_tracking_time_tracking_hour_entry_v1_instance = TimeTrackingTimeTrackingHourEntryV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingHourEntryV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_hour_entry_v1_dict = time_tracking_time_tracking_hour_entry_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingHourEntryV1 from a dict
time_tracking_time_tracking_hour_entry_v1_from_dict = TimeTrackingTimeTrackingHourEntryV1.from_dict(time_tracking_time_tracking_hour_entry_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


