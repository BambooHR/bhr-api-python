# ArchivedCustomFieldsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomFieldDefinitionResponseObject]**](CustomFieldDefinitionResponseObject.md) |  | [optional] 
**meta** | [**PaginationMetaData**](PaginationMetaData.md) | The pagination metadata for the response. | [optional] 
**links** | [**Dict[str, AvailableAction]**](AvailableAction.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.archived_custom_fields_list_response import ArchivedCustomFieldsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivedCustomFieldsListResponse from a JSON string
archived_custom_fields_list_response_instance = ArchivedCustomFieldsListResponse.from_json(json)
# print the JSON string representation of the object
print(ArchivedCustomFieldsListResponse.to_json())

# convert the object into a dict
archived_custom_fields_list_response_dict = archived_custom_fields_list_response_instance.to_dict()
# create an instance of ArchivedCustomFieldsListResponse from a dict
archived_custom_fields_list_response_from_dict = ArchivedCustomFieldsListResponse.from_dict(archived_custom_fields_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


