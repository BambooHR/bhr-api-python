# ProjectInfoApiTransformerTask

Task information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task ID | [optional] 
**name** | **str** | Task name | [optional] 

## Example

```python
from bamboohr_sdk.models.project_info_api_transformer_task import ProjectInfoApiTransformerTask

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInfoApiTransformerTask from a JSON string
project_info_api_transformer_task_instance = ProjectInfoApiTransformerTask.from_json(json)
# print the JSON string representation of the object
print(ProjectInfoApiTransformerTask.to_json())

# convert the object into a dict
project_info_api_transformer_task_dict = project_info_api_transformer_task_instance.to_dict()
# create an instance of ProjectInfoApiTransformerTask from a dict
project_info_api_transformer_task_from_dict = ProjectInfoApiTransformerTask.from_dict(project_info_api_transformer_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


