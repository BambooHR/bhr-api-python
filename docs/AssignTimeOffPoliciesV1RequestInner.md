# AssignTimeOffPoliciesV1RequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_off_policy_id** | **int** | The ID of the time off policy to assign. | 
**accrual_start_date** | **date** |  | 

## Example

```python
from bamboohr_sdk.models.assign_time_off_policies_v1_request_inner import AssignTimeOffPoliciesV1RequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssignTimeOffPoliciesV1RequestInner from a JSON string
assign_time_off_policies_v1_request_inner_instance = AssignTimeOffPoliciesV1RequestInner.from_json(json)
# print the JSON string representation of the object
print(AssignTimeOffPoliciesV1RequestInner.to_json())

# convert the object into a dict
assign_time_off_policies_v1_request_inner_dict = assign_time_off_policies_v1_request_inner_instance.to_dict()
# create an instance of AssignTimeOffPoliciesV1RequestInner from a dict
assign_time_off_policies_v1_request_inner_from_dict = AssignTimeOffPoliciesV1RequestInner.from_dict(assign_time_off_policies_v1_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


