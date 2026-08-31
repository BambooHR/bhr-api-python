# CompensationUpsellData

Schema for the compensation upsell data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_owner_name** | **str** | Account owner name | [optional] 
**can_request_demo** | **bool** | Whether user can request a demo | [optional] 
**user_permissions** | [**UserPermissionData**](UserPermissionData.md) | User permissions | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_upsell_data import CompensationUpsellData

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationUpsellData from a JSON string
compensation_upsell_data_instance = CompensationUpsellData.from_json(json)
# print the JSON string representation of the object
print(CompensationUpsellData.to_json())

# convert the object into a dict
compensation_upsell_data_dict = compensation_upsell_data_instance.to_dict()
# create an instance of CompensationUpsellData from a dict
compensation_upsell_data_from_dict = CompensationUpsellData.from_dict(compensation_upsell_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


