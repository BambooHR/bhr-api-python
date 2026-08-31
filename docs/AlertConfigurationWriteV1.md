# AlertConfigurationWriteV1

Request body for creating or updating an alert configuration. Only `bambooAlertId` is required; every other property falls back to a server-side default when omitted. The configuration's own `id`, its `editorUserId`, and its `lastEdited` timestamp are assigned by the server and must not be sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bamboo_alert_id** | **int** | Identifier of the alert template this configuration is based on, taken from the &#x60;id&#x60; field of **List Alert Templates** (&#x60;list-alert-templates&#x60;). The template catalog is global rather than per-company, and an identifier that is not in the catalog is rejected. &#x60;0&#x60; is rejected as a missing value; there is no sentinel for \&quot;any alert\&quot;. | 
**schedule** | **str** | How often the alert runs. | [optional] [default to 'daily']
**due_within** | **int** |  | [optional] 
**due_interval** | **str** |  | [optional] 
**send_to_employee** | **bool** | Whether the alert should be sent to employees. | [optional] [default to True]
**send_to_manager** | **bool** | Whether the alert should be sent to managers. | [optional] [default to False]
**send_to_admin** | **bool** | Whether the alert should be sent to admins. | [optional] [default to False]
**custom_message** | **str** |  | [optional] 
**custom_subject** | **str** |  | [optional] 
**group_by** | **str** |  | [optional] 
**limit_training_to_required** | **bool** | Whether the training covered by a training alert should be limited to required training. | [optional] [default to True]
**run_at_time** | **str** |  | [optional] 
**run_at_time_zone** | **str** |  | [optional] 
**include_position** | **bool** | Whether the alert should include position. | [optional] [default to False]
**include_location** | **bool** | Whether the alert should include location. | [optional] [default to False]
**filter_list_value_ids** | **List[int]** | List value IDs the alert is scoped to. Accepted values are the &#x60;options[].id&#x60; values of the employee filter list fields: Department, Division, Location, Job Title, Employment Status, and Status, plus Employment Type and Team on accounts where those fields are enabled. Look the IDs up with **Account Information &gt; List List Fields** (&#x60;list-list-fields&#x60;); an ID belonging to any other list field is rejected. An empty array leaves the alert unscoped, and omitting it on a replace clears all list-value scoping. This is the only recipient-scoping property the API stores. | [optional] 

## Example

```python
from bamboohr_sdk.models.alert_configuration_write_v1 import AlertConfigurationWriteV1

# TODO update the JSON string below
json = "{}"
# create an instance of AlertConfigurationWriteV1 from a JSON string
alert_configuration_write_v1_instance = AlertConfigurationWriteV1.from_json(json)
# print the JSON string representation of the object
print(AlertConfigurationWriteV1.to_json())

# convert the object into a dict
alert_configuration_write_v1_dict = alert_configuration_write_v1_instance.to_dict()
# create an instance of AlertConfigurationWriteV1 from a dict
alert_configuration_write_v1_from_dict = AlertConfigurationWriteV1.from_dict(alert_configuration_write_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


