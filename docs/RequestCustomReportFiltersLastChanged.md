# RequestCustomReportFiltersLastChanged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_null** | **str** | yes|no | [optional] 
**value** | **str** | Date last changed | [optional] 

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


