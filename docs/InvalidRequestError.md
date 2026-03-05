# InvalidRequestError

Error details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code indicating the type of validation failure. For BadPage errors, common causes include: 1) Invalid page parameter format, 2) Using the wrong paging parameter for before/after cursors, or 3) An employee on the page boundary changed between calls (for example, the employee was deleted or no longer matches the filter criteria). | 
**message** | **str** | Human-readable message describing the validation failure. | 

## Example

```python
from bamboohr_sdk.models.invalid_request_error import InvalidRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidRequestError from a JSON string
invalid_request_error_instance = InvalidRequestError.from_json(json)
# print the JSON string representation of the object
print(InvalidRequestError.to_json())

# convert the object into a dict
invalid_request_error_dict = invalid_request_error_instance.to_dict()
# create an instance of InvalidRequestError from a dict
invalid_request_error_from_dict = InvalidRequestError.from_dict(invalid_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


