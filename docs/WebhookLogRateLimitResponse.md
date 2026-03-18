# WebhookLogRateLimitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**WebhookLogRateLimitResponseError**](WebhookLogRateLimitResponseError.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_log_rate_limit_response import WebhookLogRateLimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLogRateLimitResponse from a JSON string
webhook_log_rate_limit_response_instance = WebhookLogRateLimitResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookLogRateLimitResponse.to_json())

# convert the object into a dict
webhook_log_rate_limit_response_dict = webhook_log_rate_limit_response_instance.to_dict()
# create an instance of WebhookLogRateLimitResponse from a dict
webhook_log_rate_limit_response_from_dict = WebhookLogRateLimitResponse.from_dict(webhook_log_rate_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


