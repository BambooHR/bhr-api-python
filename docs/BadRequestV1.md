# BadRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**BadRequestV1Error**](BadRequestV1Error.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.bad_request_v1 import BadRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestV1 from a JSON string
bad_request_v1_instance = BadRequestV1.from_json(json)
# print the JSON string representation of the object
print(BadRequestV1.to_json())

# convert the object into a dict
bad_request_v1_dict = bad_request_v1_instance.to_dict()
# create an instance of BadRequestV1 from a dict
bad_request_v1_from_dict = BadRequestV1.from_dict(bad_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


