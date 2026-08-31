# TimeTrackingHourEntryV1

A date and number of hours worked, rolled up to a timesheet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identifier for the hour entry. | [optional] 
**employee_id** | **int** | The employee who owns the entry. | [optional] 
**timesheet_id** | **int** | The timesheet (pay period) this entry rolls up to. | [optional] 
**var_date** | **date** | Calendar date the hours are attributed to. | [optional] 
**hours** | **float** | Hours worked on this date for the given project/task. | [optional] 
**note** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 
**created_at** | **datetime** | When the entry was created. | [optional] 
**updated_at** | **datetime** | When the entry was last modified. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_hour_entry_v1 import TimeTrackingHourEntryV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingHourEntryV1 from a JSON string
time_tracking_hour_entry_v1_instance = TimeTrackingHourEntryV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingHourEntryV1.to_json())

# convert the object into a dict
time_tracking_hour_entry_v1_dict = time_tracking_hour_entry_v1_instance.to_dict()
# create an instance of TimeTrackingHourEntryV1 from a dict
time_tracking_hour_entry_v1_from_dict = TimeTrackingHourEntryV1.from_dict(time_tracking_hour_entry_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


