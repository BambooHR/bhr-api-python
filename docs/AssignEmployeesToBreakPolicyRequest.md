# AssignEmployeesToBreakPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_ids** | **List[int]** | Array of employee IDs to assign to the break policy | 

## Example

```python
from bamboohr_sdk.models.assign_employees_to_break_policy_request import AssignEmployeesToBreakPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignEmployeesToBreakPolicyRequest from a JSON string
assign_employees_to_break_policy_request_instance = AssignEmployeesToBreakPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(AssignEmployeesToBreakPolicyRequest.to_json())

# convert the object into a dict
assign_employees_to_break_policy_request_dict = assign_employees_to_break_policy_request_instance.to_dict()
# create an instance of AssignEmployeesToBreakPolicyRequest from a dict
assign_employees_to_break_policy_request_from_dict = AssignEmployeesToBreakPolicyRequest.from_dict(assign_employees_to_break_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


