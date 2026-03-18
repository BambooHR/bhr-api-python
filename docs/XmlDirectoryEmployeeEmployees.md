# XmlDirectoryEmployeeEmployees

Employee records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee** | [**List[XmlDirectoryEmployeeEmployeesEmployeeInner]**](XmlDirectoryEmployeeEmployeesEmployeeInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_directory_employee_employees import XmlDirectoryEmployeeEmployees

# TODO update the JSON string below
json = "{}"
# create an instance of XmlDirectoryEmployeeEmployees from a JSON string
xml_directory_employee_employees_instance = XmlDirectoryEmployeeEmployees.from_json(json)
# print the JSON string representation of the object
print(XmlDirectoryEmployeeEmployees.to_json())

# convert the object into a dict
xml_directory_employee_employees_dict = xml_directory_employee_employees_instance.to_dict()
# create an instance of XmlDirectoryEmployeeEmployees from a dict
xml_directory_employee_employees_from_dict = XmlDirectoryEmployeeEmployees.from_dict(xml_directory_employee_employees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


