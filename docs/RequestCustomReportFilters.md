# RequestCustomReportFilters

Optional filters to restrict which employees appear in the report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_changed** | [**RequestCustomReportFiltersLastChanged**](RequestCustomReportFiltersLastChanged.md) |  | [optional] 
**employee_ids** | **List[int]** | Restricts the report to only the specified employee IDs. | [optional] 

## Example

```python
from bamboohr_sdk.models.request_custom_report_filters import RequestCustomReportFilters

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCustomReportFilters from a JSON string
request_custom_report_filters_instance = RequestCustomReportFilters.from_json(json)
# print the JSON string representation of the object
print(RequestCustomReportFilters.to_json())

# convert the object into a dict
request_custom_report_filters_dict = request_custom_report_filters_instance.to_dict()
# create an instance of RequestCustomReportFilters from a dict
request_custom_report_filters_from_dict = RequestCustomReportFilters.from_dict(request_custom_report_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


