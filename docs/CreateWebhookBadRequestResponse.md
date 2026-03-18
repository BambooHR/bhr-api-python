# CreateWebhookBadRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**WebhookErrorErrors**](WebhookErrorErrors.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.create_webhook_bad_request_response import CreateWebhookBadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookBadRequestResponse from a JSON string
create_webhook_bad_request_response_instance = CreateWebhookBadRequestResponse.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookBadRequestResponse.to_json())

# convert the object into a dict
create_webhook_bad_request_response_dict = create_webhook_bad_request_response_instance.to_dict()
# create an instance of CreateWebhookBadRequestResponse from a dict
create_webhook_bad_request_response_from_dict = CreateWebhookBadRequestResponse.from_dict(create_webhook_bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


