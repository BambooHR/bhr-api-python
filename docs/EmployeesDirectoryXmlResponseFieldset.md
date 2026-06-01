# EmployeesDirectoryXmlResponseFieldset

Field definitions included in this response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | [**List[EmployeesDirectoryXmlResponseFieldsetFieldInner]**](EmployeesDirectoryXmlResponseFieldsetFieldInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employees_directory_xml_response_fieldset import EmployeesDirectoryXmlResponseFieldset

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesDirectoryXmlResponseFieldset from a JSON string
employees_directory_xml_response_fieldset_instance = EmployeesDirectoryXmlResponseFieldset.from_json(json)
# print the JSON string representation of the object
print(EmployeesDirectoryXmlResponseFieldset.to_json())

# convert the object into a dict
employees_directory_xml_response_fieldset_dict = employees_directory_xml_response_fieldset_instance.to_dict()
# create an instance of EmployeesDirectoryXmlResponseFieldset from a dict
employees_directory_xml_response_fieldset_from_dict = EmployeesDirectoryXmlResponseFieldset.from_dict(employees_directory_xml_response_fieldset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


