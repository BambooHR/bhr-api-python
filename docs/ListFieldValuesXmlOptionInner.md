# ListFieldValuesXmlOptionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The existing option ID. Omit to create a new option. Required when archiving. | [optional] 
**value** | **str** | The display value for the option. In XML format, this is the text content of the &lt;option&gt; element. | [optional] 
**archived** | **str** | Whether to archive this option. Use yes to soft-delete or no to reactivate. | [optional] 
**adp_code** | **str** | Optional payroll-mapping code. | [optional] 

## Example

```python
from bamboohr_sdk.models.list_field_values_xml_option_inner import ListFieldValuesXmlOptionInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListFieldValuesXmlOptionInner from a JSON string
list_field_values_xml_option_inner_instance = ListFieldValuesXmlOptionInner.from_json(json)
# print the JSON string representation of the object
print(ListFieldValuesXmlOptionInner.to_json())

# convert the object into a dict
list_field_values_xml_option_inner_dict = list_field_values_xml_option_inner_instance.to_dict()
# create an instance of ListFieldValuesXmlOptionInner from a dict
list_field_values_xml_option_inner_from_dict = ListFieldValuesXmlOptionInner.from_dict(list_field_values_xml_option_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


