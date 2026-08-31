# TimeTrackingUpdateTimeTrackingTimeClockV1

JSON Merge Patch body for updating a time tracking time clock. Only the `name` and `timezone` properties are mutable, and at least one of them must be provided. Every other property of the time clock is read-only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the time clock. | [optional] 
**timezone** | **str** | IANA timezone name the device records clock entries in. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_update_time_tracking_time_clock_v1 import TimeTrackingUpdateTimeTrackingTimeClockV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingUpdateTimeTrackingTimeClockV1 from a JSON string
time_tracking_update_time_tracking_time_clock_v1_instance = TimeTrackingUpdateTimeTrackingTimeClockV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingUpdateTimeTrackingTimeClockV1.to_json())

# convert the object into a dict
time_tracking_update_time_tracking_time_clock_v1_dict = time_tracking_update_time_tracking_time_clock_v1_instance.to_dict()
# create an instance of TimeTrackingUpdateTimeTrackingTimeClockV1 from a dict
time_tracking_update_time_tracking_time_clock_v1_from_dict = TimeTrackingUpdateTimeTrackingTimeClockV1.from_dict(time_tracking_update_time_tracking_time_clock_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


