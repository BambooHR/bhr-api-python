# TimeTrackingUpdateClockEntryV1

Request body for a partial update of a clock entry. All fields optional; at least one required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | Updated clock-in timestamp (ISO 8601). | [optional] 
**end** | **datetime** |  | [optional] 
**timezone** | **str** | Updated IANA timezone identifier. | [optional] 
**note** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 
**clock_in_location** | **object** |  | [optional] 
**clock_out_location** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_update_clock_entry_v1 import TimeTrackingUpdateClockEntryV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingUpdateClockEntryV1 from a JSON string
time_tracking_update_clock_entry_v1_instance = TimeTrackingUpdateClockEntryV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingUpdateClockEntryV1.to_json())

# convert the object into a dict
time_tracking_update_clock_entry_v1_dict = time_tracking_update_clock_entry_v1_instance.to_dict()
# create an instance of TimeTrackingUpdateClockEntryV1 from a dict
time_tracking_update_clock_entry_v1_from_dict = TimeTrackingUpdateClockEntryV1.from_dict(time_tracking_update_clock_entry_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


