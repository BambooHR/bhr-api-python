# UpdateEmployeeVerificationIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Desired enabled state for the integration. | 

## Example

```python
from bamboohr_sdk.models.update_employee_verification_integration_request import UpdateEmployeeVerificationIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmployeeVerificationIntegrationRequest from a JSON string
update_employee_verification_integration_request_instance = UpdateEmployeeVerificationIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEmployeeVerificationIntegrationRequest.to_json())

# convert the object into a dict
update_employee_verification_integration_request_dict = update_employee_verification_integration_request_instance.to_dict()
# create an instance of UpdateEmployeeVerificationIntegrationRequest from a dict
update_employee_verification_integration_request_from_dict = UpdateEmployeeVerificationIntegrationRequest.from_dict(update_employee_verification_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


