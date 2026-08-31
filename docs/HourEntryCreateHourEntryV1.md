# HourEntryCreateHourEntryV1

Request body for creating a time tracking hour entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | The employee who owns the entry. | 
**var_date** | **date** | Calendar date the hours are attributed to. | 
**hours** | **float** | Hours worked on this date. Must be greater than zero. | 
**note** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.hour_entry_create_hour_entry_v1 import HourEntryCreateHourEntryV1

# TODO update the JSON string below
json = "{}"
# create an instance of HourEntryCreateHourEntryV1 from a JSON string
hour_entry_create_hour_entry_v1_instance = HourEntryCreateHourEntryV1.from_json(json)
# print the JSON string representation of the object
print(HourEntryCreateHourEntryV1.to_json())

# convert the object into a dict
hour_entry_create_hour_entry_v1_dict = hour_entry_create_hour_entry_v1_instance.to_dict()
# create an instance of HourEntryCreateHourEntryV1 from a dict
hour_entry_create_hour_entry_v1_from_dict = HourEntryCreateHourEntryV1.from_dict(hour_entry_create_hour_entry_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


