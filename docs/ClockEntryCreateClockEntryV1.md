# ClockEntryCreateClockEntryV1

Request body for manually creating a time tracking clock entry (corrections, retroactive entry). `timesheetId` and `date` are derived server-side from `start` + `timezone`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | The employee the clock entry belongs to. | 
**start** | **datetime** | Clock-in timestamp (ISO 8601). | 
**end** | **datetime** | Clock-out timestamp (ISO 8601). Must be after start. | 
**timezone** | **str** | IANA timezone identifier the times are recorded under. | 
**note** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 
**clock_in_location** | [**ClockEntryClockEntryLocationInputV1**](ClockEntryClockEntryLocationInputV1.md) | Geolocation captured at clock-in. | [optional] 
**clock_out_location** | [**ClockEntryClockEntryLocationInputV1**](ClockEntryClockEntryLocationInputV1.md) | Geolocation captured at clock-out. | [optional] 

## Example

```python
from bamboohr_sdk.models.clock_entry_create_clock_entry_v1 import ClockEntryCreateClockEntryV1

# TODO update the JSON string below
json = "{}"
# create an instance of ClockEntryCreateClockEntryV1 from a JSON string
clock_entry_create_clock_entry_v1_instance = ClockEntryCreateClockEntryV1.from_json(json)
# print the JSON string representation of the object
print(ClockEntryCreateClockEntryV1.to_json())

# convert the object into a dict
clock_entry_create_clock_entry_v1_dict = clock_entry_create_clock_entry_v1_instance.to_dict()
# create an instance of ClockEntryCreateClockEntryV1 from a dict
clock_entry_create_clock_entry_v1_from_dict = ClockEntryCreateClockEntryV1.from_dict(clock_entry_create_clock_entry_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


