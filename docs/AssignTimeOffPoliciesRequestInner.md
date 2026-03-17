# AssignTimeOffPoliciesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_off_policy_id** | **int** | The ID of the time off policy to assign. | 
**accrual_start_date** | **date** | The date accruals should start in YYYY-MM-DD format. Set to null to remove an existing assignment. | 

## Example

```python
from bamboohr_sdk.models.assign_time_off_policies_request_inner import AssignTimeOffPoliciesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssignTimeOffPoliciesRequestInner from a JSON string
assign_time_off_policies_request_inner_instance = AssignTimeOffPoliciesRequestInner.from_json(json)
# print the JSON string representation of the object
print(AssignTimeOffPoliciesRequestInner.to_json())

# convert the object into a dict
assign_time_off_policies_request_inner_dict = assign_time_off_policies_request_inner_instance.to_dict()
# create an instance of AssignTimeOffPoliciesRequestInner from a dict
assign_time_off_policies_request_inner_from_dict = AssignTimeOffPoliciesRequestInner.from_dict(assign_time_off_policies_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


