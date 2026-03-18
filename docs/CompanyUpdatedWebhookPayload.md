# CompanyUpdatedWebhookPayload

Webhook payload sent when a company is updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The event type identifier | [optional] 
**timestamp** | **datetime** | ISO 8601 timestamp (UTC) when the event was fired | [optional] 
**data** | [**CompanyIntegrationsUpdatedWebhookPayloadData**](CompanyIntegrationsUpdatedWebhookPayloadData.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.company_updated_webhook_payload import CompanyUpdatedWebhookPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUpdatedWebhookPayload from a JSON string
company_updated_webhook_payload_instance = CompanyUpdatedWebhookPayload.from_json(json)
# print the JSON string representation of the object
print(CompanyUpdatedWebhookPayload.to_json())

# convert the object into a dict
company_updated_webhook_payload_dict = company_updated_webhook_payload_instance.to_dict()
# create an instance of CompanyUpdatedWebhookPayload from a dict
company_updated_webhook_payload_from_dict = CompanyUpdatedWebhookPayload.from_dict(company_updated_webhook_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


