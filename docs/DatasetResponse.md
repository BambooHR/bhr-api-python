# DatasetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[Dataset]**](Dataset.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.dataset_response import DatasetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetResponse from a JSON string
dataset_response_instance = DatasetResponse.from_json(json)
# print the JSON string representation of the object
print(DatasetResponse.to_json())

# convert the object into a dict
dataset_response_dict = dataset_response_instance.to_dict()
# create an instance of DatasetResponse from a dict
dataset_response_from_dict = DatasetResponse.from_dict(dataset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


