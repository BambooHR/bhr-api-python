# EmployeeResponseAggregationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**aggregation_type** | **str** |  | [optional] 
**groups** | **object** |  | [optional] 
**all** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_response_aggregations_inner import EmployeeResponseAggregationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeResponseAggregationsInner from a JSON string
employee_response_aggregations_inner_instance = EmployeeResponseAggregationsInner.from_json(json)
# print the JSON string representation of the object
print(EmployeeResponseAggregationsInner.to_json())

# convert the object into a dict
employee_response_aggregations_inner_dict = employee_response_aggregations_inner_instance.to_dict()
# create an instance of EmployeeResponseAggregationsInner from a dict
employee_response_aggregations_inner_from_dict = EmployeeResponseAggregationsInner.from_dict(employee_response_aggregations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


