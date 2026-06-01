# EmployeeVerificationIntegration

Install state and partner metadata for the company's employee verification integration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | True when the integration is installed for the company and partner endpoints are usable. | 
**integration_type** | **str** | Identifier of the configured employee verification partner (opaque string; matches &#x60;integrationType&#x60; from the integration GET response). | 

## Example

```python
from bamboohr_sdk.models.employee_verification_integration import EmployeeVerificationIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeVerificationIntegration from a JSON string
employee_verification_integration_instance = EmployeeVerificationIntegration.from_json(json)
# print the JSON string representation of the object
print(EmployeeVerificationIntegration.to_json())

# convert the object into a dict
employee_verification_integration_dict = employee_verification_integration_instance.to_dict()
# create an instance of EmployeeVerificationIntegration from a dict
employee_verification_integration_from_dict = EmployeeVerificationIntegration.from_dict(employee_verification_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


