# TaskCreateSchema

Schema for creating a new task for a time tracking project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the task. | 
**billable** | **bool** | Indicates if the task is billable. Defaults to true if not provided. | [optional] 

## Example

```python
from bamboohr_sdk.models.task_create_schema import TaskCreateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreateSchema from a JSON string
task_create_schema_instance = TaskCreateSchema.from_json(json)
# print the JSON string representation of the object
print(TaskCreateSchema.to_json())

# convert the object into a dict
task_create_schema_dict = task_create_schema_instance.to_dict()
# create an instance of TaskCreateSchema from a dict
task_create_schema_from_dict = TaskCreateSchema.from_dict(task_create_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


