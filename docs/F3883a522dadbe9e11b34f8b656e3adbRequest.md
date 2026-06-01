# F3883a522dadbe9e11b34f8b656e3adbRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | The ID of the employee receiving the recommendation | 
**assignee_employee_id** | **str** | The ID of the employee making the recommendation | 
**approval_flow_id** | **int** | The ID of the approval flow | [optional] 
**approval_stage** | **int** | The approval stage | 
**rec_salary_increase** | **object** |  | [optional] 
**rec_bonus_increase** | **object** |  | [optional] 
**rec_equity_increase** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.f3883a522dadbe9e11b34f8b656e3adb_request import F3883a522dadbe9e11b34f8b656e3adbRequest

# TODO update the JSON string below
json = "{}"
# create an instance of F3883a522dadbe9e11b34f8b656e3adbRequest from a JSON string
f3883a522dadbe9e11b34f8b656e3adb_request_instance = F3883a522dadbe9e11b34f8b656e3adbRequest.from_json(json)
# print the JSON string representation of the object
print(F3883a522dadbe9e11b34f8b656e3adbRequest.to_json())

# convert the object into a dict
f3883a522dadbe9e11b34f8b656e3adb_request_dict = f3883a522dadbe9e11b34f8b656e3adb_request_instance.to_dict()
# create an instance of F3883a522dadbe9e11b34f8b656e3adbRequest from a dict
f3883a522dadbe9e11b34f8b656e3adb_request_from_dict = F3883a522dadbe9e11b34f8b656e3adbRequest.from_dict(f3883a522dadbe9e11b34f8b656e3adb_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


