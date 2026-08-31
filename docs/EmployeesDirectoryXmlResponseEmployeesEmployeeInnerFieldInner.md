# EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Field identifier matching one of the ids in &#x60;&lt;fieldset&gt;&#x60;. | [optional] 
**value** | **str** | Field value serialized as element text content. | [optional] 

## Example

```python
from bamboohr_sdk.models.employees_directory_xml_response_employees_employee_inner_field_inner import EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner from a JSON string
employees_directory_xml_response_employees_employee_inner_field_inner_instance = EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner.from_json(json)
# print the JSON string representation of the object
print(EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner.to_json())

# convert the object into a dict
employees_directory_xml_response_employees_employee_inner_field_inner_dict = employees_directory_xml_response_employees_employee_inner_field_inner_instance.to_dict()
# create an instance of EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner from a dict
employees_directory_xml_response_employees_employee_inner_field_inner_from_dict = EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner.from_dict(employees_directory_xml_response_employees_employee_inner_field_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


