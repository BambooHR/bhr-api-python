# SchedulingShiftAssessmentListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchedulingSchedulingShiftAssessmentV1]**](SchedulingSchedulingShiftAssessmentV1.md) | Collection of shift assessments | [optional] 
**meta** | [**SchedulingShiftAssessmentListResponseV1Meta**](SchedulingShiftAssessmentListResponseV1Meta.md) |  | [optional] 
**links** | [**SchedulingShiftListResponseV1Links**](SchedulingShiftListResponseV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.scheduling_shift_assessment_list_response_v1 import SchedulingShiftAssessmentListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingShiftAssessmentListResponseV1 from a JSON string
scheduling_shift_assessment_list_response_v1_instance = SchedulingShiftAssessmentListResponseV1.from_json(json)
# print the JSON string representation of the object
print(SchedulingShiftAssessmentListResponseV1.to_json())

# convert the object into a dict
scheduling_shift_assessment_list_response_v1_dict = scheduling_shift_assessment_list_response_v1_instance.to_dict()
# create an instance of SchedulingShiftAssessmentListResponseV1 from a dict
scheduling_shift_assessment_list_response_v1_from_dict = SchedulingShiftAssessmentListResponseV1.from_dict(scheduling_shift_assessment_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


