# TimeTrackingUpdateTimeTrackingBreakV1

Data contract for partially updating a break. All fields are optional; only fields present in the request body will be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the break | [optional] 
**policy_id** | **str** | The unique identifier of the break policy this break belongs to | [optional] 
**paid** | **bool** | Whether the break is paid | [optional] 
**duration** | **int** | Duration of the break in minutes | [optional] 
**availability_type** | **str** | When the break is available to be taken | [optional] 
**availability_min_hours_worked** | **float** | Minimum hours that must be worked before the break can be taken | [optional] 
**availability_max_hours_worked** | **float** | Maximum hours that can be worked before the break must be taken | [optional] 
**availability_start_time** | **str** | Earliest time the break can be taken (HH:MM format) | [optional] 
**availability_end_time** | **str** | Latest time the break can be taken (HH:MM format) | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_update_time_tracking_break_v1 import TimeTrackingUpdateTimeTrackingBreakV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingUpdateTimeTrackingBreakV1 from a JSON string
time_tracking_update_time_tracking_break_v1_instance = TimeTrackingUpdateTimeTrackingBreakV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingUpdateTimeTrackingBreakV1.to_json())

# convert the object into a dict
time_tracking_update_time_tracking_break_v1_dict = time_tracking_update_time_tracking_break_v1_instance.to_dict()
# create an instance of TimeTrackingUpdateTimeTrackingBreakV1 from a dict
time_tracking_update_time_tracking_break_v1_from_dict = TimeTrackingUpdateTimeTrackingBreakV1.from_dict(time_tracking_update_time_tracking_break_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


