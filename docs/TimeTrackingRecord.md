# TimeTrackingRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_tracking_id** | **str** | A unique identifier for the record. Use this ID to adjust or delete these hours. It can be any ID you use to track the record up to 36 characters in length. (i.e. UUID). | 
**employee_id** | **int** | The ID of the employee. | 
**division_id** | **int** | [Optional] The ID of the division for the employee. | [optional] 
**department_id** | **int** | [Optional] The ID of the department for the employee. | [optional] 
**job_title_id** | **int** | [Optional] The ID of the job title for the employee. | [optional] 
**pay_code** | **str** | [Optional] Only necessary if the payroll provider requires a pay code | [optional] 
**date_hours_worked** | **str** | The date the hours were worked. Please use the ISO-8601 date format YYYY-MM-DD. | 
**pay_rate** | **float** | [Optional] The rate of pay. e.g. $15.00/hour should use 15.00 here. Only necessary if the payroll provider requires a pay rate. | [optional] 
**rate_type** | **str** | The type of hours - regular or overtime. Please use either \&quot;REG\&quot;, \&quot;OT\&quot;, or \&quot;DT\&quot; here. | 
**hours_worked** | **float** | The number of hours worked. | 
**job_code** | **int** | [Optional] A job code. | [optional] 
**job_data** | **str** | [Optional] A list of up to four 20 characters max job numbers in comma delimited format with no spaces. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_record import TimeTrackingRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingRecord from a JSON string
time_tracking_record_instance = TimeTrackingRecord.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingRecord.to_json())

# convert the object into a dict
time_tracking_record_dict = time_tracking_record_instance.to_dict()
# create an instance of TimeTrackingRecord from a dict
time_tracking_record_from_dict = TimeTrackingRecord.from_dict(time_tracking_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


