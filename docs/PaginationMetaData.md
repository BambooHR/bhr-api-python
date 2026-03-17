# PaginationMetaData

A response object that contains pagination metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page number of the results. | [optional] 
**page_size** | **int** | The number of items per page. | [optional] 
**total_pages** | **int** | The total number of pages available. | [optional] 
**total_items** | **int** | The total number of items available. | [optional] 

## Example

```python
from bamboohr_sdk.models.pagination_meta_data import PaginationMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationMetaData from a JSON string
pagination_meta_data_instance = PaginationMetaData.from_json(json)
# print the JSON string representation of the object
print(PaginationMetaData.to_json())

# convert the object into a dict
pagination_meta_data_dict = pagination_meta_data_instance.to_dict()
# create an instance of PaginationMetaData from a dict
pagination_meta_data_from_dict = PaginationMetaData.from_dict(pagination_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


