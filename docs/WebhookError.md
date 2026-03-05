# WebhookError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**WebhookErrorErrors**](WebhookErrorErrors.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_error import WebhookError

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookError from a JSON string
webhook_error_instance = WebhookError.from_json(json)
# print the JSON string representation of the object
print(WebhookError.to_json())

# convert the object into a dict
webhook_error_dict = webhook_error_instance.to_dict()
# create an instance of WebhookError from a dict
webhook_error_from_dict = WebhookError.from_dict(webhook_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


