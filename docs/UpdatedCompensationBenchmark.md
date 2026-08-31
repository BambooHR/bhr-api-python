# UpdatedCompensationBenchmark


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saved_benchmark** | [**UpdatedCompensationBenchmarkSavedBenchmark**](UpdatedCompensationBenchmarkSavedBenchmark.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.updated_compensation_benchmark import UpdatedCompensationBenchmark

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedCompensationBenchmark from a JSON string
updated_compensation_benchmark_instance = UpdatedCompensationBenchmark.from_json(json)
# print the JSON string representation of the object
print(UpdatedCompensationBenchmark.to_json())

# convert the object into a dict
updated_compensation_benchmark_dict = updated_compensation_benchmark_instance.to_dict()
# create an instance of UpdatedCompensationBenchmark from a dict
updated_compensation_benchmark_from_dict = UpdatedCompensationBenchmark.from_dict(updated_compensation_benchmark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


