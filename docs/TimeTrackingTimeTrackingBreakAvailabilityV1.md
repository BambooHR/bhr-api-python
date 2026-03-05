# TimeTrackingTimeTrackingBreakAvailabilityV1

Break availability information for time tracking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the time tracking break | [optional] [readonly] 
**name** | **str** | The name of the break | [optional] [readonly] 
**policy_id** | **str** | The unique identifier of the break policy this break belongs to | [optional] [readonly] 
**paid** | **bool** | Whether the break is paid | [optional] [readonly] 
**duration** | **int** | Duration of the break in minutes | [optional] [readonly] 
**availability_type** | **str** | When the break is available to be taken | [optional] [readonly] 
**calculated_at** | **datetime** | When the break availability was calculated | [optional] [readonly] 
**effective_at** | **datetime** | Timestamp that all time-based calculations are evaluated relative to. | [optional] [readonly] 
**timezone** | **str** | The timezone the break availability is calculated in | [optional] [readonly] 
**recorded_duration** | **int** | The duration of the break that has been recorded so far | [optional] [readonly] 
**available** | **bool** | Whether the break is currently available to be taken | [optional] [readonly] 
**available_after_minutes_worked** | **int** | Minutes of work after which the break becomes available | [optional] [readonly] 
**available_in** | **int** | Minutes until the break becomes available | [optional] [readonly] 
**unavailable_in** | **int** | Minutes until the break becomes unavailable | [optional] [readonly] 
**available_at** | **datetime** | When the break is or becomes available | [optional] [readonly] 
**unavailable_at** | **datetime** | When the break is or becomes unavailable | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_break_availability_v1 import TimeTrackingTimeTrackingBreakAvailabilityV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingBreakAvailabilityV1 from a JSON string
time_tracking_time_tracking_break_availability_v1_instance = TimeTrackingTimeTrackingBreakAvailabilityV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingBreakAvailabilityV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_break_availability_v1_dict = time_tracking_time_tracking_break_availability_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingBreakAvailabilityV1 from a dict
time_tracking_time_tracking_break_availability_v1_from_dict = TimeTrackingTimeTrackingBreakAvailabilityV1.from_dict(time_tracking_time_tracking_break_availability_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


