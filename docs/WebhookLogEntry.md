# WebhookLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | The ID of the webhook. | [optional] 
**url** | **str** | The URL the webhook was delivered to. | [optional] 
**last_attempted** | **str** | Datetime of the last delivery attempt (UTC, format: YYYY-MM-DD HH:MM:SS), or a status string such as \&quot;Webhook Not Found\&quot; when the delivery target could not be reached. | [optional] 
**last_success** | **str** | Datetime of the last successful delivery (UTC, format: YYYY-MM-DD HH:MM:SS), or a status string such as \&quot;Webhook Not Found\&quot; when no successful delivery has been recorded. | [optional] 
**status_code** | **str** | HTTP status code returned by the webhook endpoint on the last delivery attempt. | [optional] 
**format** | **str** | The payload format used for this delivery. | [optional] 
**employee_ids** | **List[str]** | Array of employee IDs included in the webhook payload, returned as strings. | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_log_entry import WebhookLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLogEntry from a JSON string
webhook_log_entry_instance = WebhookLogEntry.from_json(json)
# print the JSON string representation of the object
print(WebhookLogEntry.to_json())

# convert the object into a dict
webhook_log_entry_dict = webhook_log_entry_instance.to_dict()
# create an instance of WebhookLogEntry from a dict
webhook_log_entry_from_dict = WebhookLogEntry.from_dict(webhook_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


