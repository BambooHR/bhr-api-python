# CustomFieldViewObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the Custom Field | [optional] 
**name** | **str** | The name of the Custom Field | [optional] 
**type** | **str** | The type of the Custom Field | [optional] 
**is_encrypted** | **bool** | Whether the Custom Field is encrypted or not | [optional] 
**is_calculated** | **bool** | Whether the Custom Field is calculated or not | [optional] 
**is_required** | **bool** | Whether the Custom Field is required or not | [optional] 
**order** | **int** | The order of the Custom Field | [optional] 
**values** | **List[str]** | The values of the Custom Field | [optional] 

## Example

```python
from bamboohr_sdk.models.custom_field_view_object import CustomFieldViewObject

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldViewObject from a JSON string
custom_field_view_object_instance = CustomFieldViewObject.from_json(json)
# print the JSON string representation of the object
print(CustomFieldViewObject.to_json())

# convert the object into a dict
custom_field_view_object_dict = custom_field_view_object_instance.to_dict()
# create an instance of CustomFieldViewObject from a dict
custom_field_view_object_from_dict = CustomFieldViewObject.from_dict(custom_field_view_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


