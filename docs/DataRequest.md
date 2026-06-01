# DataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[str]** | Field names to include in each returned record. Use \&quot;Get Fields from Dataset\&quot; to discover available names. | 
**aggregations** | [**DataRequestAggregations**](DataRequestAggregations.md) |  | [optional] 
**sort_by** | [**List[DataRequestSortByInner]**](DataRequestSortByInner.md) | Ordered list of sort rules. Priority follows array order. Include aggregationType when sorting by an aggregated value in a grouped request; it must match an aggregation requested for the same field. | [optional] 
**filters** | [**DataRequestFilters**](DataRequestFilters.md) |  | [optional] 
**group_by** | **List[str]** | Field names to group results by. Currently supports only one field. When grouping is active, the &#x60;data&#x60; key in the response becomes an object keyed by group value instead of an array. | [optional] 
**show_history** | **List[str]** | Entity names of historical table fields whose history rows should be included. Entity names are returned by \&quot;Get Fields from Dataset\&quot;. | [optional] 

## Example

```python
from bamboohr_sdk.models.data_request import DataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataRequest from a JSON string
data_request_instance = DataRequest.from_json(json)
# print the JSON string representation of the object
print(DataRequest.to_json())

# convert the object into a dict
data_request_dict = data_request_instance.to_dict()
# create an instance of DataRequest from a dict
data_request_from_dict = DataRequest.from_dict(data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


