# DatasetV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Machine-readable dataset identifier, used as the datasetName path parameter in other Datasets endpoints. | [optional] 
**label** | **str** | Human-readable display name for the dataset. | [optional] 

## Example

```python
from bamboohr_sdk.models.dataset_v1 import DatasetV1

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetV1 from a JSON string
dataset_v1_instance = DatasetV1.from_json(json)
# print the JSON string representation of the object
print(DatasetV1.to_json())

# convert the object into a dict
dataset_v1_dict = dataset_v1_instance.to_dict()
# create an instance of DatasetV1 from a dict
dataset_v1_from_dict = DatasetV1.from_dict(dataset_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


