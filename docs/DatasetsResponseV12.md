# DatasetsResponseV12


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[DatasetsResponseV12DatasetsInner]**](DatasetsResponseV12DatasetsInner.md) | Array of available datasets | [optional] 

## Example

```python
from bamboohr_sdk.models.datasets_response_v12 import DatasetsResponseV12

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetsResponseV12 from a JSON string
datasets_response_v12_instance = DatasetsResponseV12.from_json(json)
# print the JSON string representation of the object
print(DatasetsResponseV12.to_json())

# convert the object into a dict
datasets_response_v12_dict = datasets_response_v12_instance.to_dict()
# create an instance of DatasetsResponseV12 from a dict
datasets_response_v12_from_dict = DatasetsResponseV12.from_dict(datasets_response_v12_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


