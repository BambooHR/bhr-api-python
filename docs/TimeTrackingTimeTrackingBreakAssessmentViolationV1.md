# TimeTrackingTimeTrackingBreakAssessmentViolationV1

A break assessment violation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessment_id** | **str** | The unique identifier for the time tracking break assessment. | [optional] [readonly] 
**type** | **str** | The type of the violation | [optional] [readonly] 
**employee_timesheet_clock_entry_id** | **float** | The id of the employee timesheet clock entry | [optional] [readonly] 
**amount** | **float** | The amount of the violation | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.time_tracking_time_tracking_break_assessment_violation_v1 import TimeTrackingTimeTrackingBreakAssessmentViolationV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingTimeTrackingBreakAssessmentViolationV1 from a JSON string
time_tracking_time_tracking_break_assessment_violation_v1_instance = TimeTrackingTimeTrackingBreakAssessmentViolationV1.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingTimeTrackingBreakAssessmentViolationV1.to_json())

# convert the object into a dict
time_tracking_time_tracking_break_assessment_violation_v1_dict = time_tracking_time_tracking_break_assessment_violation_v1_instance.to_dict()
# create an instance of TimeTrackingTimeTrackingBreakAssessmentViolationV1 from a dict
time_tracking_time_tracking_break_assessment_violation_v1_from_dict = TimeTrackingTimeTrackingBreakAssessmentViolationV1.from_dict(time_tracking_time_tracking_break_assessment_violation_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


