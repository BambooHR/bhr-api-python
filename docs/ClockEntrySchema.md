# ClockEntrySchema

Schema for a single clock entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Unique identifier for the employee. | 
**var_date** | **date** | Date for the timesheet entry. Must be in YYYY-MM-DD format. | 
**start** | **str** | Start time for the timesheet entry. Local time for the employee. Must be in hh:mm 24 hour format. | 
**end** | **str** | End time for the timesheet entry. Local time for the employee. Must be in hh:mm 24 hour format. | 
**id** | **int** | The ID of an existing timesheet entry. This can be specified to edit an existing entry. | [optional] 
**project_id** | **int** | The ID of the project to associate with the timesheet entry. | [optional] 
**task_id** | **int** | The ID of the task to associate with the timesheet entry. | [optional] 
**note** | **str** | Optional note to associate with the timesheet entry. | [optional] 
**break_id** | **str** | Optional break id to associate with the timesheet entry. | [optional] 

## Example

```python
from bamboohr_sdk.models.clock_entry_schema import ClockEntrySchema

# TODO update the JSON string below
json = "{}"
# create an instance of ClockEntrySchema from a JSON string
clock_entry_schema_instance = ClockEntrySchema.from_json(json)
# print the JSON string representation of the object
print(ClockEntrySchema.to_json())

# convert the object into a dict
clock_entry_schema_dict = clock_entry_schema_instance.to_dict()
# create an instance of ClockEntrySchema from a dict
clock_entry_schema_from_dict = ClockEntrySchema.from_dict(clock_entry_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


