# CompensationBenchmarkJobLocationEmployeeSalary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_job_location_employee_salary import CompensationBenchmarkJobLocationEmployeeSalary

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkJobLocationEmployeeSalary from a JSON string
compensation_benchmark_job_location_employee_salary_instance = CompensationBenchmarkJobLocationEmployeeSalary.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkJobLocationEmployeeSalary.to_json())

# convert the object into a dict
compensation_benchmark_job_location_employee_salary_dict = compensation_benchmark_job_location_employee_salary_instance.to_dict()
# create an instance of CompensationBenchmarkJobLocationEmployeeSalary from a dict
compensation_benchmark_job_location_employee_salary_from_dict = CompensationBenchmarkJobLocationEmployeeSalary.from_dict(compensation_benchmark_job_location_employee_salary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


