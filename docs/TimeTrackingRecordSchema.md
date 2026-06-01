# TimeTrackingRecordSchema

Schema for time tracking record response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_tracking_id** | **str** | Unique identifier for the time tracking record | [optional] 
**employee_id** | **str** | ID of the employee associated with this time tracking record | [optional] 
**division_id** | **str** |  | [optional] 
**department_id** | **str** |  | [optional] 
**job_title_id** | **str** |  | [optional] 
**pay_code** | **str** |  | [optional] 
**date_hours_worked** | **date** | Date the hours were worked | [optional] 
**type** | **str** | Type of time tracking record | [optional] 
**pay_rate** | **decimal.Decimal** | Pay rate for this time tracking record | [optional] 
**rate_type** | **str** | Rate type for this time tracking record | [optional] 
**hours_worked** | **decimal.Decimal** | Number of hours worked | [optional] 
**adjusted_hours** | **decimal.Decimal** | Number of adjusted hours | [optional] 
**date_adjusted** | **datetime** | Date and time when the hours were adjusted | [optional] 
**job_code** | **str** |  | [optional] 
**job_data** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**shift_differential_id** | **str** |  | [optional] 
**holiday_id** | **str** |  | [optional] 
**project** | **object** |  | [optional] 
**shift_differential** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_record_schema import TimeTrackingRecordSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingRecordSchema from a JSON string
time_tracking_record_schema_instance = TimeTrackingRecordSchema.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingRecordSchema.to_json())

# convert the object into a dict
time_tracking_record_schema_dict = time_tracking_record_schema_instance.to_dict()
# create an instance of TimeTrackingRecordSchema from a dict
time_tracking_record_schema_from_dict = TimeTrackingRecordSchema.from_dict(time_tracking_record_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


