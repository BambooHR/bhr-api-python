# CreatedCompensationBenchmarkSavedBenchmark


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**job_title_id** | **str** |  | [optional] 
**job_location_id** | **str** |  | [optional] 
**mercer_job_code** | **str** |  | [optional] 
**benchmark_source** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**benchmark_value** | **float** |  | [optional] 
**benchmark_min** | **float** |  | [optional] 
**benchmark_max** | **float** |  | [optional] 
**external_job_title** | **str** |  | [optional] 
**external_location** | **str** |  | [optional] 
**external_level** | **str** |  | [optional] 
**external_job_description** | **str** |  | [optional] 
**companies_surveyed** | **int** |  | [optional] 
**employees_surveyed** | **int** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_date** | **str** |  | [optional] 
**data_year** | **str** |  | [optional] 
**external_country** | **str** |  | [optional] 
**external_secondary_location** | **str** |  | [optional] 
**external_company_size** | **str** |  | [optional] 
**external_industry** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.created_compensation_benchmark_saved_benchmark import CreatedCompensationBenchmarkSavedBenchmark

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedCompensationBenchmarkSavedBenchmark from a JSON string
created_compensation_benchmark_saved_benchmark_instance = CreatedCompensationBenchmarkSavedBenchmark.from_json(json)
# print the JSON string representation of the object
print(CreatedCompensationBenchmarkSavedBenchmark.to_json())

# convert the object into a dict
created_compensation_benchmark_saved_benchmark_dict = created_compensation_benchmark_saved_benchmark_instance.to_dict()
# create an instance of CreatedCompensationBenchmarkSavedBenchmark from a dict
created_compensation_benchmark_saved_benchmark_from_dict = CreatedCompensationBenchmarkSavedBenchmark.from_dict(created_compensation_benchmark_saved_benchmark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


