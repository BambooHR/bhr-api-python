# UpdateCompensationBenchmarkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the benchmark to update. | 
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
**data_year** | **str** | Year of the underlying survey data. Omitting this field clears &#x60;data_year&#x60; on the stored benchmark, so callers updating a Mercer benchmark should resend the existing value. | [optional] 
**external_country** | **str** |  | [optional] 
**external_secondary_location** | **str** |  | [optional] 
**external_company_size** | **str** |  | [optional] 
**external_industry** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_compensation_benchmark_request import UpdateCompensationBenchmarkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompensationBenchmarkRequest from a JSON string
update_compensation_benchmark_request_instance = UpdateCompensationBenchmarkRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCompensationBenchmarkRequest.to_json())

# convert the object into a dict
update_compensation_benchmark_request_dict = update_compensation_benchmark_request_instance.to_dict()
# create an instance of UpdateCompensationBenchmarkRequest from a dict
update_compensation_benchmark_request_from_dict = UpdateCompensationBenchmarkRequest.from_dict(update_compensation_benchmark_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


