# EmployeeVerificationPublicApiRecord

A single employee verification row as returned by the public list API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**employee_id** | **int** |  | [optional] 
**integration_type** | **str** |  | [optional] 
**verification_type** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 
**verification_status_notes** | **str** |  | [optional] 
**remote_access_url** | **str** |  | [optional] 
**e_verify_status** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 
**billing_processed** | **bool** |  | [optional] 
**created_by_user_id** | **int** |  | [optional] 
**created_ymdt** | **str** | Creation timestamp (company DB format). | [optional] 
**last_modified_ymdt** | **str** | Last modified timestamp (company DB format). | [optional] 
**start_date_ymdt** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_verification_public_api_record import EmployeeVerificationPublicApiRecord

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeVerificationPublicApiRecord from a JSON string
employee_verification_public_api_record_instance = EmployeeVerificationPublicApiRecord.from_json(json)
# print the JSON string representation of the object
print(EmployeeVerificationPublicApiRecord.to_json())

# convert the object into a dict
employee_verification_public_api_record_dict = employee_verification_public_api_record_instance.to_dict()
# create an instance of EmployeeVerificationPublicApiRecord from a dict
employee_verification_public_api_record_from_dict = EmployeeVerificationPublicApiRecord.from_dict(employee_verification_public_api_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


