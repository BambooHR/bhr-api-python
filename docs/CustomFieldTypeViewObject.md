# CustomFieldTypeViewObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Custom Field Type | [optional] 
**type** | **str** | The type of the Custom Field Type | [optional] 
**label** | **str** | The label of the Custom Field Type | [optional] 

## Example

```python
from bamboohr_sdk.models.custom_field_type_view_object import CustomFieldTypeViewObject

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldTypeViewObject from a JSON string
custom_field_type_view_object_instance = CustomFieldTypeViewObject.from_json(json)
# print the JSON string representation of the object
print(CustomFieldTypeViewObject.to_json())

# convert the object into a dict
custom_field_type_view_object_dict = custom_field_type_view_object_instance.to_dict()
# create an instance of CustomFieldTypeViewObject from a dict
custom_field_type_view_object_from_dict = CustomFieldTypeViewObject.from_dict(custom_field_type_view_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


