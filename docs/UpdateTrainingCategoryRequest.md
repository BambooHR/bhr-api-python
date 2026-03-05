# UpdateTrainingCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the training category. | 

## Example

```python
from bamboohr_sdk.models.update_training_category_request import UpdateTrainingCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTrainingCategoryRequest from a JSON string
update_training_category_request_instance = UpdateTrainingCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTrainingCategoryRequest.to_json())

# convert the object into a dict
update_training_category_request_dict = update_training_category_request_instance.to_dict()
# create an instance of UpdateTrainingCategoryRequest from a dict
update_training_category_request_from_dict = UpdateTrainingCategoryRequest.from_dict(update_training_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


