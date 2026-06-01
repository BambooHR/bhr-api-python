# ProjectCreateTimeTrackingProjectV1

Request body for creating a time tracking project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**billable** | **bool** |  | [optional] [default to False]
**include_in_payroll** | **bool** |  | [optional] [default to False]
**all_employees_assigned** | **bool** | If true, every time-tracked employee is assigned to the project. Ignored when &#x60;employeeIds&#x60; is provided. | [optional] [default to False]
**employee_ids** | **List[int]** | Specific employee IDs to assign. Minimum 1 entry required when provided. Takes precedence over &#x60;allEmployeesAssigned&#x60;. | [optional] 
**tasks** | [**List[ProjectCreateTimeTrackingProjectV1TasksInner]**](ProjectCreateTimeTrackingProjectV1TasksInner.md) | Tasks to create alongside the project. Minimum 1 entry required when provided. | [optional] 

## Example

```python
from bamboohr_sdk.models.project_create_time_tracking_project_v1 import ProjectCreateTimeTrackingProjectV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateTimeTrackingProjectV1 from a JSON string
project_create_time_tracking_project_v1_instance = ProjectCreateTimeTrackingProjectV1.from_json(json)
# print the JSON string representation of the object
print(ProjectCreateTimeTrackingProjectV1.to_json())

# convert the object into a dict
project_create_time_tracking_project_v1_dict = project_create_time_tracking_project_v1_instance.to_dict()
# create an instance of ProjectCreateTimeTrackingProjectV1 from a dict
project_create_time_tracking_project_v1_from_dict = ProjectCreateTimeTrackingProjectV1.from_dict(project_create_time_tracking_project_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


