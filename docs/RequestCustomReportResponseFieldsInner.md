# RequestCustomReportResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The field ID. | [optional] 
**type** | **str** | The field data type. | [optional] 
**name** | **str** | The human-readable field label. | [optional] 

## Example

```python
from bamboohr_sdk.models.request_custom_report_response_fields_inner import RequestCustomReportResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCustomReportResponseFieldsInner from a JSON string
request_custom_report_response_fields_inner_instance = RequestCustomReportResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(RequestCustomReportResponseFieldsInner.to_json())

# convert the object into a dict
request_custom_report_response_fields_inner_dict = request_custom_report_response_fields_inner_instance.to_dict()
# create an instance of RequestCustomReportResponseFieldsInner from a dict
request_custom_report_response_fields_inner_from_dict = RequestCustomReportResponseFieldsInner.from_dict(request_custom_report_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


