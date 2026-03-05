# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the webhook. | [optional] 
**name** | **str** | The name of the webhook. | [optional] 
**created** | **str** | timestamp of creation | [optional] 
**last_sent** | **str** | timestamp of last webhook sent | [optional] 
**monitor_fields** | **List[str]** | A list of fields to monitor. | [optional] 
**post_fields** | **object** | A list of fields to post to the webhook url. Field ID or alias: external name | [optional] 
**url** | **str** | The url the webhook should send data to. | [optional] 
**format** | **str** | The format the webhook should use (json, form-encoded). | [optional] 
**private_key** | **str** | The private key which can be used to verify that the webhook is secure (uses HMAC-SHA256) | [optional] 
**include_company_domain** | **bool** | If set to true, the company domain will be added to the header. | [optional] 

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


