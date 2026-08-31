# SchedulingSchedulingShiftAssessmentViolationV1

A violation associated with a shift assessment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessment_id** | **str** | The ID of the assessment this violation belongs to. | 
**type** | **str** | The type of violation. | 
**amount** | **int** |  | [optional] 
**employee_timesheet_clock_entry_id** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_scheduling_shift_assessment_violation_v1 import SchedulingSchedulingShiftAssessmentViolationV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingSchedulingShiftAssessmentViolationV1 from a JSON string
scheduling_scheduling_shift_assessment_violation_v1_instance = SchedulingSchedulingShiftAssessmentViolationV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingSchedulingShiftAssessmentViolationV1.to_json())

# convert the object into a dict
scheduling_scheduling_shift_assessment_violation_v1_dict = scheduling_scheduling_shift_assessment_violation_v1_instance.to_dict()
# create an instance of SchedulingSchedulingShiftAssessmentViolationV1 from a dict
scheduling_scheduling_shift_assessment_violation_v1_from_dict = SchedulingSchedulingShiftAssessmentViolationV1.from_dict(scheduling_scheduling_shift_assessment_violation_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


