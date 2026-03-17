# RequestCustomReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The report title. | [optional] 
**fields** | [**List[RequestCustomReportResponseFieldsInner]**](RequestCustomReportResponseFieldsInner.md) | Metadata for each field included in the report. | [optional] 
**employees** | [**List[RequestCustomReportResponseEmployeesInner]**](RequestCustomReportResponseEmployeesInner.md) | One object per employee. Each object contains an &#x60;id&#x60; property plus one key per requested field. | [optional] 

## Example

```python
from bamboohr_sdk.models.request_custom_report_response import RequestCustomReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCustomReportResponse from a JSON string
request_custom_report_response_instance = RequestCustomReportResponse.from_json(json)
# print the JSON string representation of the object
print(RequestCustomReportResponse.to_json())

# convert the object into a dict
request_custom_report_response_dict = request_custom_report_response_instance.to_dict()
# create an instance of RequestCustomReportResponse from a dict
request_custom_report_response_from_dict = RequestCustomReportResponse.from_dict(request_custom_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


