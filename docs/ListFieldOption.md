# ListFieldOption

A single option on a list field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The option ID. | [optional] 
**name** | **str** | The display value of the option. In XML format, this is the text content of the &lt;option&gt; element. | [optional] 
**archived** | **str** | Whether this option is archived. Archived options are preserved for historical data integrity and continue to appear in responses. Filter by archived: no to show only active options. | [optional] 
**created_date** | **str** |  | [optional] 
**archived_date** | **str** |  | [optional] 
**manageable** | **str** | Whether this individual option can be modified via the API. | [optional] 
**frequency** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.list_field_option import ListFieldOption

# TODO update the JSON string below
json = "{}"
# create an instance of ListFieldOption from a JSON string
list_field_option_instance = ListFieldOption.from_json(json)
# print the JSON string representation of the object
print(ListFieldOption.to_json())

# convert the object into a dict
list_field_option_dict = list_field_option_instance.to_dict()
# create an instance of ListFieldOption from a dict
list_field_option_from_dict = ListFieldOption.from_dict(list_field_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


