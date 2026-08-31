# TimeTrackingUpdateTimeTrackingConfigurationV1

JSON Merge Patch body for updating a time tracking configuration. Only the properties present are applied; an explicit null clears a nullable property. The read-only `type` and `employeeIds` properties are rejected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The configuration name. Unique per company. | [optional] 
**timesheet_type** | **str** | How time is logged. | [optional] 
**work_week_starts_on** | **str** | Day of week the work week starts. | [optional] 
**approver_type** | **str** | Who approves timesheets. Moving away from SPECIFIC_PERSON clears approverUserId server-side. | [optional] 
**approver_user_id** | **int** |  | [optional] 
**approval_cutoff** | **str** | Time of day by which timesheets must be approved, in 24-hour HH:MM format. | [optional] 
**approval_cutoff_days** | **int** | Number of days before the pay date the cutoff applies. | [optional] 
**clock_in_schedule_policy** | **str** | When scheduled employees can clock in. | [optional] 
**restrict_web_clock_actions** | **bool** | When true, removes the time clock from bamboohr.com for employees in this configuration. | [optional] 
**mobile_enabled** | **bool** | When true, employees can log time using the BambooHR mobile app. | [optional] 
**geolocation_enabled** | **bool** | When true, employee location is required when clocking in/out via mobile. Stored but has no effect while mobileEnabled is false. | [optional] 
**custom_overtime_enabled** | **bool** | When true, the overtime threshold fields are honored. Setting it to false clears all three thresholds server-side. | [optional] 
**overtime_daily_hours** | **str** |  | [optional] 
**overtime_daily_double_hours** | **str** |  | [optional] 
**overtime_weekly_hours** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_update_time_tracking_configuration_v1 import TimeTrackingUpdateTimeTrackingConfigurationV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingUpdateTimeTrackingConfigurationV1 from a JSON string
time_tracking_update_time_tracking_configuration_v1_instance = TimeTrackingUpdateTimeTrackingConfigurationV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingUpdateTimeTrackingConfigurationV1.to_json())

# convert the object into a dict
time_tracking_update_time_tracking_configuration_v1_dict = time_tracking_update_time_tracking_configuration_v1_instance.to_dict()
# create an instance of TimeTrackingUpdateTimeTrackingConfigurationV1 from a dict
time_tracking_update_time_tracking_configuration_v1_from_dict = TimeTrackingUpdateTimeTrackingConfigurationV1.from_dict(time_tracking_update_time_tracking_configuration_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


