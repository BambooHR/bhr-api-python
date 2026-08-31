# LegacyReportFieldMapResponseMappingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_field_id** | **str** | Identifier the legacy report API emitted for this field: an api alias such as &#x60;location&#x60;, or &#x60;&lt;fieldId&gt;&#x60; / &#x60;&lt;fieldId&gt;.&lt;subfieldId&gt;&#x60; when the field had no alias. Numeric ids may be negative — calculated columns such as full name or length of service carry a negative id — so match them as signed integers, not as digits only. | [optional] 
**field_name** | **str** | Field name this legacy identifier now maps to. Matches the key the report and dataset endpoints use in their responses, so it can be used as-is. | [optional] 
**field_label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**qualifier** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.legacy_report_field_map_response_mappings_inner import LegacyReportFieldMapResponseMappingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyReportFieldMapResponseMappingsInner from a JSON string
legacy_report_field_map_response_mappings_inner_instance = LegacyReportFieldMapResponseMappingsInner.from_json(json)
# print the JSON string representation of the object
print(LegacyReportFieldMapResponseMappingsInner.to_json())

# convert the object into a dict
legacy_report_field_map_response_mappings_inner_dict = legacy_report_field_map_response_mappings_inner_instance.to_dict()
# create an instance of LegacyReportFieldMapResponseMappingsInner from a dict
legacy_report_field_map_response_mappings_inner_from_dict = LegacyReportFieldMapResponseMappingsInner.from_dict(legacy_report_field_map_response_mappings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


