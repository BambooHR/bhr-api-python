# ProjectPaginatedTimeTrackingProjectsResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ProjectPaginatedResponseDataV1Meta**](ProjectPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**ProjectPaginatedResponseDataV1Links**](ProjectPaginatedResponseDataV1Links.md) |  | [optional] 
**data** | [**List[ProjectTimeTrackingProjectV1]**](ProjectTimeTrackingProjectV1.md) | Collection of time tracking projects. | [optional] 

## Example

```python
from bamboohr_sdk.models.project_paginated_time_tracking_projects_response_v1 import ProjectPaginatedTimeTrackingProjectsResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPaginatedTimeTrackingProjectsResponseV1 from a JSON string
project_paginated_time_tracking_projects_response_v1_instance = ProjectPaginatedTimeTrackingProjectsResponseV1.from_json(json)
# print the JSON string representation of the object
print(ProjectPaginatedTimeTrackingProjectsResponseV1.to_json())

# convert the object into a dict
project_paginated_time_tracking_projects_response_v1_dict = project_paginated_time_tracking_projects_response_v1_instance.to_dict()
# create an instance of ProjectPaginatedTimeTrackingProjectsResponseV1 from a dict
project_paginated_time_tracking_projects_response_v1_from_dict = ProjectPaginatedTimeTrackingProjectsResponseV1.from_dict(project_paginated_time_tracking_projects_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


