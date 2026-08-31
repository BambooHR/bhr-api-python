# LegacyReportFieldMapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | [**List[LegacyReportFieldMapResponseMappingsInner]**](LegacyReportFieldMapResponseMappingsInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.legacy_report_field_map_response import LegacyReportFieldMapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyReportFieldMapResponse from a JSON string
legacy_report_field_map_response_instance = LegacyReportFieldMapResponse.from_json(json)
# print the JSON string representation of the object
print(LegacyReportFieldMapResponse.to_json())

# convert the object into a dict
legacy_report_field_map_response_dict = legacy_report_field_map_response_instance.to_dict()
# create an instance of LegacyReportFieldMapResponse from a dict
legacy_report_field_map_response_from_dict = LegacyReportFieldMapResponse.from_dict(legacy_report_field_map_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


