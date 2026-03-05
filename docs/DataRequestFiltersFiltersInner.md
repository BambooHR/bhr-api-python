# DataRequestFiltersFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.data_request_filters_filters_inner import DataRequestFiltersFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataRequestFiltersFiltersInner from a JSON string
data_request_filters_filters_inner_instance = DataRequestFiltersFiltersInner.from_json(json)
# print the JSON string representation of the object
print(DataRequestFiltersFiltersInner.to_json())

# convert the object into a dict
data_request_filters_filters_inner_dict = data_request_filters_filters_inner_instance.to_dict()
# create an instance of DataRequestFiltersFiltersInner from a dict
data_request_filters_filters_inner_from_dict = DataRequestFiltersFiltersInner.from_dict(data_request_filters_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


