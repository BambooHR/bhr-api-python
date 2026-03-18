# CompanyIntegrationsUpdatedWebhookPayloadData

Event data containing company information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | The company ID | [optional] 

## Example

```python
from bamboohr_sdk.models.company_integrations_updated_webhook_payload_data import CompanyIntegrationsUpdatedWebhookPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyIntegrationsUpdatedWebhookPayloadData from a JSON string
company_integrations_updated_webhook_payload_data_instance = CompanyIntegrationsUpdatedWebhookPayloadData.from_json(json)
# print the JSON string representation of the object
print(CompanyIntegrationsUpdatedWebhookPayloadData.to_json())

# convert the object into a dict
company_integrations_updated_webhook_payload_data_dict = company_integrations_updated_webhook_payload_data_instance.to_dict()
# create an instance of CompanyIntegrationsUpdatedWebhookPayloadData from a dict
company_integrations_updated_webhook_payload_data_from_dict = CompanyIntegrationsUpdatedWebhookPayloadData.from_dict(company_integrations_updated_webhook_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


