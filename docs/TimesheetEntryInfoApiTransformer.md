# TimesheetEntryInfoApiTransformer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Timesheet entry ID | [optional] 
**employee_id** | **int** | Employee ID | [optional] 
**type** | **str** | Entry type | [optional] 
**var_date** | **date** | Date of the timesheet | [optional] 
**start** | **datetime** | Start time | [optional] 
**end** | **datetime** | End time | [optional] 
**timezone** | **str** | Timezone | [optional] 
**hours** | **float** | Hours worked | [optional] 
**note** | **str** | Note | [optional] 
**project_info** | [**ProjectInfoApiTransformer**](ProjectInfoApiTransformer.md) |  | [optional] 
**break_info** | [**TimesheetEntryInfoApiTransformerBreakInfo**](TimesheetEntryInfoApiTransformerBreakInfo.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.timesheet_entry_info_api_transformer import TimesheetEntryInfoApiTransformer

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetEntryInfoApiTransformer from a JSON string
timesheet_entry_info_api_transformer_instance = TimesheetEntryInfoApiTransformer.from_json(json)
# print the JSON string representation of the object
print(TimesheetEntryInfoApiTransformer.to_json())

# convert the object into a dict
timesheet_entry_info_api_transformer_dict = timesheet_entry_info_api_transformer_instance.to_dict()
# create an instance of TimesheetEntryInfoApiTransformer from a dict
timesheet_entry_info_api_transformer_from_dict = TimesheetEntryInfoApiTransformer.from_dict(timesheet_entry_info_api_transformer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


