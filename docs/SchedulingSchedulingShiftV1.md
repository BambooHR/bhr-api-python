# SchedulingSchedulingShiftV1

A shift for scheduling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the shift. This can be the UUIDv7 of the shift instance, or a composite ID (&lt;recurringShiftDefinitionId&gt;_&lt;recurrenceId&gt;) for uninstantiated recurring shifts. | [readonly] 
**schedule_id** | **str** | The ID of the schedule the shift belongs to. | 
**name** | **str** |  | [optional] 
**status** | **str** | The status of the shift. | 
**color** | **str** | 6 character color hex code. | 
**capacity** | **int** |  | [optional] 
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**timezone** | **str** | The timezone for the shift. | 
**recurrence_rule** | **str** |  | [optional] 
**recurrence_id** | **str** |  | [optional] 
**recurrence_dtstart** | **str** |  | [optional] 
**recurrence_dtend** | **str** |  | [optional] 
**recurrence_until** | **str** |  | [optional] 
**employee_ids** | **List[int]** | The list of employee IDs currently assigned. | [optional] 
**unpublished_changes** | **object** |  | [optional] 
**created_at** | **datetime** | UTC timestamp when the shift was created | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.scheduling_scheduling_shift_v1 import SchedulingSchedulingShiftV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingSchedulingShiftV1 from a JSON string
scheduling_scheduling_shift_v1_instance = SchedulingSchedulingShiftV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingSchedulingShiftV1.to_json())

# convert the object into a dict
scheduling_scheduling_shift_v1_dict = scheduling_scheduling_shift_v1_instance.to_dict()
# create an instance of SchedulingSchedulingShiftV1 from a dict
scheduling_scheduling_shift_v1_from_dict = SchedulingSchedulingShiftV1.from_dict(scheduling_scheduling_shift_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


