# RequestCustomReportResponseEmployeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The employee ID. | [optional] 

## Example

```python
from bamboohr_sdk.models.request_custom_report_response_employees_inner import RequestCustomReportResponseEmployeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCustomReportResponseEmployeesInner from a JSON string
request_custom_report_response_employees_inner_instance = RequestCustomReportResponseEmployeesInner.from_json(json)
# print the JSON string representation of the object
print(RequestCustomReportResponseEmployeesInner.to_json())

# convert the object into a dict
request_custom_report_response_employees_inner_dict = request_custom_report_response_employees_inner_instance.to_dict()
# create an instance of RequestCustomReportResponseEmployeesInner from a dict
request_custom_report_response_employees_inner_from_dict = RequestCustomReportResponseEmployeesInner.from_dict(request_custom_report_response_employees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


