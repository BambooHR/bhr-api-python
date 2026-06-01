# LevelsAndBandsUploadResponse

Schema for levels and bands import upload response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_data** | **List[str]** | Upload data | [optional] 
**column_map** | [**List[LevelsAndBandsColumnMap]**](LevelsAndBandsColumnMap.md) | Column map | [optional] 

## Example

```python
from bamboohr_sdk.models.levels_and_bands_upload_response import LevelsAndBandsUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LevelsAndBandsUploadResponse from a JSON string
levels_and_bands_upload_response_instance = LevelsAndBandsUploadResponse.from_json(json)
# print the JSON string representation of the object
print(LevelsAndBandsUploadResponse.to_json())

# convert the object into a dict
levels_and_bands_upload_response_dict = levels_and_bands_upload_response_instance.to_dict()
# create an instance of LevelsAndBandsUploadResponse from a dict
levels_and_bands_upload_response_from_dict = LevelsAndBandsUploadResponse.from_dict(levels_and_bands_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


