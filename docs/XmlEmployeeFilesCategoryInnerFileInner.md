# XmlEmployeeFilesCategoryInnerFileInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File ID on the &#x60;&lt;file&gt;&#x60; element. | [optional] 
**name** | **str** |  | [optional] 
**original_file_name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**date_created** | **str** | UTC creation timestamp in &#x60;YYYY-MM-DD HH:MM:SS&#x60; format. | [optional] 
**created_by** | **str** |  | [optional] 
**share_with_employee** | **str** |  | [optional] 
**can_rename_file** | **str** |  | [optional] 
**can_delete_file** | **str** |  | [optional] 
**can_change_share_with_employee_field_value** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_employee_files_category_inner_file_inner import XmlEmployeeFilesCategoryInnerFileInner

# TODO update the JSON string below
json = "{}"
# create an instance of XmlEmployeeFilesCategoryInnerFileInner from a JSON string
xml_employee_files_category_inner_file_inner_instance = XmlEmployeeFilesCategoryInnerFileInner.from_json(json)
# print the JSON string representation of the object
print(XmlEmployeeFilesCategoryInnerFileInner.to_json())

# convert the object into a dict
xml_employee_files_category_inner_file_inner_dict = xml_employee_files_category_inner_file_inner_instance.to_dict()
# create an instance of XmlEmployeeFilesCategoryInnerFileInner from a dict
xml_employee_files_category_inner_file_inner_from_dict = XmlEmployeeFilesCategoryInnerFileInner.from_dict(xml_employee_files_category_inner_file_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


