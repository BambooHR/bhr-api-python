# SchedulingSchedulingShiftAssessmentV1

A shift assessment result for an employee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of this assessment. | [readonly] 
**shift_id** | **str** |  | [optional] 
**employee_id** | **int** | The ID of the employee this assessment is for. | 
**var_date** | **date** | The date of the shift or clock entry in the local timezone of the shift. | 
**result** | **str** | The assessment result. | 
**violations** | [**List[SchedulingSchedulingShiftAssessmentViolationV1]**](SchedulingSchedulingShiftAssessmentViolationV1.md) | The violations associated with this assessment. | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.scheduling_scheduling_shift_assessment_v1 import SchedulingSchedulingShiftAssessmentV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingSchedulingShiftAssessmentV1 from a JSON string
scheduling_scheduling_shift_assessment_v1_instance = SchedulingSchedulingShiftAssessmentV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingSchedulingShiftAssessmentV1.to_json())

# convert the object into a dict
scheduling_scheduling_shift_assessment_v1_dict = scheduling_scheduling_shift_assessment_v1_instance.to_dict()
# create an instance of SchedulingSchedulingShiftAssessmentV1 from a dict
scheduling_scheduling_shift_assessment_v1_from_dict = SchedulingSchedulingShiftAssessmentV1.from_dict(scheduling_scheduling_shift_assessment_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


