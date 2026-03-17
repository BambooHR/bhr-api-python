# ChangedEmployeeIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest** | **datetime** | The latest last-changed timestamp among the returned employees. | 
**employees** | [**Dict[str, ChangedEmployeeIdsResponseEmployeesValue]**](ChangedEmployeeIdsResponseEmployeesValue.md) | Map of employee IDs to change metadata for each changed employee. | 

## Example

```python
from bamboohr_sdk.models.changed_employee_ids_response import ChangedEmployeeIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangedEmployeeIdsResponse from a JSON string
changed_employee_ids_response_instance = ChangedEmployeeIdsResponse.from_json(json)
# print the JSON string representation of the object
print(ChangedEmployeeIdsResponse.to_json())

# convert the object into a dict
changed_employee_ids_response_dict = changed_employee_ids_response_instance.to_dict()
# create an instance of ChangedEmployeeIdsResponse from a dict
changed_employee_ids_response_from_dict = ChangedEmployeeIdsResponse.from_dict(changed_employee_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


