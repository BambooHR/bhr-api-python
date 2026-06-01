# CompensationBenchmarkingColumnMap

Schema for compensation benchmarking column map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_column_key** | **str** |  | [optional] 
**column_name** | **str** | Column name | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmarking_column_map import CompensationBenchmarkingColumnMap

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkingColumnMap from a JSON string
compensation_benchmarking_column_map_instance = CompensationBenchmarkingColumnMap.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkingColumnMap.to_json())

# convert the object into a dict
compensation_benchmarking_column_map_dict = compensation_benchmarking_column_map_instance.to_dict()
# create an instance of CompensationBenchmarkingColumnMap from a dict
compensation_benchmarking_column_map_from_dict = CompensationBenchmarkingColumnMap.from_dict(compensation_benchmarking_column_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


