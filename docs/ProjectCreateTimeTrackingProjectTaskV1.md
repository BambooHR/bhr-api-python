# ProjectCreateTimeTrackingProjectTaskV1

Payload to create a task on a time tracking project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the task. | 
**billable** | **bool** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.project_create_time_tracking_project_task_v1 import ProjectCreateTimeTrackingProjectTaskV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateTimeTrackingProjectTaskV1 from a JSON string
project_create_time_tracking_project_task_v1_instance = ProjectCreateTimeTrackingProjectTaskV1.from_json(json)
# print the JSON string representation of the object
print(ProjectCreateTimeTrackingProjectTaskV1.to_json())

# convert the object into a dict
project_create_time_tracking_project_task_v1_dict = project_create_time_tracking_project_task_v1_instance.to_dict()
# create an instance of ProjectCreateTimeTrackingProjectTaskV1 from a dict
project_create_time_tracking_project_task_v1_from_dict = ProjectCreateTimeTrackingProjectTaskV1.from_dict(project_create_time_tracking_project_task_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


