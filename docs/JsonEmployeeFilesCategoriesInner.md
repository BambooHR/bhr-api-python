# JsonEmployeeFilesCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category ID. | [optional] 
**name** | **str** | Category display name. | [optional] 
**can_rename_category** | **str** | Whether the caller can rename this category. | [optional] 
**can_delete_category** | **str** | Whether the caller can delete this category. | [optional] 
**can_upload_files** | **str** | Whether the caller can upload files to this category. | [optional] 
**display_if_empty** | **str** | Whether to display the category when it has no files. | [optional] 
**files** | [**List[JsonEmployeeFilesCategoriesInnerFilesInner]**](JsonEmployeeFilesCategoriesInnerFilesInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.json_employee_files_categories_inner import JsonEmployeeFilesCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEmployeeFilesCategoriesInner from a JSON string
json_employee_files_categories_inner_instance = JsonEmployeeFilesCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(JsonEmployeeFilesCategoriesInner.to_json())

# convert the object into a dict
json_employee_files_categories_inner_dict = json_employee_files_categories_inner_instance.to_dict()
# create an instance of JsonEmployeeFilesCategoriesInner from a dict
json_employee_files_categories_inner_from_dict = JsonEmployeeFilesCategoriesInner.from_dict(json_employee_files_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


