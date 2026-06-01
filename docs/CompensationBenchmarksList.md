# CompensationBenchmarksList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_location_pairs** | [**List[CompensationBenchmarkJobLocationPair]**](CompensationBenchmarkJobLocationPair.md) |  | [optional] 
**dismiss_review_banner** | **bool** |  | [optional] 
**dismiss_add_location_banner** | **bool** |  | [optional] 
**dismiss_mercer_data_info_banner** | **bool** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmarks_list import CompensationBenchmarksList

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarksList from a JSON string
compensation_benchmarks_list_instance = CompensationBenchmarksList.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarksList.to_json())

# convert the object into a dict
compensation_benchmarks_list_dict = compensation_benchmarks_list_instance.to_dict()
# create an instance of CompensationBenchmarksList from a dict
compensation_benchmarks_list_from_dict = CompensationBenchmarksList.from_dict(compensation_benchmarks_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


