# SchedulingCreateSchedulingShiftRequestV1

Fields required to create a scheduling shift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** | The ID of the schedule the shift belongs to. | 
**name** | **str** |  | [optional] 
**status** | **str** | The status of the shift. | 
**color** | **str** | 6 character color hex code. | 
**timezone** | **object** |  | 
**capacity** | **int** |  | [optional] 
**employee_ids** | **List[Optional[int]]** | What employees are assigned to this shift? | [optional] [default to []]
**start** | **datetime** | UTC timestamp of the start of the shift. | 
**end** | **datetime** | UTC timestamp of the end of the shift. | 
**recurrence_rule** | **str** |  | [optional] 
**recurrence_dtstart** | **str** |  | [optional] 
**recurrence_dtend** | **str** |  | [optional] 
**recurrence_until** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_create_scheduling_shift_request_v1 import SchedulingCreateSchedulingShiftRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingCreateSchedulingShiftRequestV1 from a JSON string
scheduling_create_scheduling_shift_request_v1_instance = SchedulingCreateSchedulingShiftRequestV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingCreateSchedulingShiftRequestV1.to_json())

# convert the object into a dict
scheduling_create_scheduling_shift_request_v1_dict = scheduling_create_scheduling_shift_request_v1_instance.to_dict()
# create an instance of SchedulingCreateSchedulingShiftRequestV1 from a dict
scheduling_create_scheduling_shift_request_v1_from_dict = SchedulingCreateSchedulingShiftRequestV1.from_dict(scheduling_create_scheduling_shift_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


