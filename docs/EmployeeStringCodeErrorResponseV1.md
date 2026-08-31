# EmployeeStringCodeErrorResponseV1

Error response returned by Employee API endpoints where `error.code` is a string identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**EmployeeStringCodeErrorResponseV1Error**](EmployeeStringCodeErrorResponseV1Error.md) |  | 

## Example

```python
from bamboohr_sdk.models.employee_string_code_error_response_v1 import EmployeeStringCodeErrorResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeStringCodeErrorResponseV1 from a JSON string
employee_string_code_error_response_v1_instance = EmployeeStringCodeErrorResponseV1.from_json(json)
# print the JSON string representation of the object
print(EmployeeStringCodeErrorResponseV1.to_json())

# convert the object into a dict
employee_string_code_error_response_v1_dict = employee_string_code_error_response_v1_instance.to_dict()
# create an instance of EmployeeStringCodeErrorResponseV1 from a dict
employee_string_code_error_response_v1_from_dict = EmployeeStringCodeErrorResponseV1.from_dict(employee_string_code_error_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


