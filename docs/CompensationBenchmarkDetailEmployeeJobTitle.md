# CompensationBenchmarkDetailEmployeeJobTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_detail_employee_job_title import CompensationBenchmarkDetailEmployeeJobTitle

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkDetailEmployeeJobTitle from a JSON string
compensation_benchmark_detail_employee_job_title_instance = CompensationBenchmarkDetailEmployeeJobTitle.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkDetailEmployeeJobTitle.to_json())

# convert the object into a dict
compensation_benchmark_detail_employee_job_title_dict = compensation_benchmark_detail_employee_job_title_instance.to_dict()
# create an instance of CompensationBenchmarkDetailEmployeeJobTitle from a dict
compensation_benchmark_detail_employee_job_title_from_dict = CompensationBenchmarkDetailEmployeeJobTitle.from_dict(compensation_benchmark_detail_employee_job_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


