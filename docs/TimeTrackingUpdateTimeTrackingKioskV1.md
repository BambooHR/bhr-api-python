# TimeTrackingUpdateTimeTrackingKioskV1

JSON Merge Patch body for updating a time tracking kiosk. Only the kiosk name is mutable; all other properties are read-only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the kiosk. Must be unique across active kiosks. | 

## Example

```python
from bamboohr_sdk.models.time_tracking_update_time_tracking_kiosk_v1 import TimeTrackingUpdateTimeTrackingKioskV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingUpdateTimeTrackingKioskV1 from a JSON string
time_tracking_update_time_tracking_kiosk_v1_instance = TimeTrackingUpdateTimeTrackingKioskV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingUpdateTimeTrackingKioskV1.to_json())

# convert the object into a dict
time_tracking_update_time_tracking_kiosk_v1_dict = time_tracking_update_time_tracking_kiosk_v1_instance.to_dict()
# create an instance of TimeTrackingUpdateTimeTrackingKioskV1 from a dict
time_tracking_update_time_tracking_kiosk_v1_from_dict = TimeTrackingUpdateTimeTrackingKioskV1.from_dict(time_tracking_update_time_tracking_kiosk_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


