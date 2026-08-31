# CreatedTimeOffRequestType

The time off type for this request. Only present when the underlying time off type record could be loaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The time off type ID. | [optional] 
**name** | **str** | The time off type name. | [optional] 

## Example

```python
from bamboohr_sdk.models.created_time_off_request_type import CreatedTimeOffRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedTimeOffRequestType from a JSON string
created_time_off_request_type_instance = CreatedTimeOffRequestType.from_json(json)
# print the JSON string representation of the object
print(CreatedTimeOffRequestType.to_json())

# convert the object into a dict
created_time_off_request_type_dict = created_time_off_request_type_instance.to_dict()
# create an instance of CreatedTimeOffRequestType from a dict
created_time_off_request_type_from_dict = CreatedTimeOffRequestType.from_dict(created_time_off_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


