# HourEntrySchema

Schema for a single timesheet hour entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Unique identifier for the employee | [optional] 
**var_date** | **date** | Date for the timesheet entry. Must be in YYYY-MM-DD format | [optional] 
**hours** | **float** | Hours worked for this timesheet entry | [optional] 
**id** | **int** | The ID of an existing timesheet entry. This can be specified to edit an existing entry | [optional] 
**project_id** | **int** | The ID of the project to associate with the timesheet entry | [optional] 
**task_id** | **int** | The ID of the task to associate with the timesheet entry | [optional] 
**note** | **str** | Optional note to associate with the timesheet entry | [optional] 

## Example

```python
from bamboohr_sdk.models.hour_entry_schema import HourEntrySchema

# TODO update the JSON string below
json = "{}"
# create an instance of HourEntrySchema from a JSON string
hour_entry_schema_instance = HourEntrySchema.from_json(json)
# print the JSON string representation of the object
print(HourEntrySchema.to_json())

# convert the object into a dict
hour_entry_schema_dict = hour_entry_schema_instance.to_dict()
# create an instance of HourEntrySchema from a dict
hour_entry_schema_from_dict = HourEntrySchema.from_dict(hour_entry_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


