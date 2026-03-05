# XmlDirectoryEmployeeEmployeesEmployeeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee ID (XML attribute) | [optional] 
**var_field** | [**List[XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner]**](XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner.md) | Employee field values | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_directory_employee_employees_employee_inner import XmlDirectoryEmployeeEmployeesEmployeeInner

# TODO update the JSON string below
json = "{}"
# create an instance of XmlDirectoryEmployeeEmployeesEmployeeInner from a JSON string
xml_directory_employee_employees_employee_inner_instance = XmlDirectoryEmployeeEmployeesEmployeeInner.from_json(json)
# print the JSON string representation of the object
print(XmlDirectoryEmployeeEmployeesEmployeeInner.to_json())

# convert the object into a dict
xml_directory_employee_employees_employee_inner_dict = xml_directory_employee_employees_employee_inner_instance.to_dict()
# create an instance of XmlDirectoryEmployeeEmployeesEmployeeInner from a dict
xml_directory_employee_employees_employee_inner_from_dict = XmlDirectoryEmployeeEmployeesEmployeeInner.from_dict(xml_directory_employee_employees_employee_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


