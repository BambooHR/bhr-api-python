# WebHookPostFieldDataObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Field identifier used in the API | 
**name** | **str** | Field name | 
**type** | **str** | Field type | 
**id** | **int** | Field ID | 
**page_id** | **int** | ID of the page the field belongs to. This will always be present, as fields without a page id are disabled and not usable in webhooks. | 
**table_id** | **int** | ID of the table the field belongs to | 

## Example

```python
from bamboohr_sdk.models.web_hook_post_field_data_object import WebHookPostFieldDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookPostFieldDataObject from a JSON string
web_hook_post_field_data_object_instance = WebHookPostFieldDataObject.from_json(json)
# print the JSON string representation of the object
print(WebHookPostFieldDataObject.to_json())

# convert the object into a dict
web_hook_post_field_data_object_dict = web_hook_post_field_data_object_instance.to_dict()
# create an instance of WebHookPostFieldDataObject from a dict
web_hook_post_field_data_object_from_dict = WebHookPostFieldDataObject.from_dict(web_hook_post_field_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


