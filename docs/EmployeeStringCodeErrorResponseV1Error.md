# EmployeeStringCodeErrorResponseV1Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | String error code identifier (for example &#x60;BadRequest&#x60; or &#x60;BadPage&#x60;). | 
**message** | **str** | Human-readable error message. | 

## Example

```python
from bamboohr_sdk.models.employee_string_code_error_response_v1_error import EmployeeStringCodeErrorResponseV1Error

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeStringCodeErrorResponseV1Error from a JSON string
employee_string_code_error_response_v1_error_instance = EmployeeStringCodeErrorResponseV1Error.from_json(json)
# print the JSON string representation of the object
print(EmployeeStringCodeErrorResponseV1Error.to_json())

# convert the object into a dict
employee_string_code_error_response_v1_error_dict = employee_string_code_error_response_v1_error_instance.to_dict()
# create an instance of EmployeeStringCodeErrorResponseV1Error from a dict
employee_string_code_error_response_v1_error_from_dict = EmployeeStringCodeErrorResponseV1Error.from_dict(employee_string_code_error_response_v1_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


