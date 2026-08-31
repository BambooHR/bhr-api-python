# EmployeeVerificationsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_verifications** | [**List[EmployeeVerificationPublicApiRecord]**](EmployeeVerificationPublicApiRecord.md) | Verification records for the employee, newest first. | 

## Example

```python
from bamboohr_sdk.models.employee_verifications_list_response import EmployeeVerificationsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeVerificationsListResponse from a JSON string
employee_verifications_list_response_instance = EmployeeVerificationsListResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeVerificationsListResponse.to_json())

# convert the object into a dict
employee_verifications_list_response_dict = employee_verifications_list_response_instance.to_dict()
# create an instance of EmployeeVerificationsListResponse from a dict
employee_verifications_list_response_from_dict = EmployeeVerificationsListResponse.from_dict(employee_verifications_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


