# AddTrainingTypeRequestCategory

The category is optional and you can pass either a category id or a category name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category ID | [optional] 
**name** | **str** | Category Name | [optional] 
**accuracy** | **int** | Accuracy in meters of the clock in location | [optional] 
**address** | **str** | Address... | [optional] 

## Example

```python
from bamboohr_sdk.models.add_training_type_request_category import AddTrainingTypeRequestCategory

# TODO update the JSON string below
json = "{}"
# create an instance of AddTrainingTypeRequestCategory from a JSON string
add_training_type_request_category_instance = AddTrainingTypeRequestCategory.from_json(json)
# print the JSON string representation of the object
print(AddTrainingTypeRequestCategory.to_json())

# convert the object into a dict
add_training_type_request_category_dict = add_training_type_request_category_instance.to_dict()
# create an instance of AddTrainingTypeRequestCategory from a dict
add_training_type_request_category_from_dict = AddTrainingTypeRequestCategory.from_dict(add_training_type_request_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


