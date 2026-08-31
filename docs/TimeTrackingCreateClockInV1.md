# TimeTrackingCreateClockInV1

Request body for the clock-in process resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | The employee to clock in. | 
**timezone** | **str** | IANA timezone name for the clock-in. | 
**clock_in_location** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_create_clock_in_v1 import TimeTrackingCreateClockInV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingCreateClockInV1 from a JSON string
time_tracking_create_clock_in_v1_instance = TimeTrackingCreateClockInV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingCreateClockInV1.to_json())

# convert the object into a dict
time_tracking_create_clock_in_v1_dict = time_tracking_create_clock_in_v1_instance.to_dict()
# create an instance of TimeTrackingCreateClockInV1 from a dict
time_tracking_create_clock_in_v1_from_dict = TimeTrackingCreateClockInV1.from_dict(time_tracking_create_clock_in_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


