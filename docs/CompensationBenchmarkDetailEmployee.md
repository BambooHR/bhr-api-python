# CompensationBenchmarkDetailEmployee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**job_title** | [**CompensationBenchmarkDetailEmployeeJobTitle**](CompensationBenchmarkDetailEmployeeJobTitle.md) |  | [optional] 
**location** | **object** |  | [optional] 
**salary** | [**CompensationBenchmarkDetailEmployeeSalary**](CompensationBenchmarkDetailEmployeeSalary.md) |  | [optional] 
**variance_from_pay_band** | **object** |  | [optional] 
**years_at_company** | **int** |  | [optional] 
**range_penetration** | **float** |  | [optional] 
**compa_ratio** | **float** |  | [optional] 
**compa_ratio_status** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**is_remote** | **bool** |  | [optional] 
**currency_conversion_failed** | **bool** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_detail_employee import CompensationBenchmarkDetailEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkDetailEmployee from a JSON string
compensation_benchmark_detail_employee_instance = CompensationBenchmarkDetailEmployee.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkDetailEmployee.to_json())

# convert the object into a dict
compensation_benchmark_detail_employee_dict = compensation_benchmark_detail_employee_instance.to_dict()
# create an instance of CompensationBenchmarkDetailEmployee from a dict
compensation_benchmark_detail_employee_from_dict = CompensationBenchmarkDetailEmployee.from_dict(compensation_benchmark_detail_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


