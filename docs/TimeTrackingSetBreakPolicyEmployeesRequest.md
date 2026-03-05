# TimeTrackingSetBreakPolicyEmployeesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_ids** | **List[int]** |  | 

## Example

```python
from bamboohr_sdk.models.time_tracking_set_break_policy_employees_request import TimeTrackingSetBreakPolicyEmployeesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingSetBreakPolicyEmployeesRequest from a JSON string
time_tracking_set_break_policy_employees_request_instance = TimeTrackingSetBreakPolicyEmployeesRequest.from_json(json)
# print the JSON string representation of the object
print(TimeTrackingSetBreakPolicyEmployeesRequest.to_json())

# convert the object into a dict
time_tracking_set_break_policy_employees_request_dict = time_tracking_set_break_policy_employees_request_instance.to_dict()
# create an instance of TimeTrackingSetBreakPolicyEmployeesRequest from a dict
time_tracking_set_break_policy_employees_request_from_dict = TimeTrackingSetBreakPolicyEmployeesRequest.from_dict(time_tracking_set_break_policy_employees_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


