# TrainingTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**training_id** | [**TrainingType**](TrainingType.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.training_type_list import TrainingTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingTypeList from a JSON string
training_type_list_instance = TrainingTypeList.from_json(json)
# print the JSON string representation of the object
print(TrainingTypeList.to_json())

# convert the object into a dict
training_type_list_dict = training_type_list_instance.to_dict()
# create an instance of TrainingTypeList from a dict
training_type_list_from_dict = TrainingTypeList.from_dict(training_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


