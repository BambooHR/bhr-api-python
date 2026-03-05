# TimesheetEntryInfoApiTransformerBreakInfo

Break information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Break ID | [optional] 
**name** | **str** | Break name | [optional] 

## Example

```python
from bamboohr_sdk.models.timesheet_entry_info_api_transformer_break_info import TimesheetEntryInfoApiTransformerBreakInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetEntryInfoApiTransformerBreakInfo from a JSON string
timesheet_entry_info_api_transformer_break_info_instance = TimesheetEntryInfoApiTransformerBreakInfo.from_json(json)
# print the JSON string representation of the object
print(TimesheetEntryInfoApiTransformerBreakInfo.to_json())

# convert the object into a dict
timesheet_entry_info_api_transformer_break_info_dict = timesheet_entry_info_api_transformer_break_info_instance.to_dict()
# create an instance of TimesheetEntryInfoApiTransformerBreakInfo from a dict
timesheet_entry_info_api_transformer_break_info_from_dict = TimesheetEntryInfoApiTransformerBreakInfo.from_dict(timesheet_entry_info_api_transformer_break_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


