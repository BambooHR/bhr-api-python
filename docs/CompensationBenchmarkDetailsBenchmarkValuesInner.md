# CompensationBenchmarkDetailsBenchmarkValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**job_title** | **str** |  | [optional] 
**last_edited** | **str** |  | [optional] 
**source_color_code** | **str** |  | [optional] 
**source_date** | **str** |  | [optional] 
**created_ymdt** | **str** |  | [optional] 
**updated_ymdt** | **str** |  | [optional] 
**data_year** | **str** |  | [optional] 
**median** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_details_benchmark_values_inner import CompensationBenchmarkDetailsBenchmarkValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkDetailsBenchmarkValuesInner from a JSON string
compensation_benchmark_details_benchmark_values_inner_instance = CompensationBenchmarkDetailsBenchmarkValuesInner.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkDetailsBenchmarkValuesInner.to_json())

# convert the object into a dict
compensation_benchmark_details_benchmark_values_inner_dict = compensation_benchmark_details_benchmark_values_inner_instance.to_dict()
# create an instance of CompensationBenchmarkDetailsBenchmarkValuesInner from a dict
compensation_benchmark_details_benchmark_values_inner_from_dict = CompensationBenchmarkDetailsBenchmarkValuesInner.from_dict(compensation_benchmark_details_benchmark_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


