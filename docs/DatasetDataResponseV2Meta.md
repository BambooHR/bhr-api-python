# DatasetDataResponseV2Meta

Pagination metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.dataset_data_response_v2_meta import DatasetDataResponseV2Meta

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDataResponseV2Meta from a JSON string
dataset_data_response_v2_meta_instance = DatasetDataResponseV2Meta.from_json(json)
# print the JSON string representation of the object
print(DatasetDataResponseV2Meta.to_json())

# convert the object into a dict
dataset_data_response_v2_meta_dict = dataset_data_response_v2_meta_instance.to_dict()
# create an instance of DatasetDataResponseV2Meta from a dict
dataset_data_response_v2_meta_from_dict = DatasetDataResponseV2Meta.from_dict(dataset_data_response_v2_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


