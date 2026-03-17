# XmlEmployeeFilesCategoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category ID on the &#x60;&lt;category&gt;&#x60; element. | [optional] 
**name** | **str** |  | [optional] 
**can_rename_category** | **str** |  | [optional] 
**can_delete_category** | **str** |  | [optional] 
**can_upload_files** | **str** |  | [optional] 
**display_if_empty** | **str** |  | [optional] 
**file** | [**List[XmlEmployeeFilesCategoryInnerFileInner]**](XmlEmployeeFilesCategoryInnerFileInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_employee_files_category_inner import XmlEmployeeFilesCategoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of XmlEmployeeFilesCategoryInner from a JSON string
xml_employee_files_category_inner_instance = XmlEmployeeFilesCategoryInner.from_json(json)
# print the JSON string representation of the object
print(XmlEmployeeFilesCategoryInner.to_json())

# convert the object into a dict
xml_employee_files_category_inner_dict = xml_employee_files_category_inner_instance.to_dict()
# create an instance of XmlEmployeeFilesCategoryInner from a dict
xml_employee_files_category_inner_from_dict = XmlEmployeeFilesCategoryInner.from_dict(xml_employee_files_category_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


