# WebhooksListWebhooksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the webhook. | [optional] 
**name** | **str** | The name of the webhook. | [optional] 
**created** | **str** | The creation date of the webhook. | [optional] 
**last_sent** | **str** | The date the webhook was last sent. | [optional] 
**url** | **str** | The url of the webhook. | [optional] 

## Example

```python
from bamboohr_sdk.models.webhooks_list_webhooks_inner import WebhooksListWebhooksInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksListWebhooksInner from a JSON string
webhooks_list_webhooks_inner_instance = WebhooksListWebhooksInner.from_json(json)
# print the JSON string representation of the object
print(WebhooksListWebhooksInner.to_json())

# convert the object into a dict
webhooks_list_webhooks_inner_dict = webhooks_list_webhooks_inner_instance.to_dict()
# create an instance of WebhooksListWebhooksInner from a dict
webhooks_list_webhooks_inner_from_dict = WebhooksListWebhooksInner.from_dict(webhooks_list_webhooks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


