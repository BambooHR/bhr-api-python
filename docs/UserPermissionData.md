# UserPermissionData

Schema for the compensation upsell data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_admin** | **bool** | Whether user is an admin | [optional] 
**is_billing_contact** | **bool** | Whether user is a billing contact | [optional] 
**is_owner** | **bool** | Whether user is the owner | [optional] 
**is_support_admin** | **bool** | Whether user is a support admin | [optional] 

## Example

```python
from bamboohr_sdk.models.user_permission_data import UserPermissionData

# TODO update the JSON string below
json = "{}"
# create an instance of UserPermissionData from a JSON string
user_permission_data_instance = UserPermissionData.from_json(json)
# print the JSON string representation of the object
print(UserPermissionData.to_json())

# convert the object into a dict
user_permission_data_dict = user_permission_data_instance.to_dict()
# create an instance of UserPermissionData from a dict
user_permission_data_from_dict = UserPermissionData.from_dict(user_permission_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


