# LegacyReportIDMapResponseMappingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_report_id** | **int** |  | [optional] 
**new_report_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.legacy_report_id_map_response_mappings_inner import LegacyReportIDMapResponseMappingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyReportIDMapResponseMappingsInner from a JSON string
legacy_report_id_map_response_mappings_inner_instance = LegacyReportIDMapResponseMappingsInner.from_json(json)
# print the JSON string representation of the object
print(LegacyReportIDMapResponseMappingsInner.to_json())

# convert the object into a dict
legacy_report_id_map_response_mappings_inner_dict = legacy_report_id_map_response_mappings_inner_instance.to_dict()
# create an instance of LegacyReportIDMapResponseMappingsInner from a dict
legacy_report_id_map_response_mappings_inner_from_dict = LegacyReportIDMapResponseMappingsInner.from_dict(legacy_report_id_map_response_mappings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


