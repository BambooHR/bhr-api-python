# CustomFieldDefinitionResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The string custom field or custom table ID. | [optional] 
**legacy_id** | **int** | The legacy numeric custom field or custom table ID. | [optional] 
**name** | **str** | The custom field or custom table name. | [optional] 
**type** | **str** | The custom field or custom table type. | [optional] 
**is_encrypted** | **bool** | Whether the custom field is encrypted. | [optional] 
**is_calculated** | **bool** | Whether the custom field is calculated. | [optional] 
**is_required** | **bool** | Whether the custom field is required. | [optional] 
**order** | **int** |  | [optional] 
**page_id** | **str** |  | [optional] 
**page_legacy_id** | **int** |  | [optional] 
**section_id** | **str** |  | [optional] 
**section_legacy_id** | **int** |  | [optional] 
**custom_table_id** | **str** |  | [optional] 
**custom_table_legacy_id** | **int** |  | [optional] 
**sort_order_direction** | **str** |  | [optional] 
**summarize** | **str** |  | [optional] 
**sort_field** | **bool** |  | [optional] 
**values** | [**List[CustomFieldDefinitionResponseObjectValuesInner]**](CustomFieldDefinitionResponseObjectValuesInner.md) |  | [optional] 
**fields** | [**List[CustomFieldDefinitionResponseObject]**](CustomFieldDefinitionResponseObject.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.custom_field_definition_response_object import CustomFieldDefinitionResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDefinitionResponseObject from a JSON string
custom_field_definition_response_object_instance = CustomFieldDefinitionResponseObject.from_json(json)
# print the JSON string representation of the object
print(CustomFieldDefinitionResponseObject.to_json())

# convert the object into a dict
custom_field_definition_response_object_dict = custom_field_definition_response_object_instance.to_dict()
# create an instance of CustomFieldDefinitionResponseObject from a dict
custom_field_definition_response_object_from_dict = CustomFieldDefinitionResponseObject.from_dict(custom_field_definition_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


