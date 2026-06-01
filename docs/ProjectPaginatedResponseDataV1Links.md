# ProjectPaginatedResponseDataV1Links

Pagination links. Keys are omitted when there is no previous/next page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**ProjectPaginatedResponseDataV1LinksPrev**](ProjectPaginatedResponseDataV1LinksPrev.md) |  | [optional] 
**next** | [**ProjectPaginatedResponseDataV1LinksNext**](ProjectPaginatedResponseDataV1LinksNext.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.project_paginated_response_data_v1_links import ProjectPaginatedResponseDataV1Links

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPaginatedResponseDataV1Links from a JSON string
project_paginated_response_data_v1_links_instance = ProjectPaginatedResponseDataV1Links.from_json(json)
# print the JSON string representation of the object
print(ProjectPaginatedResponseDataV1Links.to_json())

# convert the object into a dict
project_paginated_response_data_v1_links_dict = project_paginated_response_data_v1_links_instance.to_dict()
# create an instance of ProjectPaginatedResponseDataV1Links from a dict
project_paginated_response_data_v1_links_from_dict = ProjectPaginatedResponseDataV1Links.from_dict(project_paginated_response_data_v1_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


