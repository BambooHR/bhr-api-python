# UpdateTrainingTypeRequestCategory

Category is optional and passing an empty value will remove the category from the training type. Passing a name will assign the training type to the new training category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category ID | [optional] 
**name** | **str** | Category Name | [optional] 
**accuracy** | **int** | Accuracy in meters of the clock in location | [optional] 
**address** | **str** | Address... | [optional] 

## Example

```python
from bamboohr_sdk.models.update_training_type_request_category import UpdateTrainingTypeRequestCategory

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTrainingTypeRequestCategory from a JSON string
update_training_type_request_category_instance = UpdateTrainingTypeRequestCategory.from_json(json)
# print the JSON string representation of the object
print(UpdateTrainingTypeRequestCategory.to_json())

# convert the object into a dict
update_training_type_request_category_dict = update_training_type_request_category_instance.to_dict()
# create an instance of UpdateTrainingTypeRequestCategory from a dict
update_training_type_request_category_from_dict = UpdateTrainingTypeRequestCategory.from_dict(update_training_type_request_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


