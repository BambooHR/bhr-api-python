# ListFieldValuesXml

XML payload for creating, updating, or archiving options on a list field. The root element is <options>, containing one or more <option> elements. Each <option> element carries optional id, archived, and adpCode XML attributes; the display value is the text content of the element.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | [**List[ListFieldValuesXmlOptionInner]**](ListFieldValuesXmlOptionInner.md) | One or more options to create, update, or archive. | [optional] 

## Example

```python
from bamboohr_sdk.models.list_field_values_xml import ListFieldValuesXml

# TODO update the JSON string below
json = "{}"
# create an instance of ListFieldValuesXml from a JSON string
list_field_values_xml_instance = ListFieldValuesXml.from_json(json)
# print the JSON string representation of the object
print(ListFieldValuesXml.to_json())

# convert the object into a dict
list_field_values_xml_dict = list_field_values_xml_instance.to_dict()
# create an instance of ListFieldValuesXml from a dict
list_field_values_xml_from_dict = ListFieldValuesXml.from_dict(list_field_values_xml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


