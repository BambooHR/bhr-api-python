# EmployeePhotoJsonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | **str** | The actual MIME type of the underlying image (e.g. &#x60;image/jpeg&#x60;, &#x60;image/png&#x60;, &#x60;image/bmp&#x60;, &#x60;image/gif&#x60;, &#x60;image/tiff&#x60;). Use this to identify the format of the decoded bytes. | 
**file_base64** | **bytearray** | Base64-encoded image bytes. Decoding produces the same bytes returned by the binary variant of this endpoint. | 

## Example

```python
from bamboohr_sdk.models.employee_photo_json_response import EmployeePhotoJsonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeePhotoJsonResponse from a JSON string
employee_photo_json_response_instance = EmployeePhotoJsonResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeePhotoJsonResponse.to_json())

# convert the object into a dict
employee_photo_json_response_dict = employee_photo_json_response_instance.to_dict()
# create an instance of EmployeePhotoJsonResponse from a dict
employee_photo_json_response_from_dict = EmployeePhotoJsonResponse.from_dict(employee_photo_json_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


