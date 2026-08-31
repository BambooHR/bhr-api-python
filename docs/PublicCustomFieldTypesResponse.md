# PublicCustomFieldTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[CustomFieldTypeViewObject]**](CustomFieldTypeViewObject.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.public_custom_field_types_response import PublicCustomFieldTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCustomFieldTypesResponse from a JSON string
public_custom_field_types_response_instance = PublicCustomFieldTypesResponse.from_json(json)
# print the JSON string representation of the object
print(PublicCustomFieldTypesResponse.to_json())

# convert the object into a dict
public_custom_field_types_response_dict = public_custom_field_types_response_instance.to_dict()
# create an instance of PublicCustomFieldTypesResponse from a dict
public_custom_field_types_response_from_dict = PublicCustomFieldTypesResponse.from_dict(public_custom_field_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


