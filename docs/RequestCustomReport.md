# RequestCustomReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**filters** | [**RequestCustomReportFilters**](RequestCustomReportFilters.md) |  | [optional] 
**fields** | **List[str]** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.request_custom_report import RequestCustomReport

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCustomReport from a JSON string
request_custom_report_instance = RequestCustomReport.from_json(json)
# print the JSON string representation of the object
print(RequestCustomReport.to_json())

# convert the object into a dict
request_custom_report_dict = request_custom_report_instance.to_dict()
# create an instance of RequestCustomReport from a dict
request_custom_report_from_dict = RequestCustomReport.from_dict(request_custom_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


