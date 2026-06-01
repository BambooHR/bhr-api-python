# SchedulingUpdateScheduleRequestV1

Request object for updating a schedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the schedule | [optional] 
**location_id** | **int** | The ID of the location the schedule belongs to | [optional] 
**timezone** | **str** | The timezone of the schedule. Required if location does not have a timezone. Error if location already has a timezone. | [optional] 
**start_of_week** | **str** | The starting day of the week for the schedule | [optional] 
**early_clock_in_threshold** | **int** | The threshold (in minutes) that an employee is allowed to clock in early to a shift on this schedule | [optional] 
**manager_user_ids** | **List[int]** | User IDs of managers for this schedule | [optional] 
**employee_ids** | **List[int]** | Employee IDs assigned to this schedule | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_update_schedule_request_v1 import SchedulingUpdateScheduleRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingUpdateScheduleRequestV1 from a JSON string
scheduling_update_schedule_request_v1_instance = SchedulingUpdateScheduleRequestV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingUpdateScheduleRequestV1.to_json())

# convert the object into a dict
scheduling_update_schedule_request_v1_dict = scheduling_update_schedule_request_v1_instance.to_dict()
# create an instance of SchedulingUpdateScheduleRequestV1 from a dict
scheduling_update_schedule_request_v1_from_dict = SchedulingUpdateScheduleRequestV1.from_dict(scheduling_update_schedule_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


