# ProjectTimeTrackingTaskV1

A task within a time tracking project. Tasks are sub-organizational units used to further classify hours worked.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the task. | [optional] [readonly] 
**name** | **str** | The name of the task. | [optional] 
**project_id** | **int** | The ID of the project this task belongs to. | [optional] 
**billable** | **bool** | Whether the task is billable. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from bamboohr_sdk.models.project_time_tracking_task_v1 import ProjectTimeTrackingTaskV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTimeTrackingTaskV1 from a JSON string
project_time_tracking_task_v1_instance = ProjectTimeTrackingTaskV1.from_json(json)
# print the JSON string representation of the object
print(ProjectTimeTrackingTaskV1.to_json())

# convert the object into a dict
project_time_tracking_task_v1_dict = project_time_tracking_task_v1_instance.to_dict()
# create an instance of ProjectTimeTrackingTaskV1 from a dict
project_time_tracking_task_v1_from_dict = ProjectTimeTrackingTaskV1.from_dict(project_time_tracking_task_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


