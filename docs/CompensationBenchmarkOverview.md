# CompensationBenchmarkOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**values** | [**CompensationBenchmarkOverviewValues**](CompensationBenchmarkOverviewValues.md) |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_color** | **str** |  | [optional] 
**is_mercer** | **bool** |  | [optional] 
**data_year** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_overview import CompensationBenchmarkOverview

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkOverview from a JSON string
compensation_benchmark_overview_instance = CompensationBenchmarkOverview.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkOverview.to_json())

# convert the object into a dict
compensation_benchmark_overview_dict = compensation_benchmark_overview_instance.to_dict()
# create an instance of CompensationBenchmarkOverview from a dict
compensation_benchmark_overview_from_dict = CompensationBenchmarkOverview.from_dict(compensation_benchmark_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


