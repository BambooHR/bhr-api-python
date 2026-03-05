# WebHookPostFieldPageDataObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Page ID | 
**name** | **str** | Page Name | 

## Example

```python
from bamboohr_sdk.models.web_hook_post_field_page_data_object import WebHookPostFieldPageDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookPostFieldPageDataObject from a JSON string
web_hook_post_field_page_data_object_instance = WebHookPostFieldPageDataObject.from_json(json)
# print the JSON string representation of the object
print(WebHookPostFieldPageDataObject.to_json())

# convert the object into a dict
web_hook_post_field_page_data_object_dict = web_hook_post_field_page_data_object_instance.to_dict()
# create an instance of WebHookPostFieldPageDataObject from a dict
web_hook_post_field_page_data_object_from_dict = WebHookPostFieldPageDataObject.from_dict(web_hook_post_field_page_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


