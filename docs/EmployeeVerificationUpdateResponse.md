# EmployeeVerificationUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_verification** | [**EmployeeVerificationPublicApiRecord**](EmployeeVerificationPublicApiRecord.md) |  | 

## Example

```python
from bamboohr_sdk.models.employee_verification_update_response import EmployeeVerificationUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeVerificationUpdateResponse from a JSON string
employee_verification_update_response_instance = EmployeeVerificationUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeVerificationUpdateResponse.to_json())

# convert the object into a dict
employee_verification_update_response_dict = employee_verification_update_response_instance.to_dict()
# create an instance of EmployeeVerificationUpdateResponse from a dict
employee_verification_update_response_from_dict = EmployeeVerificationUpdateResponse.from_dict(employee_verification_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


