# InlineObject1EmployeesInner

Employees that can be synced with the integration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | First and last name | [optional] 
**id** | **int** | ID | [optional] 

## Example

```python
from bamboohr_sdk.models.inline_object1_employees_inner import InlineObject1EmployeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject1EmployeesInner from a JSON string
inline_object1_employees_inner_instance = InlineObject1EmployeesInner.from_json(json)
# print the JSON string representation of the object
print(InlineObject1EmployeesInner.to_json())

# convert the object into a dict
inline_object1_employees_inner_dict = inline_object1_employees_inner_instance.to_dict()
# create an instance of InlineObject1EmployeesInner from a dict
inline_object1_employees_inner_from_dict = InlineObject1EmployeesInner.from_dict(inline_object1_employees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


