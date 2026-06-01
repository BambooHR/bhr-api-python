# DatasetsResponseV12DatasetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Machine-readable dataset identifier, used as the datasetName path parameter in other Datasets endpoints. | [optional] 
**label** | **str** | Human-readable display name for the dataset. | [optional] 

## Example

```python
from bamboohr_sdk.models.datasets_response_v12_datasets_inner import DatasetsResponseV12DatasetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetsResponseV12DatasetsInner from a JSON string
datasets_response_v12_datasets_inner_instance = DatasetsResponseV12DatasetsInner.from_json(json)
# print the JSON string representation of the object
print(DatasetsResponseV12DatasetsInner.to_json())

# convert the object into a dict
datasets_response_v12_datasets_inner_dict = datasets_response_v12_datasets_inner_instance.to_dict()
# create an instance of DatasetsResponseV12DatasetsInner from a dict
datasets_response_v12_datasets_inner_from_dict = DatasetsResponseV12DatasetsInner.from_dict(datasets_response_v12_datasets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


