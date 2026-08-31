# CompensationBenchmarkSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sort** | **str** | Sort order position, returned as a numeric string. | [optional] 
**count** | **str** | Number of benchmarks attached to this source, returned as a numeric string. | [optional] 
**color_code** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_source import CompensationBenchmarkSource

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkSource from a JSON string
compensation_benchmark_source_instance = CompensationBenchmarkSource.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkSource.to_json())

# convert the object into a dict
compensation_benchmark_source_dict = compensation_benchmark_source_instance.to_dict()
# create an instance of CompensationBenchmarkSource from a dict
compensation_benchmark_source_from_dict = CompensationBenchmarkSource.from_dict(compensation_benchmark_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


