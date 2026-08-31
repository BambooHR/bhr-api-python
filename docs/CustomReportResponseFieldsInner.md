# CustomReportResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Key this column uses in every &#x60;data&#x60; record. | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.custom_report_response_fields_inner import CustomReportResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomReportResponseFieldsInner from a JSON string
custom_report_response_fields_inner_instance = CustomReportResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(CustomReportResponseFieldsInner.to_json())

# convert the object into a dict
custom_report_response_fields_inner_dict = custom_report_response_fields_inner_instance.to_dict()
# create an instance of CustomReportResponseFieldsInner from a dict
custom_report_response_fields_inner_from_dict = CustomReportResponseFieldsInner.from_dict(custom_report_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


