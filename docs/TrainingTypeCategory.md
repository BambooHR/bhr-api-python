# TrainingTypeCategory

The training category when set, or an empty array when no category is assigned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the training category. | [optional] 
**name** | **str** | The name of the training category. | [optional] 

## Example

```python
from bamboohr_sdk.models.training_type_category import TrainingTypeCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingTypeCategory from a JSON string
training_type_category_instance = TrainingTypeCategory.from_json(json)
# print the JSON string representation of the object
print(TrainingTypeCategory.to_json())

# convert the object into a dict
training_type_category_dict = training_type_category_instance.to_dict()
# create an instance of TrainingTypeCategory from a dict
training_type_category_from_dict = TrainingTypeCategory.from_dict(training_type_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


