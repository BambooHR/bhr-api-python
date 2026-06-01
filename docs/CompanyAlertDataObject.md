# CompanyAlertDataObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the company alert. | [optional] 
**bamboo_alert_id** | **int** | The unique identifier of the Bamboo alert. | [optional] 
**schedule** | **str** | The schedule for the company alert. | [optional] 
**due_within** | **int** |  | [optional] 
**due_interval** | **str** |  | [optional] 
**send_to_employee** | **bool** | Whether the alert should be sent to employees. | [optional] 
**send_to_manager** | **bool** | Whether the alert should be sent to managers. | [optional] 
**send_to_admin** | **bool** | Whether the alert should be sent to admins. | [optional] 
**editor_user_id** | **int** |  | [optional] 
**last_edited** | **object** | The last edited date of the company alert. | [optional] 
**custom_message** | **str** |  | [optional] 
**custom_subject** | **str** |  | [optional] 
**group_by** | **str** |  | [optional] 
**limit_training_to_required** | **bool** | Whether the training should be limited to required training. | [optional] 
**run_at_time** | **str** |  | [optional] 
**run_at_time_zone** | **str** |  | [optional] 
**include_position** | **bool** | Whether the alert should include position. | [optional] 
**include_location** | **bool** | Whether the alert should include location. | [optional] 
**additional_recipient_emails** | **List[str]** | The additional recipient emails for the company alert. | [optional] 
**employee_ids** | **List[str]** | The employee IDs for the company alert. | [optional] 
**list_value_ids** | **List[int]** | The list value IDs for the company alert. | [optional] 
**filter_list_value_ids** | **List[int]** | The filter list value IDs for the company alert. | [optional] 
**user_ids** | **List[int]** | The user IDs for the company alert. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_alert_data_object import CompanyAlertDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyAlertDataObject from a JSON string
company_alert_data_object_instance = CompanyAlertDataObject.from_json(json)
# print the JSON string representation of the object
print(CompanyAlertDataObject.to_json())

# convert the object into a dict
company_alert_data_object_dict = company_alert_data_object_instance.to_dict()
# create an instance of CompanyAlertDataObject from a dict
company_alert_data_object_from_dict = CompanyAlertDataObject.from_dict(company_alert_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


