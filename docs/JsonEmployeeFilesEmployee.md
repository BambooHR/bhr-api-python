# JsonEmployeeFilesEmployee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Employee ID. | [optional] 

## Example

```python
from bamboohr_sdk.models.json_employee_files_employee import JsonEmployeeFilesEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEmployeeFilesEmployee from a JSON string
json_employee_files_employee_instance = JsonEmployeeFilesEmployee.from_json(json)
# print the JSON string representation of the object
print(JsonEmployeeFilesEmployee.to_json())

# convert the object into a dict
json_employee_files_employee_dict = json_employee_files_employee_instance.to_dict()
# create an instance of JsonEmployeeFilesEmployee from a dict
json_employee_files_employee_from_dict = JsonEmployeeFilesEmployee.from_dict(json_employee_files_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


