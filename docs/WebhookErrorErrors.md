# WebhookErrorErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**unknown_fields** | [**List[WebhookSubErrorPropertyUnknownFieldsInner]**](WebhookSubErrorPropertyUnknownFieldsInner.md) |  | [optional] 
**monitor_fields** | [**List[WebhookSubErrorPropertyMonitorFieldsInner]**](WebhookSubErrorPropertyMonitorFieldsInner.md) |  | [optional] 
**duplicate_post_string** | **List[str]** |  | [optional] 
**post_fields** | [**List[WebhookSubErrorPropertyMonitorFieldsInner]**](WebhookSubErrorPropertyMonitorFieldsInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_error_errors import WebhookErrorErrors

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookErrorErrors from a JSON string
webhook_error_errors_instance = WebhookErrorErrors.from_json(json)
# print the JSON string representation of the object
print(WebhookErrorErrors.to_json())

# convert the object into a dict
webhook_error_errors_dict = webhook_error_errors_instance.to_dict()
# create an instance of WebhookErrorErrors from a dict
webhook_error_errors_from_dict = WebhookErrorErrors.from_dict(webhook_error_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


