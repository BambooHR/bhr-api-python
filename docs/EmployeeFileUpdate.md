# EmployeeFileUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new display name for the file. | [optional] 
**category_id** | **int** | The ID of the file category (section) to move the file into. | [optional] 
**share_with_employee** | **str** | Whether the file is shared with the employee. Also accepted as &#39;shareWithEmployees&#39;. | [optional] 
**share_with_employees** | **str** | Alias for shareWithEmployee. Whether the file is shared with the employee. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_file_update import EmployeeFileUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeFileUpdate from a JSON string
employee_file_update_instance = EmployeeFileUpdate.from_json(json)
# print the JSON string representation of the object
print(EmployeeFileUpdate.to_json())

# convert the object into a dict
employee_file_update_dict = employee_file_update_instance.to_dict()
# create an instance of EmployeeFileUpdate from a dict
employee_file_update_from_dict = EmployeeFileUpdate.from_dict(employee_file_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


