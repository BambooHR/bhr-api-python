# PagedLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LocationResponseObject]**](LocationResponseObject.md) | Array of location resources for the current page | [optional] 
**meta** | [**PaginationMetaData**](PaginationMetaData.md) | The pagination metadata for the response. | [optional] 
**links** | [**Dict[str, AvailableAction]**](AvailableAction.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.paged_location_response import PagedLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PagedLocationResponse from a JSON string
paged_location_response_instance = PagedLocationResponse.from_json(json)
# print the JSON string representation of the object
print(PagedLocationResponse.to_json())

# convert the object into a dict
paged_location_response_dict = paged_location_response_instance.to_dict()
# create an instance of PagedLocationResponse from a dict
paged_location_response_from_dict = PagedLocationResponse.from_dict(paged_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


