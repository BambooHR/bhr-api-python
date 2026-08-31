# TimesheetTimesheetDailyEntryV1

An aggregated daily time summary for a single calendar date within a timesheet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The calendar date being rolled up. | 
**total_hours** | **float** | Sum of all hours on this day across rate buckets. | 
**regular_hours** | **float** | Hours in the regular (REG) rate bucket. | 
**overtime_hours** | **float** | Hours in the overtime (OT) rate bucket. | 
**double_time_hours** | **float** | Hours in the double-time rate bucket. Always 0.0 when the configuration defines no double-time. | 

## Example

```python
from bamboohr_sdk.models.timesheet_timesheet_daily_entry_v1 import TimesheetTimesheetDailyEntryV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetTimesheetDailyEntryV1 from a JSON string
timesheet_timesheet_daily_entry_v1_instance = TimesheetTimesheetDailyEntryV1.from_json(json)
# print the JSON string representation of the object
print(TimesheetTimesheetDailyEntryV1.to_json())

# convert the object into a dict
timesheet_timesheet_daily_entry_v1_dict = timesheet_timesheet_daily_entry_v1_instance.to_dict()
# create an instance of TimesheetTimesheetDailyEntryV1 from a dict
timesheet_timesheet_daily_entry_v1_from_dict = TimesheetTimesheetDailyEntryV1.from_dict(timesheet_timesheet_daily_entry_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


