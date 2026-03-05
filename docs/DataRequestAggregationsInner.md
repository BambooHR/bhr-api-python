# DataRequestAggregationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**aggregation** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.data_request_aggregations_inner import DataRequestAggregationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataRequestAggregationsInner from a JSON string
data_request_aggregations_inner_instance = DataRequestAggregationsInner.from_json(json)
# print the JSON string representation of the object
print(DataRequestAggregationsInner.to_json())

# convert the object into a dict
data_request_aggregations_inner_dict = data_request_aggregations_inner_instance.to_dict()
# create an instance of DataRequestAggregationsInner from a dict
data_request_aggregations_inner_from_dict = DataRequestAggregationsInner.from_dict(data_request_aggregations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


