# EmployeesDirectoryXmlResponseFieldsetFieldInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Field identifier; matches the &#x60;id&#x60; attribute on each &#x60;&lt;field&gt;&#x60; element inside &#x60;&lt;employee&gt;&#x60;. | [optional] 
**value** | **str** | Human-readable field label, serialized as the element&#39;s text content. | [optional] 

## Example

```python
from bamboohr_sdk.models.employees_directory_xml_response_fieldset_field_inner import EmployeesDirectoryXmlResponseFieldsetFieldInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesDirectoryXmlResponseFieldsetFieldInner from a JSON string
employees_directory_xml_response_fieldset_field_inner_instance = EmployeesDirectoryXmlResponseFieldsetFieldInner.from_json(json)
# print the JSON string representation of the object
print(EmployeesDirectoryXmlResponseFieldsetFieldInner.to_json())

# convert the object into a dict
employees_directory_xml_response_fieldset_field_inner_dict = employees_directory_xml_response_fieldset_field_inner_instance.to_dict()
# create an instance of EmployeesDirectoryXmlResponseFieldsetFieldInner from a dict
employees_directory_xml_response_fieldset_field_inner_from_dict = EmployeesDirectoryXmlResponseFieldsetFieldInner.from_dict(employees_directory_xml_response_fieldset_field_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


