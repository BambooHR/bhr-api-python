# TimeTrackingTimeTrackingTimeClockV1

A time tracking time clock. A time clock is a physical device employees use to clock in and out.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the time clock. | [optional] [readonly] 
**name** | **str** | The name of the time clock. | [optional] 
**serial_number** | **str** | The manufacturer serial number of the device. | [optional] [readonly] 
**type** | **str** | The hardware model of the time clock. | [optional] [readonly] 
**online** | **bool** |  | [optional] [readonly] 
**config_online** | **bool** |  | [optional] [readonly] 
**data_online** | **bool** |  | [optional] [readonly] 
**firmware_online** | **bool** |  | [optional] [readonly] 
**timezone** | **str** | IANA timezone name the device records clock entries in. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_time_clock_v1 import TimeTrackingTimeTrackingTimeClockV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingTimeClockV1 from a JSON string
time_tracking_time_tracking_time_clock_v1_instance = TimeTrackingTimeTrackingTimeClockV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingTimeClockV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_time_clock_v1_dict = time_tracking_time_tracking_time_clock_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingTimeClockV1 from a dict
time_tracking_time_tracking_time_clock_v1_from_dict = TimeTrackingTimeTrackingTimeClockV1.from_dict(time_tracking_time_tracking_time_clock_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


