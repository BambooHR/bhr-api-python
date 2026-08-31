# PublicListValuesCustomFieldSettingsResponseValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The string list value ID. | [optional] 
**legacy_id** | **int** | The legacy numeric list value ID. | [optional] 
**display** | **str** | The list value display name. | [optional] 
**count** | **int** | The number of employees using the list value. | [optional] 

## Example

```python
from bamboohr_sdk.models.public_list_values_custom_field_settings_response_values_inner import PublicListValuesCustomFieldSettingsResponseValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicListValuesCustomFieldSettingsResponseValuesInner from a JSON string
public_list_values_custom_field_settings_response_values_inner_instance = PublicListValuesCustomFieldSettingsResponseValuesInner.from_json(json)
# print the JSON string representation of the object
print(PublicListValuesCustomFieldSettingsResponseValuesInner.to_json())

# convert the object into a dict
public_list_values_custom_field_settings_response_values_inner_dict = public_list_values_custom_field_settings_response_values_inner_instance.to_dict()
# create an instance of PublicListValuesCustomFieldSettingsResponseValuesInner from a dict
public_list_values_custom_field_settings_response_values_inner_from_dict = PublicListValuesCustomFieldSettingsResponseValuesInner.from_dict(public_list_values_custom_field_settings_response_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


