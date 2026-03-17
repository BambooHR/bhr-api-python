# WebhookBadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[WebhookBadRequestErrorsInner]**](WebhookBadRequestErrorsInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_bad_request import WebhookBadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookBadRequest from a JSON string
webhook_bad_request_instance = WebhookBadRequest.from_json(json)
# print the JSON string representation of the object
print(WebhookBadRequest.to_json())

# convert the object into a dict
webhook_bad_request_dict = webhook_bad_request_instance.to_dict()
# create an instance of WebhookBadRequest from a dict
webhook_bad_request_from_dict = WebhookBadRequest.from_dict(webhook_bad_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


