# CompensationPlanningCycleCompleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_id** | **int** |  | [optional] 
**updated_employees_count** | **int** |  | [optional] 
**cycle_closed_email_error** | **str** |  | [optional] 
**errors** | [**List[CompensationPlanningCycleCompleteResponseErrorsInner]**](CompensationPlanningCycleCompleteResponseErrorsInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_planning_cycle_complete_response import CompensationPlanningCycleCompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationPlanningCycleCompleteResponse from a JSON string
compensation_planning_cycle_complete_response_instance = CompensationPlanningCycleCompleteResponse.from_json(json)
# print the JSON string representation of the object
print(CompensationPlanningCycleCompleteResponse.to_json())

# convert the object into a dict
compensation_planning_cycle_complete_response_dict = compensation_planning_cycle_complete_response_instance.to_dict()
# create an instance of CompensationPlanningCycleCompleteResponse from a dict
compensation_planning_cycle_complete_response_from_dict = CompensationPlanningCycleCompleteResponse.from_dict(compensation_planning_cycle_complete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


