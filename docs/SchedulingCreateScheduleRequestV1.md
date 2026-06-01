# SchedulingCreateScheduleRequestV1

Request object for creating or updating a schedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the schedule | 
**location_id** | **int** | The ID of the location the schedule belongs to | 
**timezone** | **str** |  | [optional] 
**start_of_week** | **str** | The starting day of the week for the schedule | 
**early_clock_in_threshold** | **int** | The threshold (in minutes) that an employee is allowed to clock in early to a shift on this schedule | [optional] 
**manager_user_ids** | **List[int]** | User IDs of managers for this schedule | [optional] 
**employee_ids** | **List[int]** | Employee IDs assigned to this schedule | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_create_schedule_request_v1 import SchedulingCreateScheduleRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingCreateScheduleRequestV1 from a JSON string
scheduling_create_schedule_request_v1_instance = SchedulingCreateScheduleRequestV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingCreateScheduleRequestV1.to_json())

# convert the object into a dict
scheduling_create_schedule_request_v1_dict = scheduling_create_schedule_request_v1_instance.to_dict()
# create an instance of SchedulingCreateScheduleRequestV1 from a dict
scheduling_create_schedule_request_v1_from_dict = SchedulingCreateScheduleRequestV1.from_dict(scheduling_create_schedule_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


