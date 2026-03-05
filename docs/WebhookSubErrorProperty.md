# WebhookSubErrorProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**unknown_fields** | [**List[WebhookSubErrorPropertyUnknownFieldsInner]**](WebhookSubErrorPropertyUnknownFieldsInner.md) |  | [optional] 
**monitor_fields** | [**List[TimeTrackingRecordSchemaProjectTask]**](TimeTrackingRecordSchemaProjectTask.md) |  | [optional] 
**duplicate_post_string** | **List[str]** |  | [optional] 
**post_fields** | [**List[WebhookSubErrorPropertyPostFieldsInner]**](WebhookSubErrorPropertyPostFieldsInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.webhook_sub_error_property import WebhookSubErrorProperty

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubErrorProperty from a JSON string
webhook_sub_error_property_instance = WebhookSubErrorProperty.from_json(json)
# print the JSON string representation of the object
print(WebhookSubErrorProperty.to_json())

# convert the object into a dict
webhook_sub_error_property_dict = webhook_sub_error_property_instance.to_dict()
# create an instance of WebhookSubErrorProperty from a dict
webhook_sub_error_property_from_dict = WebhookSubErrorProperty.from_dict(webhook_sub_error_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


