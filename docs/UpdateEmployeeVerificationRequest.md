# UpdateEmployeeVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_type** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 
**verification_status_notes** | **str** |  | [optional] 
**remote_access_url** | **str** |  | [optional] 
**e_verify_status** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_employee_verification_request import UpdateEmployeeVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmployeeVerificationRequest from a JSON string
update_employee_verification_request_instance = UpdateEmployeeVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEmployeeVerificationRequest.to_json())

# convert the object into a dict
update_employee_verification_request_dict = update_employee_verification_request_instance.to_dict()
# create an instance of UpdateEmployeeVerificationRequest from a dict
update_employee_verification_request_from_dict = UpdateEmployeeVerificationRequest.from_dict(update_employee_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


