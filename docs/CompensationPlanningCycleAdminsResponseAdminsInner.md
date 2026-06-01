# CompensationPlanningCycleAdminsResponseAdminsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | [optional] 
**display_name** | **str** | Display name of the admin | [optional] 
**first_name** | **str** | First name of the admin | [optional] 
**last_name** | **str** | Last name of the admin | [optional] 
**job_title** | **str** | Job title of the admin | [optional] 
**photo_url** | **str** | URL to the admin profile photo | [optional] 
**admin_type** | **str** | Type of admin | [optional] 
**is_removable** | **bool** | Whether this admin can be removed from the cycle | [optional] 
**added_at** | **datetime** |  | [optional] 
**added_by_employee_id** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_planning_cycle_admins_response_admins_inner import CompensationPlanningCycleAdminsResponseAdminsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationPlanningCycleAdminsResponseAdminsInner from a JSON string
compensation_planning_cycle_admins_response_admins_inner_instance = CompensationPlanningCycleAdminsResponseAdminsInner.from_json(json)
# print the JSON string representation of the object
print(CompensationPlanningCycleAdminsResponseAdminsInner.to_json())

# convert the object into a dict
compensation_planning_cycle_admins_response_admins_inner_dict = compensation_planning_cycle_admins_response_admins_inner_instance.to_dict()
# create an instance of CompensationPlanningCycleAdminsResponseAdminsInner from a dict
compensation_planning_cycle_admins_response_admins_inner_from_dict = CompensationPlanningCycleAdminsResponseAdminsInner.from_dict(compensation_planning_cycle_admins_response_admins_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


