# TimeTrackingCreateTimeTrackingConfigurationV1

Request body for creating a GROUP time tracking configuration. The GLOBAL configuration is auto-managed and cannot be created here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The configuration name. Unique per company. | 
**timesheet_type** | **str** | How time is logged. | 
**work_week_starts_on** | **str** | Day of week the work week starts. | 
**approver_type** | **str** | Who approves timesheets. | 
**approver_user_id** | **int** |  | [optional] 
**approval_cutoff** | **str** | Time of day by which timesheets must be approved, in 24-hour HH:MM format. | 
**approval_cutoff_days** | **int** | Number of days before the pay date the cutoff applies. | 
**clock_in_schedule_policy** | **str** | When scheduled employees can clock in. | [optional] [default to 'ANYTIME']
**restrict_web_clock_actions** | **bool** | When true, removes the time clock from bamboohr.com for employees in this configuration. | [optional] [default to False]
**mobile_enabled** | **bool** | When true, employees can log time using the BambooHR mobile app. | [optional] [default to False]
**geolocation_enabled** | **bool** | When true, employee location is required when clocking in/out via mobile. Stored but has no effect while mobileEnabled is false. | [optional] [default to False]
**custom_overtime_enabled** | **bool** | When true, the overtime threshold fields are honored. When false, they must be omitted. | [optional] [default to False]
**overtime_daily_hours** | **str** |  | [optional] 
**overtime_daily_double_hours** | **str** |  | [optional] 
**overtime_weekly_hours** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_create_time_tracking_configuration_v1 import TimeTrackingCreateTimeTrackingConfigurationV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingCreateTimeTrackingConfigurationV1 from a JSON string
time_tracking_create_time_tracking_configuration_v1_instance = TimeTrackingCreateTimeTrackingConfigurationV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingCreateTimeTrackingConfigurationV1.to_json())

# convert the object into a dict
time_tracking_create_time_tracking_configuration_v1_dict = time_tracking_create_time_tracking_configuration_v1_instance.to_dict()
# create an instance of TimeTrackingCreateTimeTrackingConfigurationV1 from a dict
time_tracking_create_time_tracking_configuration_v1_from_dict = TimeTrackingCreateTimeTrackingConfigurationV1.from_dict(time_tracking_create_time_tracking_configuration_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


