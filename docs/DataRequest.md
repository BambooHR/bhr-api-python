# DataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[str]** |  | 
**aggregations** | [**List[DataRequestAggregationsInner]**](DataRequestAggregationsInner.md) |  | [optional] 
**sort_by** | [**List[DataRequestSortByInner]**](DataRequestSortByInner.md) |  | [optional] 
**filters** | [**DataRequestFilters**](DataRequestFilters.md) |  | [optional] 
**group_by** | **List[str]** |  | [optional] 
**show_history** | **List[str]** |  | [optional] 

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


