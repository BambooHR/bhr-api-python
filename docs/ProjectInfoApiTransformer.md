# ProjectInfoApiTransformer

Project information data representation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**ProjectInfoApiTransformerProject**](ProjectInfoApiTransformerProject.md) |  | [optional] 
**task** | [**ProjectInfoApiTransformerTask**](ProjectInfoApiTransformerTask.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.project_info_api_transformer import ProjectInfoApiTransformer

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInfoApiTransformer from a JSON string
project_info_api_transformer_instance = ProjectInfoApiTransformer.from_json(json)
# print the JSON string representation of the object
print(ProjectInfoApiTransformer.to_json())

# convert the object into a dict
project_info_api_transformer_dict = project_info_api_transformer_instance.to_dict()
# create an instance of ProjectInfoApiTransformer from a dict
project_info_api_transformer_from_dict = ProjectInfoApiTransformer.from_dict(project_info_api_transformer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


