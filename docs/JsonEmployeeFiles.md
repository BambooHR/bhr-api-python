# JsonEmployeeFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee** | [**JsonEmployeeFilesEmployee**](JsonEmployeeFilesEmployee.md) |  | [optional] 
**categories** | [**List[JsonEmployeeFilesCategoriesInner]**](JsonEmployeeFilesCategoriesInner.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.json_employee_files import JsonEmployeeFiles

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEmployeeFiles from a JSON string
json_employee_files_instance = JsonEmployeeFiles.from_json(json)
# print the JSON string representation of the object
print(JsonEmployeeFiles.to_json())

# convert the object into a dict
json_employee_files_dict = json_employee_files_instance.to_dict()
# create an instance of JsonEmployeeFiles from a dict
json_employee_files_from_dict = JsonEmployeeFiles.from_dict(json_employee_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


