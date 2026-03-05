# TimeTrackingProjectWithTasksAndEmployeeIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the project. | [optional] 
**name** | **str** | Name of the project. | [optional] 
**tasks** | [**List[TimeTrackingTask]**](TimeTrackingTask.md) | A list of time tracking tasks for the project. | [optional] 
**employee_ids** | **List[int]** | A list of employee IDs that can log time for this project. If not present, all employees can log time for the project. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_tracking_project_with_tasks_and_employee_ids import TimeTrackingProjectWithTasksAndEmployeeIds

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingProjectWithTasksAndEmployeeIds from a JSON string
time_tracking_project_with_tasks_and_employee_ids_instance = TimeTrackingProjectWithTasksAndEmployeeIds.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingProjectWithTasksAndEmployeeIds.to_json())

# convert the object into a dict
time_tracking_project_with_tasks_and_employee_ids_dict = time_tracking_project_with_tasks_and_employee_ids_instance.to_dict()
# create an instance of TimeTrackingProjectWithTasksAndEmployeeIds from a dict
time_tracking_project_with_tasks_and_employee_ids_from_dict = TimeTrackingProjectWithTasksAndEmployeeIds.from_dict(time_tracking_project_with_tasks_and_employee_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


