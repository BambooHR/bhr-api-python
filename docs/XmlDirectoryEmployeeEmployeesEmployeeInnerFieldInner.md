# XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Field identifier (XML attribute). Array of employee records. Each employee object contains dynamic field values based on the fields defined in the &#39;fields&#39; array. Common fields include: id, displayName, firstName, lastName, preferredName, jobTitle, workPhone, mobilePhone, workEmail, department, location, division, twitterFeed, pronouns, workPhoneExtension, photoUploaded, photoUrl, canUploadPhoto. Actual fields may vary by company configuration. | [optional] 
**value** | **str** | Field value (element text content) | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_directory_employee_employees_employee_inner_field_inner import XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner

# TODO update the JSON string below
json = "{}"
# create an instance of XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner from a JSON string
xml_directory_employee_employees_employee_inner_field_inner_instance = XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner.from_json(json)
# print the JSON string representation of the object
print(XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner.to_json())

# convert the object into a dict
xml_directory_employee_employees_employee_inner_field_inner_dict = xml_directory_employee_employees_employee_inner_field_inner_instance.to_dict()
# create an instance of XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner from a dict
xml_directory_employee_employees_employee_inner_field_inner_from_dict = XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner.from_dict(xml_directory_employee_employees_employee_inner_field_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


