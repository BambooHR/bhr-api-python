# AdjustTimeTrackingRequestSchema

Schema for adjust time tracking request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_tracking_id** | **str** | The time tracking id is the id that was used to track the record up to 36 characters in length. (i.e. UUID). | 
**hours_worked** | **float** | The updated number of hours worked. e.g. if Employee A worked 8.0 hours originally and decided they only worked 6.0, please send 6.0 here not -2.0. | 
**project_id** | **int** | ID of the project associated with this time tracking record | [optional] 
**task_id** | **int** | ID of the task associated with this time tracking record | [optional] 
**shift_differential_id** | **int** | ID of the shift differential associated with this time tracking record | [optional] 
**holiday_id** | **int** | ID of the holiday associated with this time tracking record | [optional] 

## Example

```python
from bamboohr_sdk.models.adjust_time_tracking_request_schema import AdjustTimeTrackingRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustTimeTrackingRequestSchema from a JSON string
adjust_time_tracking_request_schema_instance = AdjustTimeTrackingRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AdjustTimeTrackingRequestSchema.to_json())

# convert the object into a dict
adjust_time_tracking_request_schema_dict = adjust_time_tracking_request_schema_instance.to_dict()
# create an instance of AdjustTimeTrackingRequestSchema from a dict
adjust_time_tracking_request_schema_from_dict = AdjustTimeTrackingRequestSchema.from_dict(adjust_time_tracking_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


