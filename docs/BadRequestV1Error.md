# BadRequestV1Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.bad_request_v1_error import BadRequestV1Error

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestV1Error from a JSON string
bad_request_v1_error_instance = BadRequestV1Error.from_json(json)
# print the JSON string representation of the object
print(BadRequestV1Error.to_json())

# convert the object into a dict
bad_request_v1_error_dict = bad_request_v1_error_instance.to_dict()
# create an instance of BadRequestV1Error from a dict
bad_request_v1_error_from_dict = BadRequestV1Error.from_dict(bad_request_v1_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


