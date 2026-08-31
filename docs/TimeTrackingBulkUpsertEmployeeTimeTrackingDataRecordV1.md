# TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1

One record of a bulk employee enrollment upsert. `employeeId` is required; the remaining properties carry the same semantics as the single-employee PATCH.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | The employee the record applies to. | 
**enabled** | **bool** | True to enable time tracking for the employee, false to disable it. Disabling retains the enrollment record for history. | [optional] 
**configuration_id** | **int** |  | [optional] 
**enabled_on** | **date** | Effective date for the enable, in YYYY-MM-DD format. Only honored while enabled is being set to true; defaults to today. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_bulk_upsert_employee_time_tracking_data_record_v1 import TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1 from a JSON string
time_tracking_bulk_upsert_employee_time_tracking_data_record_v1_instance = TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1.to_json())

# convert the object into a dict
time_tracking_bulk_upsert_employee_time_tracking_data_record_v1_dict = time_tracking_bulk_upsert_employee_time_tracking_data_record_v1_instance.to_dict()
# create an instance of TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1 from a dict
time_tracking_bulk_upsert_employee_time_tracking_data_record_v1_from_dict = TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1.from_dict(time_tracking_bulk_upsert_employee_time_tracking_data_record_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


