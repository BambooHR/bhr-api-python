# ProjectLegacyErrorResponseV1

Legacy error response returned by the time tracking project endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ProjectLegacyErrorResponseV1Error**](ProjectLegacyErrorResponseV1Error.md) |  | 

## Example

```python
from bamboohr_sdk.models.project_legacy_error_response_v1 import ProjectLegacyErrorResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectLegacyErrorResponseV1 from a JSON string
project_legacy_error_response_v1_instance = ProjectLegacyErrorResponseV1.from_json(json)
# print the JSON string representation of the object
print(ProjectLegacyErrorResponseV1.to_json())

# convert the object into a dict
project_legacy_error_response_v1_dict = project_legacy_error_response_v1_instance.to_dict()
# create an instance of ProjectLegacyErrorResponseV1 from a dict
project_legacy_error_response_v1_from_dict = ProjectLegacyErrorResponseV1.from_dict(project_legacy_error_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


