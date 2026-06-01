# ProjectUpdateTimeTrackingProjectV1

Data contract for partially updating a time tracking project. All fields are optional; only fields present in the request body will be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the project. | [optional] 
**billable** | **bool** | Whether or not the project is billable. | [optional] 
**include_in_payroll** | **bool** | Whether hours logged to this project will show in payroll and payroll reports. | [optional] 
**all_employees_assigned** | **bool** | Whether all time &amp; attendance employees are assigned or not. | [optional] 
**archived** | **bool** | Whether or not the project is archived. | [optional] 
**employee_ids** | **List[int]** | Array of employee IDs to assign to the project. Replaces the current assignment list when present; an empty array clears all assignments. | [optional] 
**has_tasks** | **bool** | Toggles whether time is logged directly to the project (false) or to specific tasks on the project (true). Setting to true requires the project to already have at least one active task; setting to false leaves existing tasks unchanged. | [optional] 

## Example

```python
from bamboohr_sdk.models.project_update_time_tracking_project_v1 import ProjectUpdateTimeTrackingProjectV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdateTimeTrackingProjectV1 from a JSON string
project_update_time_tracking_project_v1_instance = ProjectUpdateTimeTrackingProjectV1.from_json(json)
# print the JSON string representation of the object
print(ProjectUpdateTimeTrackingProjectV1.to_json())

# convert the object into a dict
project_update_time_tracking_project_v1_dict = project_update_time_tracking_project_v1_instance.to_dict()
# create an instance of ProjectUpdateTimeTrackingProjectV1 from a dict
project_update_time_tracking_project_v1_from_dict = ProjectUpdateTimeTrackingProjectV1.from_dict(project_update_time_tracking_project_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


