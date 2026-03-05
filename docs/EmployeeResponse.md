# EmployeeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | [optional] 
**aggregations** | [**List[EmployeeResponseAggregationsInner]**](EmployeeResponseAggregationsInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_response import EmployeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeResponse from a JSON string
employee_response_instance = EmployeeResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeResponse.to_json())

# convert the object into a dict
employee_response_dict = employee_response_instance.to_dict()
# create an instance of EmployeeResponse from a dict
employee_response_from_dict = EmployeeResponse.from_dict(employee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


