# UnarchiveCustomFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.unarchive_custom_fields_response import UnarchiveCustomFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnarchiveCustomFieldsResponse from a JSON string
unarchive_custom_fields_response_instance = UnarchiveCustomFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(UnarchiveCustomFieldsResponse.to_json())

# convert the object into a dict
unarchive_custom_fields_response_dict = unarchive_custom_fields_response_instance.to_dict()
# create an instance of UnarchiveCustomFieldsResponse from a dict
unarchive_custom_fields_response_from_dict = UnarchiveCustomFieldsResponse.from_dict(unarchive_custom_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


