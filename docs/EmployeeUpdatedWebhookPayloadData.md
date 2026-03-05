# EmployeeUpdatedWebhookPayloadData

Event data containing employee and change information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | The company ID | [optional] 
**employee_id** | **str** | The employee ID that was updated | [optional] 
**changed_fields** | **List[str]** | Array of API aliases for fields that changed and are monitored by this webhook | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_updated_webhook_payload_data import EmployeeUpdatedWebhookPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeUpdatedWebhookPayloadData from a JSON string
employee_updated_webhook_payload_data_instance = EmployeeUpdatedWebhookPayloadData.from_json(json)
# print the JSON string representation of the object
print(EmployeeUpdatedWebhookPayloadData.to_json())

# convert the object into a dict
employee_updated_webhook_payload_data_dict = employee_updated_webhook_payload_data_instance.to_dict()
# create an instance of EmployeeUpdatedWebhookPayloadData from a dict
employee_updated_webhook_payload_data_from_dict = EmployeeUpdatedWebhookPayloadData.from_dict(employee_updated_webhook_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


