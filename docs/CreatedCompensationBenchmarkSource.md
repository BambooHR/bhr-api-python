# CreatedCompensationBenchmarkSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the newly created benchmark source. | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.created_compensation_benchmark_source import CreatedCompensationBenchmarkSource

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedCompensationBenchmarkSource from a JSON string
created_compensation_benchmark_source_instance = CreatedCompensationBenchmarkSource.from_json(json)
# print the JSON string representation of the object
print(CreatedCompensationBenchmarkSource.to_json())

# convert the object into a dict
created_compensation_benchmark_source_dict = created_compensation_benchmark_source_instance.to_dict()
# create an instance of CreatedCompensationBenchmarkSource from a dict
created_compensation_benchmark_source_from_dict = CreatedCompensationBenchmarkSource.from_dict(created_compensation_benchmark_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


