# UpdateCompensationBenchmarkSourcesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark_sources** | [**List[UpdateCompensationBenchmarkSourceItem]**](UpdateCompensationBenchmarkSourceItem.md) |  | 

## Example

```python
from bamboohr_sdk.models.update_compensation_benchmark_sources_request import UpdateCompensationBenchmarkSourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompensationBenchmarkSourcesRequest from a JSON string
update_compensation_benchmark_sources_request_instance = UpdateCompensationBenchmarkSourcesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCompensationBenchmarkSourcesRequest.to_json())

# convert the object into a dict
update_compensation_benchmark_sources_request_dict = update_compensation_benchmark_sources_request_instance.to_dict()
# create an instance of UpdateCompensationBenchmarkSourcesRequest from a dict
update_compensation_benchmark_sources_request_from_dict = UpdateCompensationBenchmarkSourcesRequest.from_dict(update_compensation_benchmark_sources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


