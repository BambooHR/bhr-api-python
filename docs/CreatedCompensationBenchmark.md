# CreatedCompensationBenchmark


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saved_benchmark** | [**CreatedCompensationBenchmarkSavedBenchmark**](CreatedCompensationBenchmarkSavedBenchmark.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.created_compensation_benchmark import CreatedCompensationBenchmark

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedCompensationBenchmark from a JSON string
created_compensation_benchmark_instance = CreatedCompensationBenchmark.from_json(json)
# print the JSON string representation of the object
print(CreatedCompensationBenchmark.to_json())

# convert the object into a dict
created_compensation_benchmark_dict = created_compensation_benchmark_instance.to_dict()
# create an instance of CreatedCompensationBenchmark from a dict
created_compensation_benchmark_from_dict = CreatedCompensationBenchmark.from_dict(created_compensation_benchmark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


