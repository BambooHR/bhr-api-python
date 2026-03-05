# EmployeeUpdatedWebhookPayload

Webhook payload sent when an employee is updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The event type identifier | [optional] 
**timestamp** | **datetime** | ISO 8601 timestamp (UTC) when the event was fired | [optional] 
**data** | [**EmployeeUpdatedWebhookPayloadData**](EmployeeUpdatedWebhookPayloadData.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_updated_webhook_payload import EmployeeUpdatedWebhookPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeUpdatedWebhookPayload from a JSON string
employee_updated_webhook_payload_instance = EmployeeUpdatedWebhookPayload.from_json(json)
# print the JSON string representation of the object
print(EmployeeUpdatedWebhookPayload.to_json())

# convert the object into a dict
employee_updated_webhook_payload_dict = employee_updated_webhook_payload_instance.to_dict()
# create an instance of EmployeeUpdatedWebhookPayload from a dict
employee_updated_webhook_payload_from_dict = EmployeeUpdatedWebhookPayload.from_dict(employee_updated_webhook_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


