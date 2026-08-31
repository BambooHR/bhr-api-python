# UnarchiveCustomFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | **List[int]** |  | 
**tab** | **int** |  | 
**section** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.unarchive_custom_fields_request import UnarchiveCustomFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnarchiveCustomFieldsRequest from a JSON string
unarchive_custom_fields_request_instance = UnarchiveCustomFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(UnarchiveCustomFieldsRequest.to_json())

# convert the object into a dict
unarchive_custom_fields_request_dict = unarchive_custom_fields_request_instance.to_dict()
# create an instance of UnarchiveCustomFieldsRequest from a dict
unarchive_custom_fields_request_from_dict = UnarchiveCustomFieldsRequest.from_dict(unarchive_custom_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


