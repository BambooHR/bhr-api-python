# EmployeesDirectoryXmlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldset** | [**EmployeesDirectoryXmlResponseFieldset**](EmployeesDirectoryXmlResponseFieldset.md) |  | [optional] 
**employees** | [**EmployeesDirectoryXmlResponseEmployees**](EmployeesDirectoryXmlResponseEmployees.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employees_directory_xml_response import EmployeesDirectoryXmlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesDirectoryXmlResponse from a JSON string
employees_directory_xml_response_instance = EmployeesDirectoryXmlResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesDirectoryXmlResponse.to_json())

# convert the object into a dict
employees_directory_xml_response_dict = employees_directory_xml_response_instance.to_dict()
# create an instance of EmployeesDirectoryXmlResponse from a dict
employees_directory_xml_response_from_dict = EmployeesDirectoryXmlResponse.from_dict(employees_directory_xml_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


