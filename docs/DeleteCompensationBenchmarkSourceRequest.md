# DeleteCompensationBenchmarkSourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the benchmark source to delete. Must be non-empty. | 

## Example

```python
from bamboohr_sdk.models.delete_compensation_benchmark_source_request import DeleteCompensationBenchmarkSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCompensationBenchmarkSourceRequest from a JSON string
delete_compensation_benchmark_source_request_instance = DeleteCompensationBenchmarkSourceRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteCompensationBenchmarkSourceRequest.to_json())

# convert the object into a dict
delete_compensation_benchmark_source_request_dict = delete_compensation_benchmark_source_request_instance.to_dict()
# create an instance of DeleteCompensationBenchmarkSourceRequest from a dict
delete_compensation_benchmark_source_request_from_dict = DeleteCompensationBenchmarkSourceRequest.from_dict(delete_compensation_benchmark_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


