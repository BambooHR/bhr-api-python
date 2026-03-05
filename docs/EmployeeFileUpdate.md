# EmployeeFileUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**share_with_employee** | **str** |  | [optional] 

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


