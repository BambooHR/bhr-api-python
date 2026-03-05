# XmlDirectoryEmployee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldset** | [**XmlDirectoryEmployeeFieldset**](XmlDirectoryEmployeeFieldset.md) |  | [optional] 
**employees** | [**XmlDirectoryEmployeeEmployees**](XmlDirectoryEmployeeEmployees.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_directory_employee import XmlDirectoryEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of XmlDirectoryEmployee from a JSON string
xml_directory_employee_instance = XmlDirectoryEmployee.from_json(json)
# print the JSON string representation of the object
print(XmlDirectoryEmployee.to_json())

# convert the object into a dict
xml_directory_employee_dict = xml_directory_employee_instance.to_dict()
# create an instance of XmlDirectoryEmployee from a dict
xml_directory_employee_from_dict = XmlDirectoryEmployee.from_dict(xml_directory_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


