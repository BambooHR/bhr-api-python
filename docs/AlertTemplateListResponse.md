# AlertTemplateListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[AlertTemplateListResponseAlertsInner]**](AlertTemplateListResponseAlertsInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.alert_template_list_response import AlertTemplateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTemplateListResponse from a JSON string
alert_template_list_response_instance = AlertTemplateListResponse.from_json(json)
# print the JSON string representation of the object
print(AlertTemplateListResponse.to_json())

# convert the object into a dict
alert_template_list_response_dict = alert_template_list_response_instance.to_dict()
# create an instance of AlertTemplateListResponse from a dict
alert_template_list_response_from_dict = AlertTemplateListResponse.from_dict(alert_template_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


