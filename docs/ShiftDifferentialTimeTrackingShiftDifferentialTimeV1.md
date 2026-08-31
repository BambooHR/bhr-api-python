# ShiftDifferentialTimeTrackingShiftDifferentialTimeV1

A time window when a shift differential pay rate applies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the time window. | [optional] [readonly] 
**start_day** | **str** | Start day of the time window. | [optional] 
**end_day** | **str** | End day of the time window. | [optional] 
**start** | **str** | Start time in HH:MM format (24-hour). | [optional] 
**end** | **str** | End time in HH:MM format (24-hour). | [optional] 

## Example

```python
from bamboohr_sdk.models.shift_differential_time_tracking_shift_differential_time_v1 import ShiftDifferentialTimeTrackingShiftDifferentialTimeV1

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftDifferentialTimeTrackingShiftDifferentialTimeV1 from a JSON string
shift_differential_time_tracking_shift_differential_time_v1_instance = ShiftDifferentialTimeTrackingShiftDifferentialTimeV1.from_json(json)
# print the JSON string representation of the object
print(ShiftDifferentialTimeTrackingShiftDifferentialTimeV1.to_json())

# convert the object into a dict
shift_differential_time_tracking_shift_differential_time_v1_dict = shift_differential_time_tracking_shift_differential_time_v1_instance.to_dict()
# create an instance of ShiftDifferentialTimeTrackingShiftDifferentialTimeV1 from a dict
shift_differential_time_tracking_shift_differential_time_v1_from_dict = ShiftDifferentialTimeTrackingShiftDifferentialTimeV1.from_dict(shift_differential_time_tracking_shift_differential_time_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


