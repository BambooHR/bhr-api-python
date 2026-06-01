# DataRequestFilters

Filter configuration. Combine multiple conditions with a `match` strategy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | **str** | Logical operator for combining filters: &#x60;all&#x60; (AND) or &#x60;any&#x60; (OR). | [optional] 
**filters** | [**List[DataRequestFiltersFiltersInner]**](DataRequestFiltersFiltersInner.md) | Array of filter conditions. Filter fields do not need to appear in the top-level &#x60;fields&#x60; array. | [optional] 

## Example

```python
from bamboohr_sdk.models.data_request_filters import DataRequestFilters

# TODO update the JSON string below
json = "{}"
# create an instance of DataRequestFilters from a JSON string
data_request_filters_instance = DataRequestFilters.from_json(json)
# print the JSON string representation of the object
print(DataRequestFilters.to_json())

# convert the object into a dict
data_request_filters_dict = data_request_filters_instance.to_dict()
# create an instance of DataRequestFilters from a dict
data_request_filters_from_dict = DataRequestFilters.from_dict(data_request_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


