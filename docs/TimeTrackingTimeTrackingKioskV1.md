# TimeTrackingTimeTrackingKioskV1

A time tracking kiosk. A kiosk is a shared device employees use to clock in and out.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the time tracking kiosk. | [optional] [readonly] 
**name** | **str** | The name of the kiosk. | [optional] 
**last_used** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_kiosk_v1 import TimeTrackingTimeTrackingKioskV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingKioskV1 from a JSON string
time_tracking_time_tracking_kiosk_v1_instance = TimeTrackingTimeTrackingKioskV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingKioskV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_kiosk_v1_dict = time_tracking_time_tracking_kiosk_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingKioskV1 from a dict
time_tracking_time_tracking_kiosk_v1_from_dict = TimeTrackingTimeTrackingKioskV1.from_dict(time_tracking_time_tracking_kiosk_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


