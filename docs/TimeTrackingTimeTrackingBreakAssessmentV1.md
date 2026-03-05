# TimeTrackingTimeTrackingBreakAssessmentV1

A break assessment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the time tracking break assessment | [optional] [readonly] 
**break_id** | **str** | The unique identifier of the break | [optional] [readonly] 
**employee_id** | **float** | The id of the employee | [optional] 
**employee_timesheet_id** | **float** | The id of the employee timesheet | [optional] 
**var_date** | **date** | The date of the break assessment | [optional] 
**timezone** | **str** | The timezone of the break assessment | [optional] 
**result** | **str** | The result of the break assessment | [optional] 
**available_ymdt** | **datetime** | ISO 8601 timestamp when the break became available | [optional] [readonly] 
**unavailable_ymdt** | **datetime** | ISO 8601 timestamp when the break became unavailable | [optional] [readonly] 
**created_at** | **datetime** | ISO 8601 timestamp when the break was created | [optional] [readonly] 
**updated_at** | **datetime** | ISO 8601 timestamp when the break was last updated | [optional] [readonly] 
**violations** | [**List[TimeTrackingTimeTrackingBreakAssessmentViolationV1]**](TimeTrackingTimeTrackingBreakAssessmentViolationV1.md) | Violations associated with the assessment  | [optional] 
**clock_entry_ids** | **List[int]** | Clock entry ids associated with the time tracking break assessment | [optional] 
**expected_duration** | **int** | The expected duration of the break in minutes | [optional] 
**recorded_duration** | **int** | The recorded duration of the break in minutes | [optional] 
**duration_difference** | **int** | The difference between the expected and recorded duration in minutes | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_break_assessment_v1 import TimeTrackingTimeTrackingBreakAssessmentV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingBreakAssessmentV1 from a JSON string
time_tracking_time_tracking_break_assessment_v1_instance = TimeTrackingTimeTrackingBreakAssessmentV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingBreakAssessmentV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_break_assessment_v1_dict = time_tracking_time_tracking_break_assessment_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingBreakAssessmentV1 from a dict
time_tracking_time_tracking_break_assessment_v1_from_dict = TimeTrackingTimeTrackingBreakAssessmentV1.from_dict(time_tracking_time_tracking_break_assessment_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


