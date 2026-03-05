# NewWebHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the webhook. | 
**monitor_fields** | **List[str]** | A list of fields to monitor. | 
**post_fields** | **object** | A list of fields to post to the webhook url. Field ID or alias: external name | [optional] 
**url** | **str** | The url the webhook should send data to (must begin with https://). | 
**format** | **str** | The format the webhook should use (json - default, form-encoded). | [optional] 
**include_company_domain** | **bool** | If set to true, the company domain will be added to the header. | [optional] 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) | Events that trigger this webhook. Defaults to [&#39;employee_with_fields.updated&#39;, &#39;employee_with_fields.deleted&#39;, &#39;employee_with_fields.created&#39;] if not specified. Cannot mix employee_with_fields events with employee events. | [optional] 

## Example

```python
from bamboohr_sdk.models.new_web_hook import NewWebHook

# TODO update the JSON string below
json = "{}"
# create an instance of NewWebHook from a JSON string
new_web_hook_instance = NewWebHook.from_json(json)
# print the JSON string representation of the object
print(NewWebHook.to_json())

# convert the object into a dict
new_web_hook_dict = new_web_hook_instance.to_dict()
# create an instance of NewWebHook from a dict
new_web_hook_from_dict = NewWebHook.from_dict(new_web_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


