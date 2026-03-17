# XmlEmployeeFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Employee ID on the root &#x60;&lt;employee&gt;&#x60; element. | [optional] 
**category** | [**List[XmlEmployeeFilesCategoryInner]**](XmlEmployeeFilesCategoryInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.xml_employee_files import XmlEmployeeFiles

# TODO update the JSON string below
json = "{}"
# create an instance of XmlEmployeeFiles from a JSON string
xml_employee_files_instance = XmlEmployeeFiles.from_json(json)
# print the JSON string representation of the object
print(XmlEmployeeFiles.to_json())

# convert the object into a dict
xml_employee_files_dict = xml_employee_files_instance.to_dict()
# create an instance of XmlEmployeeFiles from a dict
xml_employee_files_from_dict = XmlEmployeeFiles.from_dict(xml_employee_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


