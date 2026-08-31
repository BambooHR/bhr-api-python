# TimeTrackingTimeTrackingConfigurationV1

A time tracking configuration. Groups of employees with shared time tracking settings are configurations with type GROUP; each company has a single GLOBAL configuration that acts as the default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the configuration. | [optional] [readonly] 
**name** | **str** | The configuration name. Unique per company. | [optional] 
**type** | **str** | The configuration type. Read-only. Exactly one GLOBAL configuration exists per company; all customer-created configurations are GROUP. | [optional] [readonly] 
**timesheet_type** | **str** | How time is logged. | [optional] 
**work_week_starts_on** | **str** | Day of week the work week starts. | [optional] 
**approver_type** | **str** |  | [optional] 
**approver_user_id** | **int** |  | [optional] 
**approval_cutoff** | **str** | Time of day by which timesheets must be approved, in 24-hour HH:MM format. | [optional] 
**approval_cutoff_days** | **int** | Number of days before the pay date the cutoff applies. | [optional] 
**clock_in_schedule_policy** | **str** | When scheduled employees can clock in. | [optional] 
**restrict_web_clock_actions** | **bool** | When true, removes the time clock from bamboohr.com for employees in this configuration. | [optional] 
**mobile_enabled** | **bool** | When true, employees can log time using the BambooHR mobile app. | [optional] 
**geolocation_enabled** | **bool** | When true, employee location is required when clocking in/out via mobile. Only meaningful when mobileEnabled is true. | [optional] 
**custom_overtime_enabled** | **bool** | When false, standard U.S. and Canada overtime rules apply. When true, the daily/weekly overtime fields are honored. | [optional] 
**overtime_daily_hours** | **str** |  | [optional] 
**overtime_daily_double_hours** | **str** |  | [optional] 
**overtime_weekly_hours** | **str** |  | [optional] 
**employee_ids** | **List[int]** | Read-only array of employee IDs currently enrolled in this configuration. | [optional] 
**created_at** | **datetime** | ISO 8601 timestamp when the configuration was created. | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_configuration_v1 import TimeTrackingTimeTrackingConfigurationV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingConfigurationV1 from a JSON string
time_tracking_time_tracking_configuration_v1_instance = TimeTrackingTimeTrackingConfigurationV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingConfigurationV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_configuration_v1_dict = time_tracking_time_tracking_configuration_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingConfigurationV1 from a dict
time_tracking_time_tracking_configuration_v1_from_dict = TimeTrackingTimeTrackingConfigurationV1.from_dict(time_tracking_time_tracking_configuration_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


