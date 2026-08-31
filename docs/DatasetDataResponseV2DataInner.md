# DatasetDataResponseV2DataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**Dict[str, DatasetDataResponseV2DataInnerFieldsValue]**](DatasetDataResponseV2DataInnerFieldsValue.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.dataset_data_response_v2_data_inner import DatasetDataResponseV2DataInner

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDataResponseV2DataInner from a JSON string
dataset_data_response_v2_data_inner_instance = DatasetDataResponseV2DataInner.from_json(json)
# print the JSON string representation of the object
print(DatasetDataResponseV2DataInner.to_json())

# convert the object into a dict
dataset_data_response_v2_data_inner_dict = dataset_data_response_v2_data_inner_instance.to_dict()
# create an instance of DatasetDataResponseV2DataInner from a dict
dataset_data_response_v2_data_inner_from_dict = DatasetDataResponseV2DataInner.from_dict(dataset_data_response_v2_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


