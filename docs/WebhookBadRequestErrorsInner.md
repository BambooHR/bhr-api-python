# WebhookBadRequestErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**issues** | **List[str]** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_bad_request_errors_inner import WebhookBadRequestErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookBadRequestErrorsInner from a JSON string
webhook_bad_request_errors_inner_instance = WebhookBadRequestErrorsInner.from_json(json)
# print the JSON string representation of the object
print(WebhookBadRequestErrorsInner.to_json())

# convert the object into a dict
webhook_bad_request_errors_inner_dict = webhook_bad_request_errors_inner_instance.to_dict()
# create an instance of WebhookBadRequestErrorsInner from a dict
webhook_bad_request_errors_inner_from_dict = WebhookBadRequestErrorsInner.from_dict(webhook_bad_request_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


