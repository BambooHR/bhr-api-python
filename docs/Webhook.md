# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the webhook. | [optional] 
**name** | **str** | The name of the webhook. | [optional] 
**created** | **str** | Datetime when the webhook was created (UTC, format: YYYY-MM-DD HH:MM:SS). | [optional] 
**last_sent** | **str** | Datetime when the webhook was last fired (UTC, format: YYYY-MM-DD HH:MM:SS). Null if the webhook has never fired. | [optional] 
**monitor_fields** | **List[str]** |  | [optional] 
**post_fields** | **object** | An object map of field ID or alias to the external name used in the webhook payload. | [optional] 
**url** | **str** | The URL the webhook sends data to. | [optional] 
**format** | **str** | The payload format used by the webhook. | [optional] 
**private_key** | **str** | The private key used to verify webhook authenticity via HMAC-SHA256. Only returned at creation time. | [optional] 
**include_company_domain** | **bool** | Whether the company domain is added to the webhook request header. | [optional] 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) | Events that trigger this webhook. | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


