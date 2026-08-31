# CustomFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Custom Field to be edited | [optional] 
**name** | **str** | The name of the Custom Field to be edited / created | [optional] 
**type** | **str** | The type of the Custom Field to be edited / created | [optional] 
**tab** | **int** | The id of the tab where the Custom Field will be added | [optional] 
**section** | **int** | The id of the section where the Custom Field will be added | [optional] 
**required** | **bool** | Whether the Custom Field is required or not | [optional] 
**options** | **List[str]** | The options of the Custom Field to be edited / created | [optional] 

## Example

```python
from bamboohr_sdk.models.custom_field_request import CustomFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldRequest from a JSON string
custom_field_request_instance = CustomFieldRequest.from_json(json)
# print the JSON string representation of the object
print(CustomFieldRequest.to_json())

# convert the object into a dict
custom_field_request_dict = custom_field_request_instance.to_dict()
# create an instance of CustomFieldRequest from a dict
custom_field_request_from_dict = CustomFieldRequest.from_dict(custom_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


