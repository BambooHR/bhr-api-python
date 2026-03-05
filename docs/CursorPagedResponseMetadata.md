# CursorPagedResponseMetadata

Metadata information for employee list responses including total count and pagination details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of employees matching the filter criteria | 
**page** | [**CursorPagesResponse**](CursorPagesResponse.md) | Pagination information for the current response | 

## Example

```python
from bamboohr_sdk.models.cursor_paged_response_metadata import CursorPagedResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPagedResponseMetadata from a JSON string
cursor_paged_response_metadata_instance = CursorPagedResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(CursorPagedResponseMetadata.to_json())

# convert the object into a dict
cursor_paged_response_metadata_dict = cursor_paged_response_metadata_instance.to_dict()
# create an instance of CursorPagedResponseMetadata from a dict
cursor_paged_response_metadata_from_dict = CursorPagedResponseMetadata.from_dict(cursor_paged_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


