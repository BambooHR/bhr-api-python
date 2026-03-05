# EmployeeDeletedWebhookPayload

Webhook payload sent when an employee is deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The event type identifier | [optional] 
**timestamp** | **datetime** | ISO 8601 timestamp (UTC) when the event was fired | [optional] 
**data** | [**EmployeeDeletedWebhookPayloadData**](EmployeeDeletedWebhookPayloadData.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_deleted_webhook_payload import EmployeeDeletedWebhookPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeDeletedWebhookPayload from a JSON string
employee_deleted_webhook_payload_instance = EmployeeDeletedWebhookPayload.from_json(json)
# print the JSON string representation of the object
print(EmployeeDeletedWebhookPayload.to_json())

# convert the object into a dict
employee_deleted_webhook_payload_dict = employee_deleted_webhook_payload_instance.to_dict()
# create an instance of EmployeeDeletedWebhookPayload from a dict
employee_deleted_webhook_payload_from_dict = EmployeeDeletedWebhookPayload.from_dict(employee_deleted_webhook_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


