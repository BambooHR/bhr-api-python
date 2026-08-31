# ProjectStandardApiErrorResponseV1

Error response returned by standard time tracking project API failures.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**details** | **str** |  | 

## Example

```python
from bamboohr_sdk.models.project_standard_api_error_response_v1 import ProjectStandardApiErrorResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStandardApiErrorResponseV1 from a JSON string
project_standard_api_error_response_v1_instance = ProjectStandardApiErrorResponseV1.from_json(json)
# print the JSON string representation of the object
print(ProjectStandardApiErrorResponseV1.to_json())

# convert the object into a dict
project_standard_api_error_response_v1_dict = project_standard_api_error_response_v1_instance.to_dict()
# create an instance of ProjectStandardApiErrorResponseV1 from a dict
project_standard_api_error_response_v1_from_dict = ProjectStandardApiErrorResponseV1.from_dict(project_standard_api_error_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


