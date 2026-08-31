# EmployeeTimeOffRequestApproverResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID of the approver | 
**display_name** | **str** | Display name of the approver | 
**employee_id** | **int** | Employee ID of the approver | 
**photo_url** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_time_off_request_approver_response_inner import EmployeeTimeOffRequestApproverResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTimeOffRequestApproverResponseInner from a JSON string
employee_time_off_request_approver_response_inner_instance = EmployeeTimeOffRequestApproverResponseInner.from_json(json)
# print the JSON string representation of the object
print(EmployeeTimeOffRequestApproverResponseInner.to_json())

# convert the object into a dict
employee_time_off_request_approver_response_inner_dict = employee_time_off_request_approver_response_inner_instance.to_dict()
# create an instance of EmployeeTimeOffRequestApproverResponseInner from a dict
employee_time_off_request_approver_response_inner_from_dict = EmployeeTimeOffRequestApproverResponseInner.from_dict(employee_time_off_request_approver_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


