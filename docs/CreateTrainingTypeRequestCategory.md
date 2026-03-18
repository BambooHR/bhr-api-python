# CreateTrainingTypeRequestCategory

The category is optional and you can pass either a category id or a category name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category ID | [optional] 
**name** | **str** | Category Name | [optional] 

## Example

```python
from bamboohr_sdk.models.create_training_type_request_category import CreateTrainingTypeRequestCategory

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTrainingTypeRequestCategory from a JSON string
create_training_type_request_category_instance = CreateTrainingTypeRequestCategory.from_json(json)
# print the JSON string representation of the object
print(CreateTrainingTypeRequestCategory.to_json())

# convert the object into a dict
create_training_type_request_category_dict = create_training_type_request_category_instance.to_dict()
# create an instance of CreateTrainingTypeRequestCategory from a dict
create_training_type_request_category_from_dict = CreateTrainingTypeRequestCategory.from_dict(create_training_type_request_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


