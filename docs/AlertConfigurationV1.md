# AlertConfigurationV1

A single alert the company has configured: the alert template it is based on, when it runs, who receives it, and any customizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of this alert configuration. | [optional] 
**bamboo_alert_id** | **int** | The identifier of the alert template this configuration is based on. Resolve template identifiers to a name and group with **List Alert Templates** (&#x60;list-alert-templates&#x60;), which exposes the same identifier as &#x60;id&#x60;. | [optional] 
**schedule** | **str** | The schedule for the company alert. | [optional] 
**due_within** | **int** |  | [optional] 
**due_interval** | **str** |  | [optional] 
**send_to_employee** | **bool** | Whether the alert should be sent to employees. | [optional] 
**send_to_manager** | **bool** | Whether the alert should be sent to managers. | [optional] 
**send_to_admin** | **bool** | Whether the alert should be sent to admins. | [optional] 
**editor_user_id** | **int** |  | [optional] 
**last_edited** | **datetime** |  | [optional] 
**custom_message** | **str** |  | [optional] 
**custom_subject** | **str** |  | [optional] 
**group_by** | **str** |  | [optional] 
**limit_training_to_required** | **bool** | Whether the training should be limited to required training. | [optional] 
**run_at_time** | **str** |  | [optional] 
**run_at_time_zone** | **str** |  | [optional] 
**include_position** | **bool** | Whether the alert should include position. | [optional] 
**include_location** | **bool** | Whether the alert should include location. | [optional] 
**additional_recipient_emails** | **List[str]** | Never persisted by this API. A &#x60;GET&#x60;, both the list and the single-read, always returns an empty array, while a create or replace response echoes back whatever was submitted; that echo does not mean the value was stored. | [optional] 
**employee_ids** | **List[str]** | Internal employee IDs. Never persisted by this API: a read always returns an empty array, while a create or replace response echoes back whatever was submitted; that echo does not mean the value was stored. | [optional] 
**list_value_ids** | **List[int]** | Never persisted by this API. A &#x60;GET&#x60;, both the list and the single-read, always returns an empty array, while a create or replace response echoes back whatever was submitted; that echo does not mean the value was stored. Use &#x60;filterListValueIds&#x60; to scope an alert by list value. | [optional] 
**filter_list_value_ids** | **List[int]** | List value IDs the alert is scoped to, such as specific departments or locations. An empty array means the alert is not scoped by list value. | [optional] 
**user_ids** | **List[int]** | Never persisted by this API. A &#x60;GET&#x60;, both the list and the single-read, always returns an empty array, while a create or replace response echoes back whatever was submitted; that echo does not mean the value was stored. | [optional] 

## Example

```python
from bamboohr_sdk.models.alert_configuration_v1 import AlertConfigurationV1

# TODO update the JSON string below
json = "{}"
# create an instance of AlertConfigurationV1 from a JSON string
alert_configuration_v1_instance = AlertConfigurationV1.from_json(json)
# print the JSON string representation of the object
print(AlertConfigurationV1.to_json())

# convert the object into a dict
alert_configuration_v1_dict = alert_configuration_v1_instance.to_dict()
# create an instance of AlertConfigurationV1 from a dict
alert_configuration_v1_from_dict = AlertConfigurationV1.from_dict(alert_configuration_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


