# ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1

Request body for partially updating a time tracking shift differential. At least one property must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**rate** | **str** | Non-negative decimal string with at most two decimal places. | [optional] 
**rate_type** | **str** |  | [optional] 
**allow_all_employees** | **bool** | If true, every time-tracked employee is assigned. Ignored when &#x60;employeeIds&#x60; is provided. | [optional] 
**employee_ids** | **List[int]** | Specific internal employee IDs to assign. Minimum 1 entry required when provided. Takes precedence over &#x60;allowAllEmployees&#x60;. | [optional] 
**times** | [**List[ShiftDifferentialCreateTimeTrackingShiftDifferentialV1TimesInner]**](ShiftDifferentialCreateTimeTrackingShiftDifferentialV1TimesInner.md) | Time windows when this differential applies. Replaces all existing time windows when provided. | [optional] 
**archived** | **bool** | When true, archives the shift differential. When false, unarchives it. | [optional] 

## Example

```python
from bamboohr_sdk.models.shift_differential_update_time_tracking_shift_differential_v1 import ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1 from a JSON string
shift_differential_update_time_tracking_shift_differential_v1_instance = ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1.from_json(json)
# print the JSON string representation of the object
print(ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1.to_json())

# convert the object into a dict
shift_differential_update_time_tracking_shift_differential_v1_dict = shift_differential_update_time_tracking_shift_differential_v1_instance.to_dict()
# create an instance of ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1 from a dict
shift_differential_update_time_tracking_shift_differential_v1_from_dict = ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1.from_dict(shift_differential_update_time_tracking_shift_differential_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


