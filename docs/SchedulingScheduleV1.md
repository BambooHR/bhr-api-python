# SchedulingScheduleV1

A shift schedule for a specific location, which organizes shifts for employees

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The UUID of the schedule | [optional] [readonly] 
**name** | **str** | The name of the schedule | [optional] 
**location_id** | **int** | The ID of the location the schedule belongs to | [optional] 
**timezone** | **str** | The timezone of the schedule, provide if location is missing timezone | [optional] 
**start_of_week** | **str** | The starting day of the week for the schedule | [optional] 
**early_clock_in_threshold** | **int** | The threshold (in minutes) that an employee is allowed to clock in early to a shift on this schedule | [optional] 
**manager_user_ids** | **List[int]** | What users manage this schedule | [optional] 
**employee_ids** | **List[int]** | What employees are assigned to this schedule | [optional] 
**created_at** | **datetime** | UTC timestamp when the schedule was created | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.scheduling_schedule_v1 import SchedulingScheduleV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingScheduleV1 from a JSON string
scheduling_schedule_v1_instance = SchedulingScheduleV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingScheduleV1.to_json())

# convert the object into a dict
scheduling_schedule_v1_dict = scheduling_schedule_v1_instance.to_dict()
# create an instance of SchedulingScheduleV1 from a dict
scheduling_schedule_v1_from_dict = SchedulingScheduleV1.from_dict(scheduling_schedule_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


