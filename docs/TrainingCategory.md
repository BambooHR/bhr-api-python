# TrainingCategory

The category ID and name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the training category. | [optional] 
**name** | **str** | The name of the training category. | [optional] 

## Example

```python
from bamboohr_sdk.models.training_category import TrainingCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingCategory from a JSON string
training_category_instance = TrainingCategory.from_json(json)
# print the JSON string representation of the object
print(TrainingCategory.to_json())

# convert the object into a dict
training_category_dict = training_category_instance.to_dict()
# create an instance of TrainingCategory from a dict
training_category_from_dict = TrainingCategory.from_dict(training_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


