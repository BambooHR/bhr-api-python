# ProjectPaginatedResponseDataV1

Pagination envelope shared by paginated Project endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ProjectPaginatedResponseDataV1Meta**](ProjectPaginatedResponseDataV1Meta.md) |  | [optional] 
**links** | [**ProjectPaginatedResponseDataV1Links**](ProjectPaginatedResponseDataV1Links.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.project_paginated_response_data_v1 import ProjectPaginatedResponseDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPaginatedResponseDataV1 from a JSON string
project_paginated_response_data_v1_instance = ProjectPaginatedResponseDataV1.from_json(json)
# print the JSON string representation of the object
print(ProjectPaginatedResponseDataV1.to_json())

# convert the object into a dict
project_paginated_response_data_v1_dict = project_paginated_response_data_v1_instance.to_dict()
# create an instance of ProjectPaginatedResponseDataV1 from a dict
project_paginated_response_data_v1_from_dict = ProjectPaginatedResponseDataV1.from_dict(project_paginated_response_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


