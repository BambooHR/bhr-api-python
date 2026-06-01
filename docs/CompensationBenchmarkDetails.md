# CompensationBenchmarkDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**mercer_benchmark_details** | **object** |  | [optional] 
**company_pay_range** | **object** |  | [optional] 
**internal_job_pay_band** | **object** |  | [optional] 
**benchmark_values** | [**List[CompensationBenchmarkDetailsBenchmarkValuesInner]**](CompensationBenchmarkDetailsBenchmarkValuesInner.md) | All saved benchmarks for this job/location. Empty when no benchmarks exist. | [optional] 
**employees** | [**List[CompensationBenchmarkDetailEmployee]**](CompensationBenchmarkDetailEmployee.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_details import CompensationBenchmarkDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkDetails from a JSON string
compensation_benchmark_details_instance = CompensationBenchmarkDetails.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkDetails.to_json())

# convert the object into a dict
compensation_benchmark_details_dict = compensation_benchmark_details_instance.to_dict()
# create an instance of CompensationBenchmarkDetails from a dict
compensation_benchmark_details_from_dict = CompensationBenchmarkDetails.from_dict(compensation_benchmark_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


