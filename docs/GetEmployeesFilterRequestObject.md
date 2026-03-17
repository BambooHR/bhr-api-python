# GetEmployeesFilterRequestObject

Filter criteria for the employee list endpoint. All filter fields are optional. Multiple fields are combined with AND logic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | This will match any employees whose first name contains this string (case insensitive) | [optional] 
**last_name** | **str** | This will match any employees whose last name contains this string (case insensitive) | [optional] 
**job_title_name** | **str** | This will match any employees whose current job title descriptor contains this string (case insensitive) | [optional] 
**status** | **str** | Employee status | [optional] 
**ids** | **List[int]** | List of employee IDs for batch fetch. Accepts repeated keys (filter[ids][]&#x3D;123&amp;filter[ids][]&#x3D;124) or a single comma-separated string (filter[ids]&#x3D;123,124). | [optional] 

## Example

```python
from bamboohr_sdk.models.get_employees_filter_request_object import GetEmployeesFilterRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeesFilterRequestObject from a JSON string
get_employees_filter_request_object_instance = GetEmployeesFilterRequestObject.from_json(json)
# print the JSON string representation of the object
print(GetEmployeesFilterRequestObject.to_json())

# convert the object into a dict
get_employees_filter_request_object_dict = get_employees_filter_request_object_instance.to_dict()
# create an instance of GetEmployeesFilterRequestObject from a dict
get_employees_filter_request_object_from_dict = GetEmployeesFilterRequestObject.from_dict(get_employees_filter_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


