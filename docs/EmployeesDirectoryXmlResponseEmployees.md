# EmployeesDirectoryXmlResponseEmployees

Directory employee records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee** | [**List[EmployeesDirectoryXmlResponseEmployeesEmployeeInner]**](EmployeesDirectoryXmlResponseEmployeesEmployeeInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employees_directory_xml_response_employees import EmployeesDirectoryXmlResponseEmployees

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesDirectoryXmlResponseEmployees from a JSON string
employees_directory_xml_response_employees_instance = EmployeesDirectoryXmlResponseEmployees.from_json(json)
# print the JSON string representation of the object
print(EmployeesDirectoryXmlResponseEmployees.to_json())

# convert the object into a dict
employees_directory_xml_response_employees_dict = employees_directory_xml_response_employees_instance.to_dict()
# create an instance of EmployeesDirectoryXmlResponseEmployees from a dict
employees_directory_xml_response_employees_from_dict = EmployeesDirectoryXmlResponseEmployees.from_dict(employees_directory_xml_response_employees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


