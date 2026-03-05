# WebHookResponse


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
**include_company_domain** | **bool** | If set to true, the company domain will be added to the header. | [optional] 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) | Events that trigger this webhook. | [optional] 

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


