# ClockEntryClockEntryLocationInputV1

Geolocation captured for a clock action. Persisted only when the configuration has geolocation enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude in decimal degrees. | 
**longitude** | **float** | Longitude in decimal degrees. | 
**accuracy** | **float** |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.clock_entry_clock_entry_location_input_v1 import ClockEntryClockEntryLocationInputV1

# TODO update the JSON string below
json = "{}"
# create an instance of ClockEntryClockEntryLocationInputV1 from a JSON string
clock_entry_clock_entry_location_input_v1_instance = ClockEntryClockEntryLocationInputV1.from_json(json)
# print the JSON string representation of the object
print(ClockEntryClockEntryLocationInputV1.to_json())

# convert the object into a dict
clock_entry_clock_entry_location_input_v1_dict = clock_entry_clock_entry_location_input_v1_instance.to_dict()
# create an instance of ClockEntryClockEntryLocationInputV1 from a dict
clock_entry_clock_entry_location_input_v1_from_dict = ClockEntryClockEntryLocationInputV1.from_dict(clock_entry_clock_entry_location_input_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


