# EmployeeTimeOffPolicyAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_off_policy_id** | **int** | The ID of the assigned time off policy. | [optional] 
**time_off_type_id** | **int** | The ID of the time off type. | [optional] 
**accrual_start_date** | **date** | The date accruals started in YYYY-MM-DD format. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_time_off_policy_assignment import EmployeeTimeOffPolicyAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTimeOffPolicyAssignment from a JSON string
employee_time_off_policy_assignment_instance = EmployeeTimeOffPolicyAssignment.from_json(json)
# print the JSON string representation of the object
print(EmployeeTimeOffPolicyAssignment.to_json())

# convert the object into a dict
employee_time_off_policy_assignment_dict = employee_time_off_policy_assignment_instance.to_dict()
# create an instance of EmployeeTimeOffPolicyAssignment from a dict
employee_time_off_policy_assignment_from_dict = EmployeeTimeOffPolicyAssignment.from_dict(employee_time_off_policy_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


