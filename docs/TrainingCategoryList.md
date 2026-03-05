# TrainingCategoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | [**TrainingCategory**](TrainingCategory.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.training_category_list import TrainingCategoryList

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingCategoryList from a JSON string
training_category_list_instance = TrainingCategoryList.from_json(json)
# print the JSON string representation of the object
print(TrainingCategoryList.to_json())

# convert the object into a dict
training_category_list_dict = training_category_list_instance.to_dict()
# create an instance of TrainingCategoryList from a dict
training_category_list_from_dict = TrainingCategoryList.from_dict(training_category_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


