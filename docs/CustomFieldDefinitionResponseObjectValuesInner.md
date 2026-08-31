# CustomFieldDefinitionResponseObjectValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The string list value ID. | [optional] 
**legacy_id** | **int** | The legacy numeric list value ID. | [optional] 
**display** | **str** | The list value display name. | [optional] 

## Example

```python
from bamboohr_sdk.models.custom_field_definition_response_object_values_inner import CustomFieldDefinitionResponseObjectValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDefinitionResponseObjectValuesInner from a JSON string
custom_field_definition_response_object_values_inner_instance = CustomFieldDefinitionResponseObjectValuesInner.from_json(json)
# print the JSON string representation of the object
print(CustomFieldDefinitionResponseObjectValuesInner.to_json())

# convert the object into a dict
custom_field_definition_response_object_values_inner_dict = custom_field_definition_response_object_values_inner_instance.to_dict()
# create an instance of CustomFieldDefinitionResponseObjectValuesInner from a dict
custom_field_definition_response_object_values_inner_from_dict = CustomFieldDefinitionResponseObjectValuesInner.from_dict(custom_field_definition_response_object_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


