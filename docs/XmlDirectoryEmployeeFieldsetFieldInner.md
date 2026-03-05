# XmlDirectoryEmployeeFieldsetFieldInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Field identifier (XML attribute) | [optional] 
**value** | **str** | Field display name (element text content) | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_directory_employee_fieldset_field_inner import XmlDirectoryEmployeeFieldsetFieldInner

# TODO update the JSON string below
json = "{}"
# create an instance of XmlDirectoryEmployeeFieldsetFieldInner from a JSON string
xml_directory_employee_fieldset_field_inner_instance = XmlDirectoryEmployeeFieldsetFieldInner.from_json(json)
# print the JSON string representation of the object
print(XmlDirectoryEmployeeFieldsetFieldInner.to_json())

# convert the object into a dict
xml_directory_employee_fieldset_field_inner_dict = xml_directory_employee_fieldset_field_inner_instance.to_dict()
# create an instance of XmlDirectoryEmployeeFieldsetFieldInner from a dict
xml_directory_employee_fieldset_field_inner_from_dict = XmlDirectoryEmployeeFieldsetFieldInner.from_dict(xml_directory_employee_fieldset_field_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


