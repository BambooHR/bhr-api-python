# SchedulingUpdateSchedulingShiftRequestV1

Fields for updating a scheduling shift. All fields are optional, and only provided fields will be updated. recurrenceEditOption is required when the shift already has recurrence settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**color** | **str** | 6 character color hex code. | [optional] 
**capacity** | **int** |  | [optional] 
**start** | **datetime** | UTC timestamp of the start of the shift. | [optional] 
**end** | **datetime** | UTC timestamp of the end of the shift. | [optional] 
**timezone** | **str** | The timezone for the shift. | [optional] 
**recurrence_rule** | **str** |  | [optional] 
**recurrence_edit_option** | **str** | How should recurrence edits be effective? Edits will not affect any realized shifts regardless of option. | [optional] 
**recurrence_dtstart** | **datetime** |  | [optional] 
**recurrence_dtend** | **datetime** |  | [optional] 
**recurrence_until** | **datetime** |  | [optional] 
**employee_ids** | **List[int]** | What employees are assigned to this shift? | [optional] 
**unpublished_changes** | **object** | The pending changes that have not been published. Only accepts null to clear unpublished changes. | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_update_scheduling_shift_request_v1 import SchedulingUpdateSchedulingShiftRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingUpdateSchedulingShiftRequestV1 from a JSON string
scheduling_update_scheduling_shift_request_v1_instance = SchedulingUpdateSchedulingShiftRequestV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingUpdateSchedulingShiftRequestV1.to_json())

# convert the object into a dict
scheduling_update_scheduling_shift_request_v1_dict = scheduling_update_scheduling_shift_request_v1_instance.to_dict()
# create an instance of SchedulingUpdateSchedulingShiftRequestV1 from a dict
scheduling_update_scheduling_shift_request_v1_from_dict = SchedulingUpdateSchedulingShiftRequestV1.from_dict(scheduling_update_scheduling_shift_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


