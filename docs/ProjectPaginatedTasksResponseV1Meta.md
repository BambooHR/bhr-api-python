# ProjectPaginatedTasksResponseV1Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from bamboohr_sdk.models.project_paginated_tasks_response_v1_meta import ProjectPaginatedTasksResponseV1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPaginatedTasksResponseV1Meta from a JSON string
project_paginated_tasks_response_v1_meta_instance = ProjectPaginatedTasksResponseV1Meta.from_json(json)
# print the JSON string representation of the object
print(ProjectPaginatedTasksResponseV1Meta.to_json())

# convert the object into a dict
project_paginated_tasks_response_v1_meta_dict = project_paginated_tasks_response_v1_meta_instance.to_dict()
# create an instance of ProjectPaginatedTasksResponseV1Meta from a dict
project_paginated_tasks_response_v1_meta_from_dict = ProjectPaginatedTasksResponseV1Meta.from_dict(project_paginated_tasks_response_v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


