# DatasetResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[DatasetV1]**](DatasetV1.md) | Array of available datasets. | [optional] 

## Example

```python
from bamboohr_sdk.models.dataset_response_v1 import DatasetResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetResponseV1 from a JSON string
dataset_response_v1_instance = DatasetResponseV1.from_json(json)
# print the JSON string representation of the object
print(DatasetResponseV1.to_json())

# convert the object into a dict
dataset_response_v1_dict = dataset_response_v1_instance.to_dict()
# create an instance of DatasetResponseV1 from a dict
dataset_response_v1_from_dict = DatasetResponseV1.from_dict(dataset_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


