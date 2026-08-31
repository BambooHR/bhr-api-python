# CreateCompensationBenchmarkSourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the new benchmark source. Cannot be empty or equal to &#x60;mercer&#x60;. | 
**color_code** | **str** | Optional hex color used to display the source in the UI. | [optional] 

## Example

```python
from bamboohr_sdk.models.create_compensation_benchmark_source_request import CreateCompensationBenchmarkSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompensationBenchmarkSourceRequest from a JSON string
create_compensation_benchmark_source_request_instance = CreateCompensationBenchmarkSourceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCompensationBenchmarkSourceRequest.to_json())

# convert the object into a dict
create_compensation_benchmark_source_request_dict = create_compensation_benchmark_source_request_instance.to_dict()
# create an instance of CreateCompensationBenchmarkSourceRequest from a dict
create_compensation_benchmark_source_request_from_dict = CreateCompensationBenchmarkSourceRequest.from_dict(create_compensation_benchmark_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


