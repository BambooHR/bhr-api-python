# ListValueViewObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The string list value ID. | [optional] 
**legacy_id** | **int** | The legacy numeric list value ID. | [optional] 
**display** | **str** | List value display name. | [optional] 

## Example

```python
from bamboohr_sdk.models.list_value_view_object import ListValueViewObject

# TODO update the JSON string below
json = "{}"
# create an instance of ListValueViewObject from a JSON string
list_value_view_object_instance = ListValueViewObject.from_json(json)
# print the JSON string representation of the object
print(ListValueViewObject.to_json())

# convert the object into a dict
list_value_view_object_dict = list_value_view_object_instance.to_dict()
# create an instance of ListValueViewObject from a dict
list_value_view_object_from_dict = ListValueViewObject.from_dict(list_value_view_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


