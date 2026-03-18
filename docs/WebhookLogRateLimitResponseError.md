# WebhookLogRateLimitResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_log_rate_limit_response_error import WebhookLogRateLimitResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLogRateLimitResponseError from a JSON string
webhook_log_rate_limit_response_error_instance = WebhookLogRateLimitResponseError.from_json(json)
# print the JSON string representation of the object
print(WebhookLogRateLimitResponseError.to_json())

# convert the object into a dict
webhook_log_rate_limit_response_error_dict = webhook_log_rate_limit_response_error_instance.to_dict()
# create an instance of WebhookLogRateLimitResponseError from a dict
webhook_log_rate_limit_response_error_from_dict = WebhookLogRateLimitResponseError.from_dict(webhook_log_rate_limit_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


