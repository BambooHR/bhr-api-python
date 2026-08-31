# TimeTrackingClockEntryLocationV1

Geolocation captured for a clock action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude in decimal degrees. | [optional] 
**longitude** | **float** | Longitude in decimal degrees. | [optional] 
**accuracy** | **float** |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_clock_entry_location_v1 import TimeTrackingClockEntryLocationV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingClockEntryLocationV1 from a JSON string
time_tracking_clock_entry_location_v1_instance = TimeTrackingClockEntryLocationV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingClockEntryLocationV1.to_json())

# convert the object into a dict
time_tracking_clock_entry_location_v1_dict = time_tracking_clock_entry_location_v1_instance.to_dict()
# create an instance of TimeTrackingClockEntryLocationV1 from a dict
time_tracking_clock_entry_location_v1_from_dict = TimeTrackingClockEntryLocationV1.from_dict(time_tracking_clock_entry_location_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


