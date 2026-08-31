# ProjectUpdateTimeTrackingProjectTaskV1

Payload to partially update a task on a time tracking project. All fields are optional; at least one field must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the task. | [optional] 
**billable** | **bool** | Whether hours on this task are billable. | [optional] 

## Example

```python
from bamboohr_sdk.models.project_update_time_tracking_project_task_v1 import ProjectUpdateTimeTrackingProjectTaskV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdateTimeTrackingProjectTaskV1 from a JSON string
project_update_time_tracking_project_task_v1_instance = ProjectUpdateTimeTrackingProjectTaskV1.from_json(json)
# print the JSON string representation of the object
print(ProjectUpdateTimeTrackingProjectTaskV1.to_json())

# convert the object into a dict
project_update_time_tracking_project_task_v1_dict = project_update_time_tracking_project_task_v1_instance.to_dict()
# create an instance of ProjectUpdateTimeTrackingProjectTaskV1 from a dict
project_update_time_tracking_project_task_v1_from_dict = ProjectUpdateTimeTrackingProjectTaskV1.from_dict(project_update_time_tracking_project_task_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


