# UploadEmployeePhotoRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **bytearray** | Base64-encoded image bytes. Same format/size/dimension rules as the multipart &#x60;file&#x60; field: JPEG, PNG, BMP, or GIF (HEIC, SVG, AVIF, and WebP are rejected with 415; TIFF is accepted by the format gate but some variants may fail downstream); square within 1 pixel; at least 150×150 pixels; decoded payload no larger than 20MB. Whitespace inside the base64 string is tolerated and stripped before decoding. | 

## Example

```python
from bamboohr_sdk.models.upload_employee_photo_request1 import UploadEmployeePhotoRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of UploadEmployeePhotoRequest1 from a JSON string
upload_employee_photo_request1_instance = UploadEmployeePhotoRequest1.from_json(json)
# print the JSON string representation of the object
print(UploadEmployeePhotoRequest1.to_json())

# convert the object into a dict
upload_employee_photo_request1_dict = upload_employee_photo_request1_instance.to_dict()
# create an instance of UploadEmployeePhotoRequest1 from a dict
upload_employee_photo_request1_from_dict = UploadEmployeePhotoRequest1.from_dict(upload_employee_photo_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


