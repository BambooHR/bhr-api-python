# AddCustomFieldListValueResponseOneOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The string list value ID. | [optional] 
**legacy_id** | **int** | The legacy numeric list value ID. | [optional] 
**display** | **str** | List value display name. | [optional] 

## Example

```python
from bamboohr_sdk.models.add_custom_field_list_value_response_one_of_inner import AddCustomFieldListValueResponseOneOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomFieldListValueResponseOneOfInner from a JSON string
add_custom_field_list_value_response_one_of_inner_instance = AddCustomFieldListValueResponseOneOfInner.from_json(json)
# print the JSON string representation of the object
print(AddCustomFieldListValueResponseOneOfInner.to_json())

# convert the object into a dict
add_custom_field_list_value_response_one_of_inner_dict = add_custom_field_list_value_response_one_of_inner_instance.to_dict()
# create an instance of AddCustomFieldListValueResponseOneOfInner from a dict
add_custom_field_list_value_response_one_of_inner_from_dict = AddCustomFieldListValueResponseOneOfInner.from_dict(add_custom_field_list_value_response_one_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


