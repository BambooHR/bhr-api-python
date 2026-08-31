# AlertTemplateListResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[AlertTemplateListResponseV1AlertsInner]**](AlertTemplateListResponseV1AlertsInner.md) | Alert templates, ordered by &#x60;groupName&#x60; and then &#x60;name&#x60;. Empty only if the catalog itself is empty. | [optional] 

## Example

```python
from bamboohr_sdk.models.alert_template_list_response_v1 import AlertTemplateListResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTemplateListResponseV1 from a JSON string
alert_template_list_response_v1_instance = AlertTemplateListResponseV1.from_json(json)
# print the JSON string representation of the object
print(AlertTemplateListResponseV1.to_json())

# convert the object into a dict
alert_template_list_response_v1_dict = alert_template_list_response_v1_instance.to_dict()
# create an instance of AlertTemplateListResponseV1 from a dict
alert_template_list_response_v1_from_dict = AlertTemplateListResponseV1.from_dict(alert_template_list_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


