# DatasetsResponseDatasetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Internal name identifier for the dataset | [optional] 
**label** | **str** | Human-readable label for the dataset | [optional] 

## Example

```python
from bamboohr_sdk.models.datasets_response_datasets_inner import DatasetsResponseDatasetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetsResponseDatasetsInner from a JSON string
datasets_response_datasets_inner_instance = DatasetsResponseDatasetsInner.from_json(json)
# print the JSON string representation of the object
print(DatasetsResponseDatasetsInner.to_json())

# convert the object into a dict
datasets_response_datasets_inner_dict = datasets_response_datasets_inner_instance.to_dict()
# create an instance of DatasetsResponseDatasetsInner from a dict
datasets_response_datasets_inner_from_dict = DatasetsResponseDatasetsInner.from_dict(datasets_response_datasets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


