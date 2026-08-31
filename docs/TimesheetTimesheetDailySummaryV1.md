# TimesheetTimesheetDailySummaryV1

Daily breakdown of a timesheet, partitioned by rate bucket, covering every date in the pay period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timesheet_id** | **int** | Identifier for the timesheet. | 
**daily_entries** | [**List[TimesheetTimesheetDailyEntryV1]**](TimesheetTimesheetDailyEntryV1.md) | Daily entries covering every date in the pay period (inclusive), ordered ascending. | 

## Example

```python
from bamboohr_sdk.models.timesheet_timesheet_daily_summary_v1 import TimesheetTimesheetDailySummaryV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetTimesheetDailySummaryV1 from a JSON string
timesheet_timesheet_daily_summary_v1_instance = TimesheetTimesheetDailySummaryV1.from_json(json)
# print the JSON string representation of the object
print(TimesheetTimesheetDailySummaryV1.to_json())

# convert the object into a dict
timesheet_timesheet_daily_summary_v1_dict = timesheet_timesheet_daily_summary_v1_instance.to_dict()
# create an instance of TimesheetTimesheetDailySummaryV1 from a dict
timesheet_timesheet_daily_summary_v1_from_dict = TimesheetTimesheetDailySummaryV1.from_dict(timesheet_timesheet_daily_summary_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


