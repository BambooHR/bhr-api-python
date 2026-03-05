# FieldListFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.field_list_fields_inner import FieldListFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FieldListFieldsInner from a JSON string
field_list_fields_inner_instance = FieldListFieldsInner.from_json(json)
# print the JSON string representation of the object
print(FieldListFieldsInner.to_json())

# convert the object into a dict
field_list_fields_inner_dict = field_list_fields_inner_instance.to_dict()
# create an instance of FieldListFieldsInner from a dict
field_list_fields_inner_from_dict = FieldListFieldsInner.from_dict(field_list_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


