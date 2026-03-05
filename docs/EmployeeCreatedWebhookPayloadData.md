# EmployeeCreatedWebhookPayloadData

Event data containing employee information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | The company ID | [optional] 
**employee_id** | **str** | The employee ID that was created | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_created_webhook_payload_data import EmployeeCreatedWebhookPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeCreatedWebhookPayloadData from a JSON string
employee_created_webhook_payload_data_instance = EmployeeCreatedWebhookPayloadData.from_json(json)
# print the JSON string representation of the object
print(EmployeeCreatedWebhookPayloadData.to_json())

# convert the object into a dict
employee_created_webhook_payload_data_dict = employee_created_webhook_payload_data_instance.to_dict()
# create an instance of EmployeeCreatedWebhookPayloadData from a dict
employee_created_webhook_payload_data_from_dict = EmployeeCreatedWebhookPayloadData.from_dict(employee_created_webhook_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


