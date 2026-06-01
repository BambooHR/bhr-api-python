# DataRequestAggregations

Aggregation configuration. Set `defaultAggregation` to apply one aggregation type to every requested field, or use `overridingAggregations` to target specific fields. Both may be combined.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_aggregation** | **str** |  | [optional] 
**overriding_aggregations** | **List[Dict[str, str]]** | Per-field aggregation overrides. Each element is an object whose single key is the field name and whose value is the aggregation type. | [optional] 

## Example

```python
from bamboohr_sdk.models.data_request_aggregations import DataRequestAggregations

# TODO update the JSON string below
json = "{}"
# create an instance of DataRequestAggregations from a JSON string
data_request_aggregations_instance = DataRequestAggregations.from_json(json)
# print the JSON string representation of the object
print(DataRequestAggregations.to_json())

# convert the object into a dict
data_request_aggregations_dict = data_request_aggregations_instance.to_dict()
# create an instance of DataRequestAggregations from a dict
data_request_aggregations_from_dict = DataRequestAggregations.from_dict(data_request_aggregations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


