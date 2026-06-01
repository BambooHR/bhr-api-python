# EmployeesDirectoryJsonResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Field identifier; appears as a key on each employee object. | [optional] 
**type** | **str** | Field data type. Observed values include &#x60;text&#x60;, &#x60;list&#x60;, &#x60;email&#x60;, &#x60;bool&#x60;, &#x60;url&#x60;, and &#x60;employee&#x60;. | [optional] 
**name** | **str** | Human-readable field label. | [optional] 

## Example

```python
from bamboohr_sdk.models.employees_directory_json_response_fields_inner import EmployeesDirectoryJsonResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesDirectoryJsonResponseFieldsInner from a JSON string
employees_directory_json_response_fields_inner_instance = EmployeesDirectoryJsonResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(EmployeesDirectoryJsonResponseFieldsInner.to_json())

# convert the object into a dict
employees_directory_json_response_fields_inner_dict = employees_directory_json_response_fields_inner_instance.to_dict()
# create an instance of EmployeesDirectoryJsonResponseFieldsInner from a dict
employees_directory_json_response_fields_inner_from_dict = EmployeesDirectoryJsonResponseFieldsInner.from_dict(employees_directory_json_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


