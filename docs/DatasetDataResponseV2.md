# DatasetDataResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DatasetDataResponseV2DataInner]**](DatasetDataResponseV2DataInner.md) | Array of record objects. Each object contains a &#x60;fields&#x60; object whose keys are the requested field names. Values may be strings, numbers, booleans, arrays/objects, or null depending on the dataset field and value. | [optional] 
**links** | [**DatasetDataResponseV2Links**](DatasetDataResponseV2Links.md) |  | [optional] 
**meta** | [**DatasetDataResponseV2Meta**](DatasetDataResponseV2Meta.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.dataset_data_response_v2 import DatasetDataResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDataResponseV2 from a JSON string
dataset_data_response_v2_instance = DatasetDataResponseV2.from_json(json)
# print the JSON string representation of the object
print(DatasetDataResponseV2.to_json())

# convert the object into a dict
dataset_data_response_v2_dict = dataset_data_response_v2_instance.to_dict()
# create an instance of DatasetDataResponseV2 from a dict
dataset_data_response_v2_from_dict = DatasetDataResponseV2.from_dict(dataset_data_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


