# UnassignEmployeesFromBreakPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_ids** | **List[int]** | Array of employee IDs to unassign from the break policy | 

## Example

```python
from bamboohr_sdk.models.unassign_employees_from_break_policy_request import UnassignEmployeesFromBreakPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignEmployeesFromBreakPolicyRequest from a JSON string
unassign_employees_from_break_policy_request_instance = UnassignEmployeesFromBreakPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(UnassignEmployeesFromBreakPolicyRequest.to_json())

# convert the object into a dict
unassign_employees_from_break_policy_request_dict = unassign_employees_from_break_policy_request_instance.to_dict()
# create an instance of UnassignEmployeesFromBreakPolicyRequest from a dict
unassign_employees_from_break_policy_request_from_dict = UnassignEmployeesFromBreakPolicyRequest.from_dict(unassign_employees_from_break_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


