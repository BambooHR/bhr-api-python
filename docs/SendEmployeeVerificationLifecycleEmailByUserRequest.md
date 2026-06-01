# SendEmployeeVerificationLifecycleEmailByUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_type** | **str** | Which employee verification lifecycle email to send; must be {@see EverifyEmailType::SIGNUP_SURVEY} or {@see EverifyEmailType::APP_INSTALLED} (string values &#x60;signup_survey&#x60;, &#x60;app_installed&#x60;). | 

## Example

```python
from bamboohr_sdk.models.send_employee_verification_lifecycle_email_by_user_request import SendEmployeeVerificationLifecycleEmailByUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmployeeVerificationLifecycleEmailByUserRequest from a JSON string
send_employee_verification_lifecycle_email_by_user_request_instance = SendEmployeeVerificationLifecycleEmailByUserRequest.from_json(json)
# print the JSON string representation of the object
print(SendEmployeeVerificationLifecycleEmailByUserRequest.to_json())

# convert the object into a dict
send_employee_verification_lifecycle_email_by_user_request_dict = send_employee_verification_lifecycle_email_by_user_request_instance.to_dict()
# create an instance of SendEmployeeVerificationLifecycleEmailByUserRequest from a dict
send_employee_verification_lifecycle_email_by_user_request_from_dict = SendEmployeeVerificationLifecycleEmailByUserRequest.from_dict(send_employee_verification_lifecycle_email_by_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


