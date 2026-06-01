# EmployeeVerificationIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | [**EmployeeVerificationIntegration**](EmployeeVerificationIntegration.md) |  | 

## Example

```python
from bamboohr_sdk.models.employee_verification_integration_response import EmployeeVerificationIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeVerificationIntegrationResponse from a JSON string
employee_verification_integration_response_instance = EmployeeVerificationIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeVerificationIntegrationResponse.to_json())

# convert the object into a dict
employee_verification_integration_response_dict = employee_verification_integration_response_instance.to_dict()
# create an instance of EmployeeVerificationIntegrationResponse from a dict
employee_verification_integration_response_from_dict = EmployeeVerificationIntegrationResponse.from_dict(employee_verification_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


