# ProjectCreateRequestSchema

Schema for creating a new time tracking project with optional tasks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the project. Must be unique and no more than 50 characters. | 
**billable** | **bool** | Indicates if the project is billable. Defaults to true if not provided. | [optional] 
**allow_all_employees** | **bool** | Indicates if all employees can log time for this project. Defaults to true if not provided. | [optional] 
**employee_ids** | **List[int]** | A list of employee IDs that can log time for this project. Only used when &#x60;allowAllEmployees&#x60; is false. | [optional] 
**has_tasks** | **bool** | Indicates if the project has tasks. Defaults to false if not provided. | [optional] 
**tasks** | [**List[TaskCreateSchema]**](TaskCreateSchema.md) | List of tasks to create and associate with the project. | [optional] 

## Example

```python
from bamboohr_sdk.models.project_create_request_schema import ProjectCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateRequestSchema from a JSON string
project_create_request_schema_instance = ProjectCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ProjectCreateRequestSchema.to_json())

# convert the object into a dict
project_create_request_schema_dict = project_create_request_schema_instance.to_dict()
# create an instance of ProjectCreateRequestSchema from a dict
project_create_request_schema_from_dict = ProjectCreateRequestSchema.from_dict(project_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


