# TimeTrackingTimesheetV1

A pay period's time data for an employee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identifier for the timesheet. | [optional] 
**employee_id** | **int** | The employee this timesheet belongs to. | [optional] 
**type** | **str** | Tracking method snapshotted from the configuration at period start. | [optional] 
**start_date** | **date** | First date of the pay period (inclusive). | [optional] 
**end_date** | **date** | Last date of the pay period (inclusive). | [optional] 
**status** | **str** | Derived approval state. | [optional] 
**total_hours** | **float** | Sum of all hours across regular, overtime, holiday, and approved PTO. | [optional] 
**overtime_hours** | **float** | Subset of totalHours that falls into the overtime rate bucket. | [optional] 
**approved_by** | **int** |  | [optional] 
**approved_at** | **datetime** |  | [optional] 
**created_at** | **datetime** | When the timesheet record was created. | [optional] 
**updated_at** | **datetime** | When the timesheet was last modified. | [optional] 
**hours_last_changed_at** | **datetime** | When the timesheet&#39;s hours were last changed. Send this value back as the approval request&#39;s &#x60;lastChangedAt&#x60;. Distinct from &#x60;updatedAt&#x60; because hours are stored separately from the timesheet row. | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_timesheet_v1 import TimeTrackingTimesheetV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimesheetV1 from a JSON string
time_tracking_timesheet_v1_instance = TimeTrackingTimesheetV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimesheetV1.to_json())

# convert the object into a dict
time_tracking_timesheet_v1_dict = time_tracking_timesheet_v1_instance.to_dict()
# create an instance of TimeTrackingTimesheetV1 from a dict
time_tracking_timesheet_v1_from_dict = TimeTrackingTimesheetV1.from_dict(time_tracking_timesheet_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


