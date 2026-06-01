# DatasetDataResponseV2Links

Pagination navigation links. Contains `next` and/or `prev` URLs when applicable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**prev** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.dataset_data_response_v2_links import DatasetDataResponseV2Links

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDataResponseV2Links from a JSON string
dataset_data_response_v2_links_instance = DatasetDataResponseV2Links.from_json(json)
# print the JSON string representation of the object
print(DatasetDataResponseV2Links.to_json())

# convert the object into a dict
dataset_data_response_v2_links_dict = dataset_data_response_v2_links_instance.to_dict()
# create an instance of DatasetDataResponseV2Links from a dict
dataset_data_response_v2_links_from_dict = DatasetDataResponseV2Links.from_dict(dataset_data_response_v2_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


