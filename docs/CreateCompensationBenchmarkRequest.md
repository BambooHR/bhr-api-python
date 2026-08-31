# CreateCompensationBenchmarkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_title_id** | **str** | ID of the company job title the benchmark applies to. | 
**job_location_id** | **str** | Optional job location ID to scope the benchmark to a specific location. | [optional] 
**currency_code** | **str** | ISO 4217 currency code for the benchmark values. | 
**mjl_job_code** | **str** | Mercer Job Library code associated with this benchmark. Stored on the benchmark as &#x60;mercerJobCode&#x60;. | [optional] 
**benchmark_value** | **float** | Benchmark median value. | 
**benchmark_min** | **float** | Benchmark minimum value. | 
**benchmark_max** | **float** | Benchmark maximum value. | 
**benchmark_source** | **str** | Free-text label describing where the benchmark came from. | [optional] 
**external_job_title** | **str** |  | [optional] 
**external_location** | **str** |  | [optional] 
**external_level** | **str** |  | [optional] 
**external_job_description** | **str** |  | [optional] 
**companies_surveyed** | **int** |  | [optional] 
**employees_surveyed** | **int** |  | [optional] 
**source_id** | **str** | ID of the benchmark source from &#x60;GET /api/v1/compensation/benchmarks/sources&#x60;. | [optional] 
**source_date** | **str** | Date the benchmark source data applies to. | [optional] 
**data_year** | **str** | Year of the underlying survey data. | [optional] 
**external_country** | **str** |  | [optional] 
**external_secondary_location** | **str** |  | [optional] 
**external_company_size** | **str** |  | [optional] 
**external_industry** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.create_compensation_benchmark_request import CreateCompensationBenchmarkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompensationBenchmarkRequest from a JSON string
create_compensation_benchmark_request_instance = CreateCompensationBenchmarkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCompensationBenchmarkRequest.to_json())

# convert the object into a dict
create_compensation_benchmark_request_dict = create_compensation_benchmark_request_instance.to_dict()
# create an instance of CreateCompensationBenchmarkRequest from a dict
create_compensation_benchmark_request_from_dict = CreateCompensationBenchmarkRequest.from_dict(create_compensation_benchmark_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


