# WebHookPostFieldResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[WebHookPostFieldDataObject]**](WebHookPostFieldDataObject.md) |  | 
**pages** | [**List[WebHookPostFieldPageDataObject]**](WebHookPostFieldPageDataObject.md) |  | 
**tables** | [**List[WebHookPostFieldTableDataObject]**](WebHookPostFieldTableDataObject.md) |  | 

## Example

```python
from bamboohr_sdk.models.web_hook_post_field_response_object import WebHookPostFieldResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookPostFieldResponseObject from a JSON string
web_hook_post_field_response_object_instance = WebHookPostFieldResponseObject.from_json(json)
# print the JSON string representation of the object
print(WebHookPostFieldResponseObject.to_json())

# convert the object into a dict
web_hook_post_field_response_object_dict = web_hook_post_field_response_object_instance.to_dict()
# create an instance of WebHookPostFieldResponseObject from a dict
web_hook_post_field_response_object_from_dict = WebHookPostFieldResponseObject.from_dict(web_hook_post_field_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


