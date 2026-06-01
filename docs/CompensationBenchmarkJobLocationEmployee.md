# CompensationBenchmarkJobLocationEmployee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**salary** | [**CompensationBenchmarkJobLocationEmployeeSalary**](CompensationBenchmarkJobLocationEmployeeSalary.md) |  | [optional] 
**photo_url** | **str** |  | [optional] 
**manager_name** | **str** |  | [optional] 
**manager_title** | **str** |  | [optional] 
**division** | **object** |  | [optional] 
**department** | **object** |  | [optional] 
**currency_conversion_failed** | **bool** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_job_location_employee import CompensationBenchmarkJobLocationEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkJobLocationEmployee from a JSON string
compensation_benchmark_job_location_employee_instance = CompensationBenchmarkJobLocationEmployee.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkJobLocationEmployee.to_json())

# convert the object into a dict
compensation_benchmark_job_location_employee_dict = compensation_benchmark_job_location_employee_instance.to_dict()
# create an instance of CompensationBenchmarkJobLocationEmployee from a dict
compensation_benchmark_job_location_employee_from_dict = CompensationBenchmarkJobLocationEmployee.from_dict(compensation_benchmark_job_location_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


