# UpdateWebhookBadRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**WebhookErrorErrors**](WebhookErrorErrors.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_webhook_bad_request_response import UpdateWebhookBadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookBadRequestResponse from a JSON string
update_webhook_bad_request_response_instance = UpdateWebhookBadRequestResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookBadRequestResponse.to_json())

# convert the object into a dict
update_webhook_bad_request_response_dict = update_webhook_bad_request_response_instance.to_dict()
# create an instance of UpdateWebhookBadRequestResponse from a dict
update_webhook_bad_request_response_from_dict = UpdateWebhookBadRequestResponse.from_dict(update_webhook_bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


