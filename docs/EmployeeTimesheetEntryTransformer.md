# EmployeeTimesheetEntryTransformer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Timesheet entry ID | [optional] 
**employee_id** | **int** | Employee ID | [optional] 
**type** | **str** | Entry type | [optional] 
**var_date** | **date** | Date of the timesheet | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**timezone** | **str** |  | [optional] 
**hours** | **float** |  | [optional] 
**note** | **str** |  | [optional] 
**project_info** | [**ProjectInfoApiTransformer**](ProjectInfoApiTransformer.md) |  | [optional] 
**approved_at** | **datetime** |  | [optional] 
**approved** | **bool** | Whether the timesheet entry is approved | [optional] 
**created_at** | **datetime** | Created time | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_timesheet_entry_transformer import EmployeeTimesheetEntryTransformer

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTimesheetEntryTransformer from a JSON string
employee_timesheet_entry_transformer_instance = EmployeeTimesheetEntryTransformer.from_json(json)
# print the JSON string representation of the object
print(EmployeeTimesheetEntryTransformer.to_json())

# convert the object into a dict
employee_timesheet_entry_transformer_dict = employee_timesheet_entry_transformer_instance.to_dict()
# create an instance of EmployeeTimesheetEntryTransformer from a dict
employee_timesheet_entry_transformer_from_dict = EmployeeTimesheetEntryTransformer.from_dict(employee_timesheet_entry_transformer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


