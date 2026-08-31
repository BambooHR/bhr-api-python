# CompensationBenchmarkJobLocationPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_details** | [**CompensationBenchmarkJobLocationPairJobDetails**](CompensationBenchmarkJobLocationPairJobDetails.md) |  | [optional] 
**location_details** | **object** |  | [optional] 
**is_remote** | **bool** |  | [optional] 
**benchmarks** | [**List[CompensationBenchmarkOverview]**](CompensationBenchmarkOverview.md) | Saved benchmarks attached to this job/location. Empty when none are configured. | [optional] 
**employees** | [**List[CompensationBenchmarkJobLocationEmployee]**](CompensationBenchmarkJobLocationEmployee.md) |  | [optional] 
**internal_job_pay_band** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_benchmark_job_location_pair import CompensationBenchmarkJobLocationPair

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationBenchmarkJobLocationPair from a JSON string
compensation_benchmark_job_location_pair_instance = CompensationBenchmarkJobLocationPair.from_json(json)
# print the JSON string representation of the object
print(CompensationBenchmarkJobLocationPair.to_json())

# convert the object into a dict
compensation_benchmark_job_location_pair_dict = compensation_benchmark_job_location_pair_instance.to_dict()
# create an instance of CompensationBenchmarkJobLocationPair from a dict
compensation_benchmark_job_location_pair_from_dict = CompensationBenchmarkJobLocationPair.from_dict(compensation_benchmark_job_location_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


