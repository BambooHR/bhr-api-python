# JsonEmployeeFilesCategoriesInnerFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File ID. | [optional] 
**name** | **str** | File display name. | [optional] 
**original_file_name** | **str** | Original uploaded filename. | [optional] 
**size** | **int** | File size in bytes. | [optional] 
**date_created** | **str** | UTC creation timestamp in &#x60;YYYY-MM-DDTHH:MM:SS+0000&#x60; format. | [optional] 
**created_by** | **str** | Full name of the user who uploaded the file. | [optional] 
**share_with_employee** | **str** | Whether the file is shared with the employee. | [optional] 
**can_rename_file** | **str** | Whether the caller can rename this file. | [optional] 
**can_delete_file** | **str** | Whether the caller can delete this file. | [optional] 
**can_change_share_with_employee_field_value** | **str** | Whether the caller can toggle the share-with-employee setting. | [optional] 

## Example

```python
from bamboohr_sdk.models.json_employee_files_categories_inner_files_inner import JsonEmployeeFilesCategoriesInnerFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEmployeeFilesCategoriesInnerFilesInner from a JSON string
json_employee_files_categories_inner_files_inner_instance = JsonEmployeeFilesCategoriesInnerFilesInner.from_json(json)
# print the JSON string representation of the object
print(JsonEmployeeFilesCategoriesInnerFilesInner.to_json())

# convert the object into a dict
json_employee_files_categories_inner_files_inner_dict = json_employee_files_categories_inner_files_inner_instance.to_dict()
# create an instance of JsonEmployeeFilesCategoriesInnerFilesInner from a dict
json_employee_files_categories_inner_files_inner_from_dict = JsonEmployeeFilesCategoriesInnerFilesInner.from_dict(json_employee_files_categories_inner_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


