# EmployeeCreatedWebhookPayload

Webhook payload sent when a new employee is created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The event type identifier | [optional] 
**timestamp** | **datetime** | ISO 8601 timestamp (UTC) when the event was fired | [optional] 
**data** | [**EmployeeCreatedWebhookPayloadData**](EmployeeCreatedWebhookPayloadData.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_created_webhook_payload import EmployeeCreatedWebhookPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeCreatedWebhookPayload from a JSON string
employee_created_webhook_payload_instance = EmployeeCreatedWebhookPayload.from_json(json)
# print the JSON string representation of the object
print(EmployeeCreatedWebhookPayload.to_json())

# convert the object into a dict
employee_created_webhook_payload_dict = employee_created_webhook_payload_instance.to_dict()
# create an instance of EmployeeCreatedWebhookPayload from a dict
employee_created_webhook_payload_from_dict = EmployeeCreatedWebhookPayload.from_dict(employee_created_webhook_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


