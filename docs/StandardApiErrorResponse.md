# StandardApiErrorResponse

Standard error response format returned by API endpoints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Error type identifier | 
**title** | **str** | Human-readable error message | 
**details** | **str** | Additional error details | [optional] 

## Example

```python
from bamboohr_sdk.models.standard_api_error_response import StandardApiErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StandardApiErrorResponse from a JSON string
standard_api_error_response_instance = StandardApiErrorResponse.from_json(json)
# print the JSON string representation of the object
print(StandardApiErrorResponse.to_json())

# convert the object into a dict
standard_api_error_response_dict = standard_api_error_response_instance.to_dict()
# create an instance of StandardApiErrorResponse from a dict
standard_api_error_response_from_dict = StandardApiErrorResponse.from_dict(standard_api_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


