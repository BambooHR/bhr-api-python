# ShiftDifferentialTimeTrackingShiftDifferentialV1

A shift differential rule with time windows and employee assignments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the shift differential. | [optional] [readonly] 
**name** | **str** | The name of the shift differential rule. | [optional] 
**rate** | **str** | The differential pay rate as a decimal string. | [optional] 
**rate_type** | **str** | How the rate is applied. | [optional] 
**allow_all_employees** | **bool** | Whether all time &amp; attendance employees are assigned. | [optional] 
**times** | [**List[ShiftDifferentialTimeTrackingShiftDifferentialTimeV1]**](ShiftDifferentialTimeTrackingShiftDifferentialTimeV1.md) | Time windows when this differential applies. | [optional] 
**employee_ids** | **List[int]** | Employee IDs assigned to this shift differential. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**archived_at** | **datetime** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.shift_differential_time_tracking_shift_differential_v1 import ShiftDifferentialTimeTrackingShiftDifferentialV1

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftDifferentialTimeTrackingShiftDifferentialV1 from a JSON string
shift_differential_time_tracking_shift_differential_v1_instance = ShiftDifferentialTimeTrackingShiftDifferentialV1.from_json(json)
# print the JSON string representation of the object
print(ShiftDifferentialTimeTrackingShiftDifferentialV1.to_json())

# convert the object into a dict
shift_differential_time_tracking_shift_differential_v1_dict = shift_differential_time_tracking_shift_differential_v1_instance.to_dict()
# create an instance of ShiftDifferentialTimeTrackingShiftDifferentialV1 from a dict
shift_differential_time_tracking_shift_differential_v1_from_dict = ShiftDifferentialTimeTrackingShiftDifferentialV1.from_dict(shift_differential_time_tracking_shift_differential_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


