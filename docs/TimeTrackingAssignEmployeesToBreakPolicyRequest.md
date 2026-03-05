# TimeTrackingAssignEmployeesToBreakPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_ids** | **List[int]** | Array of employee IDs to assign to the break policy | 

## Example

```python
from bamboohr_sdk.models.time_tracking_assign_employees_to_break_policy_request import TimeTrackingAssignEmployeesToBreakPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingAssignEmployeesToBreakPolicyRequest from a JSON string
time_tracking_assign_employees_to_break_policy_request_instance = TimeTrackingAssignEmployeesToBreakPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingAssignEmployeesToBreakPolicyRequest.to_json())

# convert the object into a dict
time_tracking_assign_employees_to_break_policy_request_dict = time_tracking_assign_employees_to_break_policy_request_instance.to_dict()
# create an instance of TimeTrackingAssignEmployeesToBreakPolicyRequest from a dict
time_tracking_assign_employees_to_break_policy_request_from_dict = TimeTrackingAssignEmployeesToBreakPolicyRequest.from_dict(time_tracking_assign_employees_to_break_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


