# EmployeeDeletedWebhookPayloadData

Event data containing employee information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | The company ID | [optional] 
**employee_id** | **str** | The employee ID that was deleted | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_deleted_webhook_payload_data import EmployeeDeletedWebhookPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeDeletedWebhookPayloadData from a JSON string
employee_deleted_webhook_payload_data_instance = EmployeeDeletedWebhookPayloadData.from_json(json)
# print the JSON string representation of the object
print(EmployeeDeletedWebhookPayloadData.to_json())

# convert the object into a dict
employee_deleted_webhook_payload_data_dict = employee_deleted_webhook_payload_data_instance.to_dict()
# create an instance of EmployeeDeletedWebhookPayloadData from a dict
employee_deleted_webhook_payload_data_from_dict = EmployeeDeletedWebhookPayloadData.from_dict(employee_deleted_webhook_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


