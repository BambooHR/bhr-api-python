# EmployeeVerificationLifecycleEmailAcceptedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_verification_lifecycle_email_accepted_response import EmployeeVerificationLifecycleEmailAcceptedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeVerificationLifecycleEmailAcceptedResponse from a JSON string
employee_verification_lifecycle_email_accepted_response_instance = EmployeeVerificationLifecycleEmailAcceptedResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeVerificationLifecycleEmailAcceptedResponse.to_json())

# convert the object into a dict
employee_verification_lifecycle_email_accepted_response_dict = employee_verification_lifecycle_email_accepted_response_instance.to_dict()
# create an instance of EmployeeVerificationLifecycleEmailAcceptedResponse from a dict
employee_verification_lifecycle_email_accepted_response_from_dict = EmployeeVerificationLifecycleEmailAcceptedResponse.from_dict(employee_verification_lifecycle_email_accepted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


