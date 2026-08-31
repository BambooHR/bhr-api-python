# CompensationBenchmarkOverviewValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**median** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**original_median** | **float** |  | [optional] 
**original_min** | **float** |  | [optional] 
**original_max** | **float** |  | [optional] 
**original_currency_code** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_overview_values import CompensationBenchmarkOverviewValues

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkOverviewValues from a JSON string
compensation_benchmark_overview_values_instance = CompensationBenchmarkOverviewValues.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkOverviewValues.to_json())

# convert the object into a dict
compensation_benchmark_overview_values_dict = compensation_benchmark_overview_values_instance.to_dict()
# create an instance of CompensationBenchmarkOverviewValues from a dict
compensation_benchmark_overview_values_from_dict = CompensationBenchmarkOverviewValues.from_dict(compensation_benchmark_overview_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


