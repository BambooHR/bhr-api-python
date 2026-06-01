# CompensationPlanningCycleAdminsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admins** | [**List[CompensationPlanningCycleAdminsResponseAdminsInner]**](CompensationPlanningCycleAdminsResponseAdminsInner.md) | List of admins for the cycle | [optional] 
**is_full_admin** | **bool** | Whether the requesting user is a full compensation plan admin | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_planning_cycle_admins_response import CompensationPlanningCycleAdminsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationPlanningCycleAdminsResponse from a JSON string
compensation_planning_cycle_admins_response_instance = CompensationPlanningCycleAdminsResponse.from_json(json)
# print the JSON string representation of the object
print(CompensationPlanningCycleAdminsResponse.to_json())

# convert the object into a dict
compensation_planning_cycle_admins_response_dict = compensation_planning_cycle_admins_response_instance.to_dict()
# create an instance of CompensationPlanningCycleAdminsResponse from a dict
compensation_planning_cycle_admins_response_from_dict = CompensationPlanningCycleAdminsResponse.from_dict(compensation_planning_cycle_admins_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


