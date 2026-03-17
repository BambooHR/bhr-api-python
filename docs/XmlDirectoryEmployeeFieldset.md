# XmlDirectoryEmployeeFieldset

Field definitions included in this directory response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | [**List[XmlDirectoryEmployeeFieldsetFieldInner]**](XmlDirectoryEmployeeFieldsetFieldInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_directory_employee_fieldset import XmlDirectoryEmployeeFieldset

# TODO update the JSON string below
json = "{}"
# create an instance of XmlDirectoryEmployeeFieldset from a JSON string
xml_directory_employee_fieldset_instance = XmlDirectoryEmployeeFieldset.from_json(json)
# print the JSON string representation of the object
print(XmlDirectoryEmployeeFieldset.to_json())

# convert the object into a dict
xml_directory_employee_fieldset_dict = xml_directory_employee_fieldset_instance.to_dict()
# create an instance of XmlDirectoryEmployeeFieldset from a dict
xml_directory_employee_fieldset_from_dict = XmlDirectoryEmployeeFieldset.from_dict(xml_directory_employee_fieldset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


