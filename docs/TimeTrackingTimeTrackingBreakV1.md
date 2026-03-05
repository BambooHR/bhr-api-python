# TimeTrackingTimeTrackingBreakV1

A break for time tracking belonging to a break policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the time tracking break | [optional] [readonly] 
**name** | **str** | The name of the break | [optional] 
**policy_id** | **str** | The unique identifier of the break policy this break belongs to | [optional] 
**paid** | **bool** | Whether the break is paid | [optional] 
**duration** | **int** | Duration of the break in minutes | [optional] 
**availability_type** | **str** | When the break is available to be taken | [optional] 
**availability_min_hours_worked** | **float** | Minimum hours that must be worked before the break can be taken | [optional] 
**availability_max_hours_worked** | **float** | Maximum hours that can be worked before the break must be taken | [optional] 
**availability_start_time** | **str** | Earliest time the break can be taken (HH:MM format) | [optional] 
**availability_end_time** | **str** | Latest time the break can be taken (HH:MM format) | [optional] 
**created_at** | **datetime** | ISO 8601 timestamp when the break was created | [optional] [readonly] 
**updated_at** | **datetime** | ISO 8601 timestamp when the break was last updated | [optional] [readonly] 
**deleted_at** | **datetime** | ISO 8601 timestamp when the break was deleted | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingBreakV1 from a JSON string
time_tracking_time_tracking_break_v1_instance = TimeTrackingTimeTrackingBreakV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingBreakV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_break_v1_dict = time_tracking_time_tracking_break_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingBreakV1 from a dict
time_tracking_time_tracking_break_v1_from_dict = TimeTrackingTimeTrackingBreakV1.from_dict(time_tracking_time_tracking_break_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


