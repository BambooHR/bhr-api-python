# ImportCompensationBenchmarksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_data** | **List[List[Optional[str]]]** | Parsed CSV rows. Each row is an array of cell values as strings. | [optional] 
**column_map** | [**List[CompensationBenchmarkingColumnMap]**](CompensationBenchmarkingColumnMap.md) | Suggested mapping between expected benchmark fields and CSV column headers. | [optional] 

## Example

```python
from bamboohr_sdk.models.import_compensation_benchmarks_response import ImportCompensationBenchmarksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCompensationBenchmarksResponse from a JSON string
import_compensation_benchmarks_response_instance = ImportCompensationBenchmarksResponse.from_json(json)
# print the JSON string representation of the object
print(ImportCompensationBenchmarksResponse.to_json())

# convert the object into a dict
import_compensation_benchmarks_response_dict = import_compensation_benchmarks_response_instance.to_dict()
# create an instance of ImportCompensationBenchmarksResponse from a dict
import_compensation_benchmarks_response_from_dict = ImportCompensationBenchmarksResponse.from_dict(import_compensation_benchmarks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


