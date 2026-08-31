# CustomReportResponse

Data from a saved custom report, plus a `fields` array describing its columns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[CustomReportResponseFieldsInner]**](CustomReportResponseFieldsInner.md) | The report&#39;s columns, in the order the report shows them. | [optional] 
**data** | **List[object]** |  | [optional] 
**aggregations** | [**List[EmployeeResponseAggregationsInner]**](EmployeeResponseAggregationsInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.custom_report_response import CustomReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomReportResponse from a JSON string
custom_report_response_instance = CustomReportResponse.from_json(json)
# print the JSON string representation of the object
print(CustomReportResponse.to_json())

# convert the object into a dict
custom_report_response_dict = custom_report_response_instance.to_dict()
# create an instance of CustomReportResponse from a dict
custom_report_response_from_dict = CustomReportResponse.from_dict(custom_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


