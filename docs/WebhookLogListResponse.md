# WebhookLogListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**WebhookLogRateLimitResponseError**](WebhookLogRateLimitResponseError.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_log_list_response import WebhookLogListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLogListResponse from a JSON string
webhook_log_list_response_instance = WebhookLogListResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookLogListResponse.to_json())

# convert the object into a dict
webhook_log_list_response_dict = webhook_log_list_response_instance.to_dict()
# create an instance of WebhookLogListResponse from a dict
webhook_log_list_response_from_dict = WebhookLogListResponse.from_dict(webhook_log_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


