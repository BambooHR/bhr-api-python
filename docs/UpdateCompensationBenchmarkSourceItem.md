# UpdateCompensationBenchmarkSourceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the existing benchmark source to update. | 
**name** | **str** | New display name for the source. Cannot equal &#x60;mercer&#x60;. | 
**sort** | **str** | Optional new sort position, as a numeric string. | [optional] 

## Example

```python
from bamboohr_sdk.models.update_compensation_benchmark_source_item import UpdateCompensationBenchmarkSourceItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompensationBenchmarkSourceItem from a JSON string
update_compensation_benchmark_source_item_instance = UpdateCompensationBenchmarkSourceItem.from_json(json)
# print the JSON string representation of the object
print(UpdateCompensationBenchmarkSourceItem.to_json())

# convert the object into a dict
update_compensation_benchmark_source_item_dict = update_compensation_benchmark_source_item_instance.to_dict()
# create an instance of UpdateCompensationBenchmarkSourceItem from a dict
update_compensation_benchmark_source_item_from_dict = UpdateCompensationBenchmarkSourceItem.from_dict(update_compensation_benchmark_source_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


