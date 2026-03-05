# ProjectInfoApiTransformerProject

Project information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project ID | [optional] 
**name** | **str** | Project name | [optional] 

## Example

```python
from bamboohr_sdk.models.project_info_api_transformer_project import ProjectInfoApiTransformerProject

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInfoApiTransformerProject from a JSON string
project_info_api_transformer_project_instance = ProjectInfoApiTransformerProject.from_json(json)
# print the JSON string representation of the object
print(ProjectInfoApiTransformerProject.to_json())

# convert the object into a dict
project_info_api_transformer_project_dict = project_info_api_transformer_project_instance.to_dict()
# create an instance of ProjectInfoApiTransformerProject from a dict
project_info_api_transformer_project_from_dict = ProjectInfoApiTransformerProject.from_dict(project_info_api_transformer_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


