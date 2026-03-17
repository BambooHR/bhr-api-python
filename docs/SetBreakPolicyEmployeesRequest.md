# SetBreakPolicyEmployeesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_ids** | **List[int]** | Array of employee IDs to assign to the break policy. Replaces all existing assignments. | 

## Example

```python
from bamboohr_sdk.models.set_break_policy_employees_request import SetBreakPolicyEmployeesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetBreakPolicyEmployeesRequest from a JSON string
set_break_policy_employees_request_instance = SetBreakPolicyEmployeesRequest.from_json(json)
# print the JSON string representation of the object
print(SetBreakPolicyEmployeesRequest.to_json())

# convert the object into a dict
set_break_policy_employees_request_dict = set_break_policy_employees_request_instance.to_dict()
# create an instance of SetBreakPolicyEmployeesRequest from a dict
set_break_policy_employees_request_from_dict = SetBreakPolicyEmployeesRequest.from_dict(set_break_policy_employees_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


