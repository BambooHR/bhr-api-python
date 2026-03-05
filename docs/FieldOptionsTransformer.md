# FieldOptionsTransformer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the field option | [optional] 
**value** | **str** | The value of the field option | [optional] 

## Example

```python
from bamboohr_sdk.models.field_options_transformer import FieldOptionsTransformer

# TODO update the JSON string below
json = "{}"
# create an instance of FieldOptionsTransformer from a JSON string
field_options_transformer_instance = FieldOptionsTransformer.from_json(json)
# print the JSON string representation of the object
print(FieldOptionsTransformer.to_json())

# convert the object into a dict
field_options_transformer_dict = field_options_transformer_instance.to_dict()
# create an instance of FieldOptionsTransformer from a dict
field_options_transformer_from_dict = FieldOptionsTransformer.from_dict(field_options_transformer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


