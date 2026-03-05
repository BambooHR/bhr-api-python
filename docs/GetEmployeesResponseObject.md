# GetEmployeesResponseObject

Complete response object for employee list API containing employee data, metadata, and navigation links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetEmployeesEmployeeResponse]**](GetEmployeesEmployeeResponse.md) | Typed collection of employee response objects | 
**meta** | [**CursorPagedResponseMetadata**](CursorPagedResponseMetadata.md) | Metadata information including total count and pagination details | 
**links** | [**GetEmployeesResponseObjectLinks**](GetEmployeesResponseObjectLinks.md) |  | 

## Example

```python
from bamboohr_sdk.models.get_employees_response_object import GetEmployeesResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeesResponseObject from a JSON string
get_employees_response_object_instance = GetEmployeesResponseObject.from_json(json)
# print the JSON string representation of the object
print(GetEmployeesResponseObject.to_json())

# convert the object into a dict
get_employees_response_object_dict = get_employees_response_object_instance.to_dict()
# create an instance of GetEmployeesResponseObject from a dict
get_employees_response_object_from_dict = GetEmployeesResponseObject.from_dict(get_employees_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


