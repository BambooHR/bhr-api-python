# ListFieldValues

Payload for creating, updating, or archiving options on a list field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**List[ListFieldValuesOptionsInner]**](ListFieldValuesOptionsInner.md) | The list field options to create, update, or archive. | [optional] 

## Example

```python
from bamboohr_sdk.models.list_field_values import ListFieldValues

# TODO update the JSON string below
json = "{}"
# create an instance of ListFieldValues from a JSON string
list_field_values_instance = ListFieldValues.from_json(json)
# print the JSON string representation of the object
print(ListFieldValues.to_json())

# convert the object into a dict
list_field_values_dict = list_field_values_instance.to_dict()
# create an instance of ListFieldValues from a dict
list_field_values_from_dict = ListFieldValues.from_dict(list_field_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


