# TimeTrackingEmployeeTimeTrackingDataV1

An employee's time tracking enrollment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the enrollment record. | [optional] [readonly] 
**employee_id** | **int** | The ID of the employee. | [optional] 
**configuration_id** | **int** |  | [optional] 
**enabled** | **bool** | Whether the employee is enrolled in time tracking. | [optional] 
**enabled_on** | **date** |  | [optional] 
**timezone** | **str** |  | [optional] [readonly] 
**clock_in_id** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** | ISO 8601 timestamp when the enrollment record was created. | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_employee_time_tracking_data_v1 import TimeTrackingEmployeeTimeTrackingDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingEmployeeTimeTrackingDataV1 from a JSON string
time_tracking_employee_time_tracking_data_v1_instance = TimeTrackingEmployeeTimeTrackingDataV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingEmployeeTimeTrackingDataV1.to_json())

# convert the object into a dict
time_tracking_employee_time_tracking_data_v1_dict = time_tracking_employee_time_tracking_data_v1_instance.to_dict()
# create an instance of TimeTrackingEmployeeTimeTrackingDataV1 from a dict
time_tracking_employee_time_tracking_data_v1_from_dict = TimeTrackingEmployeeTimeTrackingDataV1.from_dict(time_tracking_employee_time_tracking_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


