# EmployeesDirectoryXmlResponseEmployeesEmployeeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee ID, serialized as an attribute on the &#x60;&lt;employee&gt;&#x60; element. | [optional] 
**var_field** | [**List[EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner]**](EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner.md) | Field values for the employee. Each &#x60;&lt;field&gt;&#x60; element has an &#x60;id&#x60; attribute matching one of the &#x60;&lt;fieldset&gt;&#x60; ids and the value as element text. Currency fields additionally carry a &#x60;currency&#x60; attribute (ISO currency code). Boolean fields are serialized as the strings &#x60;true&#x60;/&#x60;false&#x60;; the appended &#x60;canUploadPhoto&#x60; field is serialized as &#x60;yes&#x60;/&#x60;no&#x60;. | [optional] 

## Example

```python
from bamboohr_sdk.models.employees_directory_xml_response_employees_employee_inner import EmployeesDirectoryXmlResponseEmployeesEmployeeInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesDirectoryXmlResponseEmployeesEmployeeInner from a JSON string
employees_directory_xml_response_employees_employee_inner_instance = EmployeesDirectoryXmlResponseEmployeesEmployeeInner.from_json(json)
# print the JSON string representation of the object
print(EmployeesDirectoryXmlResponseEmployeesEmployeeInner.to_json())

# convert the object into a dict
employees_directory_xml_response_employees_employee_inner_dict = employees_directory_xml_response_employees_employee_inner_instance.to_dict()
# create an instance of EmployeesDirectoryXmlResponseEmployeesEmployeeInner from a dict
employees_directory_xml_response_employees_employee_inner_from_dict = EmployeesDirectoryXmlResponseEmployeesEmployeeInner.from_dict(employees_directory_xml_response_employees_employee_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


