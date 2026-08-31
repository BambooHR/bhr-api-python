# PublicListValuesCustomFieldSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The string custom field ID. | [optional] 
**legacy_id** | **int** | The legacy numeric custom field ID. | [optional] 
**name** | **str** | The custom field name. | [optional] 
**type** | **str** | The custom field type. | [optional] 
**is_encrypted** | **bool** | Whether the custom field is encrypted. | [optional] 
**is_calculated** | **bool** | Whether the custom field is calculated. | [optional] 
**is_required** | **bool** | Whether the custom field is required. | [optional] 
**summarize** | **str** | The custom field summary setting. | [optional] 
**values** | [**List[PublicListValuesCustomFieldSettingsResponseValuesInner]**](PublicListValuesCustomFieldSettingsResponseValuesInner.md) | The list values and the number of employees using each value. | [optional] 

## Example

```python
from bamboohr_sdk.models.public_list_values_custom_field_settings_response import PublicListValuesCustomFieldSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicListValuesCustomFieldSettingsResponse from a JSON string
public_list_values_custom_field_settings_response_instance = PublicListValuesCustomFieldSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(PublicListValuesCustomFieldSettingsResponse.to_json())

# convert the object into a dict
public_list_values_custom_field_settings_response_dict = public_list_values_custom_field_settings_response_instance.to_dict()
# create an instance of PublicListValuesCustomFieldSettingsResponse from a dict
public_list_values_custom_field_settings_response_from_dict = PublicListValuesCustomFieldSettingsResponse.from_dict(public_list_values_custom_field_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


