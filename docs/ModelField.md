# ModelField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Machine-readable field identifier. Use this value in the &#x60;fields&#x60; array when querying data. | [optional] 
**label** | **str** | Human-readable display name for the field. | [optional] 
**parent_type** | **str** | The type of the parent section (e.g. &#x60;page&#x60;, &#x60;table&#x60;). | [optional] 
**parent_name** | **str** | The name of the parent section this field belongs to. | [optional] 
**entity_name** | **str** | The entity name for the field, used in &#x60;showHistory&#x60; when querying historical table fields. | [optional] 

## Example

```python
from bamboohr_sdk.models.model_field import ModelField

# TODO update the JSON string below
json = "{}"
# create an instance of ModelField from a JSON string
model_field_instance = ModelField.from_json(json)
# print the JSON string representation of the object
print(ModelField.to_json())

# convert the object into a dict
model_field_dict = model_field_instance.to_dict()
# create an instance of ModelField from a dict
model_field_from_dict = ModelField.from_dict(model_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


