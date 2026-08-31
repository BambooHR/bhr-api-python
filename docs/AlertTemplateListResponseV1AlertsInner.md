# AlertTemplateListResponseV1AlertsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Alert template identifier. Supply this value as &#x60;bambooAlertId&#x60; when creating or replacing an alert configuration. | [optional] 
**name** | **str** | Display name of the alert template, as shown in the company&#39;s Email Alerts settings. | [optional] 
**group_name** | **str** | Settings group the alert template is filed under, for example &#x60;Celebrations&#x60;, &#x60;Time off&#x60;, or &#x60;Training&#x60;. | [optional] 

## Example

```python
from bamboohr_sdk.models.alert_template_list_response_v1_alerts_inner import AlertTemplateListResponseV1AlertsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTemplateListResponseV1AlertsInner from a JSON string
alert_template_list_response_v1_alerts_inner_instance = AlertTemplateListResponseV1AlertsInner.from_json(json)
# print the JSON string representation of the object
print(AlertTemplateListResponseV1AlertsInner.to_json())

# convert the object into a dict
alert_template_list_response_v1_alerts_inner_dict = alert_template_list_response_v1_alerts_inner_instance.to_dict()
# create an instance of AlertTemplateListResponseV1AlertsInner from a dict
alert_template_list_response_v1_alerts_inner_from_dict = AlertTemplateListResponseV1AlertsInner.from_dict(alert_template_list_response_v1_alerts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


