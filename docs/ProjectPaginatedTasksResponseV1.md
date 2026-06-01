# ProjectPaginatedTasksResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProjectTimeTrackingTaskV1]**](ProjectTimeTrackingTaskV1.md) | Collection of time tracking tasks for a project. | 
**meta** | [**ProjectPaginatedTasksResponseV1Meta**](ProjectPaginatedTasksResponseV1Meta.md) |  | 
**links** | [**ProjectPaginatedTasksResponseV1Links**](ProjectPaginatedTasksResponseV1Links.md) |  | 

## Example

```python
from bamboohr_sdk.models.project_paginated_tasks_response_v1 import ProjectPaginatedTasksResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPaginatedTasksResponseV1 from a JSON string
project_paginated_tasks_response_v1_instance = ProjectPaginatedTasksResponseV1.from_json(json)
# print the JSON string representation of the object
print(ProjectPaginatedTasksResponseV1.to_json())

# convert the object into a dict
project_paginated_tasks_response_v1_dict = project_paginated_tasks_response_v1_instance.to_dict()
# create an instance of ProjectPaginatedTasksResponseV1 from a dict
project_paginated_tasks_response_v1_from_dict = ProjectPaginatedTasksResponseV1.from_dict(project_paginated_tasks_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


