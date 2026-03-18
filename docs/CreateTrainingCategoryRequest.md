# CreateTrainingCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new training category. | 

## Example

```python
from bamboohr_sdk.models.create_training_category_request import CreateTrainingCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTrainingCategoryRequest from a JSON string
create_training_category_request_instance = CreateTrainingCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTrainingCategoryRequest.to_json())

# convert the object into a dict
create_training_category_request_dict = create_training_category_request_instance.to_dict()
# create an instance of CreateTrainingCategoryRequest from a dict
create_training_category_request_from_dict = CreateTrainingCategoryRequest.from_dict(create_training_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


