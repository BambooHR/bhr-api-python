# AddCustomFieldListValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **str** | A single new list value. | [optional] 
**values** | **List[Optional[str]]** | Multiple new list values. | [optional] 

## Example

```python
from bamboohr_sdk.models.add_custom_field_list_value_request import AddCustomFieldListValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomFieldListValueRequest from a JSON string
add_custom_field_list_value_request_instance = AddCustomFieldListValueRequest.from_json(json)
# print the JSON string representation of the object
print(AddCustomFieldListValueRequest.to_json())

# convert the object into a dict
add_custom_field_list_value_request_dict = add_custom_field_list_value_request_instance.to_dict()
# create an instance of AddCustomFieldListValueRequest from a dict
add_custom_field_list_value_request_from_dict = AddCustomFieldListValueRequest.from_dict(add_custom_field_list_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


