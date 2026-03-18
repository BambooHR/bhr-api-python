# WebHookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the webhook. | [optional] 
**name** | **str** | The name of the webhook. | [optional] 
**created** | **str** | Datetime when the webhook was created (UTC, format: YYYY-MM-DD HH:MM:SS). | [optional] 
**last_sent** | **str** | Datetime when the webhook was last fired (UTC, format: YYYY-MM-DD HH:MM:SS). Null if the webhook has never fired. | [optional] 
**monitor_fields** | **List[str]** |  | [optional] 
**post_fields** | **object** | A map of field ID or alias to the external name used in the webhook payload. | [optional] 
**url** | **str** | The URL the webhook sends data to. | [optional] 
**format** | **str** | The payload format used by the webhook. | [optional] 
**include_company_domain** | **bool** | Whether the company domain is added to the webhook request header. | [optional] 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) | Events that trigger this webhook. | [optional] 
**errors** | [**List[WebhookSubErrorProperty]**](WebhookSubErrorProperty.md) | Field-level permission errors associated with the webhook configuration, when present. | [optional] 

## Example

```python
from bamboohr_sdk.models.web_hook_response import WebHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookResponse from a JSON string
web_hook_response_instance = WebHookResponse.from_json(json)
# print the JSON string representation of the object
print(WebHookResponse.to_json())

# convert the object into a dict
web_hook_response_dict = web_hook_response_instance.to_dict()
# create an instance of WebHookResponse from a dict
web_hook_response_from_dict = WebHookResponse.from_dict(web_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


