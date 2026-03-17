# RequestCustomReportFiltersLastChanged

Filters employees to those whose data was last changed on or after the given date/time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** | ISO 8601 date-time value. Only employees whose data has changed at or after this date-time will be included. | [optional] 
**include_null** | **str** | Whether to include employees with no last-changed date. &#x60;yes&#x60; (default) includes them; &#x60;no&#x60; excludes them. | [optional] 
**any_field** | **str** | Whether to match against changes to any field (&#x60;yes&#x60;, default) or only specific fields. Set to &#x60;no&#x60; to restrict matching. Note: &#x60;anyField&#x3D;no&#x60; is deprecated. | [optional] 

## Example

```python
from bamboohr_sdk.models.request_custom_report_filters_last_changed import RequestCustomReportFiltersLastChanged

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCustomReportFiltersLastChanged from a JSON string
request_custom_report_filters_last_changed_instance = RequestCustomReportFiltersLastChanged.from_json(json)
# print the JSON string representation of the object
print(RequestCustomReportFiltersLastChanged.to_json())

# convert the object into a dict
request_custom_report_filters_last_changed_dict = request_custom_report_filters_last_changed_instance.to_dict()
# create an instance of RequestCustomReportFiltersLastChanged from a dict
request_custom_report_filters_last_changed_from_dict = RequestCustomReportFiltersLastChanged.from_dict(request_custom_report_filters_last_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


