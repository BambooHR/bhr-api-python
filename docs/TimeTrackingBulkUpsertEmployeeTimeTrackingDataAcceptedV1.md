# TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1

Acknowledgement that a bulk employee enrollment upsert has been accepted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Correlation id for the accepted batch. Returned for log correlation only; there is no status polling endpoint. | 
**message** | **str** | How to confirm the final enrollment state. | 

## Example

```python
from bamboohr_sdk.models.time_tracking_bulk_upsert_employee_time_tracking_data_accepted_v1 import TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1 from a JSON string
time_tracking_bulk_upsert_employee_time_tracking_data_accepted_v1_instance = TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1.to_json())

# convert the object into a dict
time_tracking_bulk_upsert_employee_time_tracking_data_accepted_v1_dict = time_tracking_bulk_upsert_employee_time_tracking_data_accepted_v1_instance.to_dict()
# create an instance of TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1 from a dict
time_tracking_bulk_upsert_employee_time_tracking_data_accepted_v1_from_dict = TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1.from_dict(time_tracking_bulk_upsert_employee_time_tracking_data_accepted_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


