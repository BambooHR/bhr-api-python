# EmployeeDependentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_dependents** | [**List[EmployeeDependentsResponseEmployeeDependentsInner]**](EmployeeDependentsResponseEmployeeDependentsInner.md) | Array of employee dependent objects. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_dependents_response import EmployeeDependentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeDependentsResponse from a JSON string
employee_dependents_response_instance = EmployeeDependentsResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeDependentsResponse.to_json())

# convert the object into a dict
employee_dependents_response_dict = employee_dependents_response_instance.to_dict()
# create an instance of EmployeeDependentsResponse from a dict
employee_dependents_response_from_dict = EmployeeDependentsResponse.from_dict(employee_dependents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


