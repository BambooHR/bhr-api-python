# DatasetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[DatasetsResponseDatasetsInner]**](DatasetsResponseDatasetsInner.md) | Array of available datasets | [optional] 

## Example

```python
from bamboohr_sdk.models.datasets_response import DatasetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetsResponse from a JSON string
datasets_response_instance = DatasetsResponse.from_json(json)
# print the JSON string representation of the object
print(DatasetsResponse.to_json())

# convert the object into a dict
datasets_response_dict = datasets_response_instance.to_dict()
# create an instance of DatasetsResponse from a dict
datasets_response_from_dict = DatasetsResponse.from_dict(datasets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


