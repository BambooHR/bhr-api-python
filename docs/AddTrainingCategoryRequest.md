# AddTrainingCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new training category. | 

## Example

```python
from bamboohr_sdk.models.add_training_category_request import AddTrainingCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTrainingCategoryRequest from a JSON string
add_training_category_request_instance = AddTrainingCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(AddTrainingCategoryRequest.to_json())

# convert the object into a dict
add_training_category_request_dict = add_training_category_request_instance.to_dict()
# create an instance of AddTrainingCategoryRequest from a dict
add_training_category_request_from_dict = AddTrainingCategoryRequest.from_dict(add_training_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


