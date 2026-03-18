# ApplicationDetailsAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachment ID | [optional] 
**name** | **str** | Attachment file name | [optional] 
**file_url** | **str** | URL to download the attachment | [optional] 

## Example

```python
from bamboohr_sdk.models.application_details_attachments_inner import ApplicationDetailsAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDetailsAttachmentsInner from a JSON string
application_details_attachments_inner_instance = ApplicationDetailsAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationDetailsAttachmentsInner.to_json())

# convert the object into a dict
application_details_attachments_inner_dict = application_details_attachments_inner_instance.to_dict()
# create an instance of ApplicationDetailsAttachmentsInner from a dict
application_details_attachments_inner_from_dict = ApplicationDetailsAttachmentsInner.from_dict(application_details_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


