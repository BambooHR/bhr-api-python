# PagedResponse

A response object that contains a paginated list of results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** | The data for the current page. | [optional] 
**meta** | [**PaginationMetaData**](PaginationMetaData.md) | The pagination metadata for the response. | [optional] 
**links** | [**Dict[str, AvailableAction]**](AvailableAction.md) | Hypermedia links for collection navigation (next, prev) and available collection actions (e.g., create). Actions are permission-based and may vary. | [optional] 

## Example

```python
from bamboohr_sdk.models.paged_response import PagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResponse from a JSON string
paged_response_instance = PagedResponse.from_json(json)
# print the JSON string representation of the object
print(PagedResponse.to_json())

# convert the object into a dict
paged_response_dict = paged_response_instance.to_dict()
# create an instance of PagedResponse from a dict
paged_response_from_dict = PagedResponse.from_dict(paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


