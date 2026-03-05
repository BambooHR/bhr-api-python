# JsonDirectoryEmployeeFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Field identifier | [optional] 
**type** | **str** | Field data type | [optional] 
**name** | **str** | Field display name | [optional] 

## Example

```python
from bamboohr_sdk.models.json_directory_employee_fields_inner import JsonDirectoryEmployeeFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDirectoryEmployeeFieldsInner from a JSON string
json_directory_employee_fields_inner_instance = JsonDirectoryEmployeeFieldsInner.from_json(json)
# print the JSON string representation of the object
print(JsonDirectoryEmployeeFieldsInner.to_json())

# convert the object into a dict
json_directory_employee_fields_inner_dict = json_directory_employee_fields_inner_instance.to_dict()
# create an instance of JsonDirectoryEmployeeFieldsInner from a dict
json_directory_employee_fields_inner_from_dict = JsonDirectoryEmployeeFieldsInner.from_dict(json_directory_employee_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


