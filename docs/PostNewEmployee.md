# PostNewEmployee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.post_new_employee import PostNewEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of PostNewEmployee from a JSON string
post_new_employee_instance = PostNewEmployee.from_json(json)
# print the JSON string representation of the object
print(PostNewEmployee.to_json())

# convert the object into a dict
post_new_employee_dict = post_new_employee_instance.to_dict()
# create an instance of PostNewEmployee from a dict
post_new_employee_from_dict = PostNewEmployee.from_dict(post_new_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


