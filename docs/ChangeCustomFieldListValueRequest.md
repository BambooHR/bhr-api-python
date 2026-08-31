# ChangeCustomFieldListValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **str** | The new list value | [optional] 
**preserve_existing_option** | **bool** | Whether to preserve the existing option or not | [optional] 

## Example

```python
from bamboohr_sdk.models.change_custom_field_list_value_request import ChangeCustomFieldListValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeCustomFieldListValueRequest from a JSON string
change_custom_field_list_value_request_instance = ChangeCustomFieldListValueRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeCustomFieldListValueRequest.to_json())

# convert the object into a dict
change_custom_field_list_value_request_dict = change_custom_field_list_value_request_instance.to_dict()
# create an instance of ChangeCustomFieldListValueRequest from a dict
change_custom_field_list_value_request_from_dict = ChangeCustomFieldListValueRequest.from_dict(change_custom_field_list_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


