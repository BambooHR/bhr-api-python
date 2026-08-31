# ForbiddenV1Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.forbidden_v1_error import ForbiddenV1Error

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenV1Error from a JSON string
forbidden_v1_error_instance = ForbiddenV1Error.from_json(json)
# print the JSON string representation of the object
print(ForbiddenV1Error.to_json())

# convert the object into a dict
forbidden_v1_error_dict = forbidden_v1_error_instance.to_dict()
# create an instance of ForbiddenV1Error from a dict
forbidden_v1_error_from_dict = ForbiddenV1Error.from_dict(forbidden_v1_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


