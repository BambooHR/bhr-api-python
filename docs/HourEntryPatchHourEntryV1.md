# HourEntryPatchHourEntryV1

Request body for partially updating a time tracking hour entry. All fields are optional, but at least one must be provided. employeeId is not mutable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Calendar date the hours are attributed to. Must fall inside an existing pay period for the entry&#39;s employee. | [optional] 
**hours** | **float** | Hours worked on this date. Must be greater than zero. | [optional] 
**note** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.hour_entry_patch_hour_entry_v1 import HourEntryPatchHourEntryV1

# TODO update the JSON string below
json = "{}"
# create an instance of HourEntryPatchHourEntryV1 from a JSON string
hour_entry_patch_hour_entry_v1_instance = HourEntryPatchHourEntryV1.from_json(json)
# print the JSON string representation of the object
print(HourEntryPatchHourEntryV1.to_json())

# convert the object into a dict
hour_entry_patch_hour_entry_v1_dict = hour_entry_patch_hour_entry_v1_instance.to_dict()
# create an instance of HourEntryPatchHourEntryV1 from a dict
hour_entry_patch_hour_entry_v1_from_dict = HourEntryPatchHourEntryV1.from_dict(hour_entry_patch_hour_entry_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


