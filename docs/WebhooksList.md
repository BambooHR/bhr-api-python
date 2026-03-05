# WebhooksList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhooks** | [**List[WebhooksListWebhooksInner]**](WebhooksListWebhooksInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhooks_list import WebhooksList

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksList from a JSON string
webhooks_list_instance = WebhooksList.from_json(json)
# print the JSON string representation of the object
print(WebhooksList.to_json())

# convert the object into a dict
webhooks_list_dict = webhooks_list_instance.to_dict()
# create an instance of WebhooksList from a dict
webhooks_list_from_dict = WebhooksList.from_dict(webhooks_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


