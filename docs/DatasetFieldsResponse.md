# DatasetFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**fields** | [**List[ModelField]**](ModelField.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.dataset_fields_response import DatasetFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetFieldsResponse from a JSON string
dataset_fields_response_instance = DatasetFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(DatasetFieldsResponse.to_json())

# convert the object into a dict
dataset_fields_response_dict = dataset_fields_response_instance.to_dict()
# create an instance of DatasetFieldsResponse from a dict
dataset_fields_response_from_dict = DatasetFieldsResponse.from_dict(dataset_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


