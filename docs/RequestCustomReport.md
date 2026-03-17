# RequestCustomReport

Report definition for an ad-hoc custom report. Specify the fields to include and optionally filter the employee set. Field IDs are the internal BambooHR field names (e.g. `firstName`, `lastName`, `department`). See the fields metadata endpoint for available field IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A label for the report. Included in the response and used as the file name for downloaded reports. | [optional] 
**fields** | **List[str]** | Array of field IDs to include as columns in the report. Maximum of 400 fields. | [optional] 
**filters** | [**RequestCustomReportFilters**](RequestCustomReportFilters.md) |  | [optional] 
**filter_duplicates** | **str** | Whether to apply standard duplicate row filtering. Defaults to enabled. Set to &#x60;no&#x60; to return raw results without deduplication. | [optional] 

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


