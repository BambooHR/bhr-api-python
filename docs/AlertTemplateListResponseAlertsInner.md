# AlertTemplateListResponseAlertsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Alert template ID (bambooAlertId) | [optional] 
**name** | **str** | Display name of the alert | [optional] 
**group_name** | **str** | Category group the alert belongs to | [optional] 

## Example

```python
from bamboohr_sdk.models.alert_template_list_response_alerts_inner import AlertTemplateListResponseAlertsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTemplateListResponseAlertsInner from a JSON string
alert_template_list_response_alerts_inner_instance = AlertTemplateListResponseAlertsInner.from_json(json)
# print the JSON string representation of the object
print(AlertTemplateListResponseAlertsInner.to_json())

# convert the object into a dict
alert_template_list_response_alerts_inner_dict = alert_template_list_response_alerts_inner_instance.to_dict()
# create an instance of AlertTemplateListResponseAlertsInner from a dict
alert_template_list_response_alerts_inner_from_dict = AlertTemplateListResponseAlertsInner.from_dict(alert_template_list_response_alerts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


