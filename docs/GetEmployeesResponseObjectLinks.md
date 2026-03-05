# GetEmployeesResponseObjectLinks

Navigation links for API pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**GetEmployeesResponseObjectLinksSelf**](GetEmployeesResponseObjectLinksSelf.md) |  | [optional] 
**next** | [**GetEmployeesResponseObjectLinksNext**](GetEmployeesResponseObjectLinksNext.md) |  | [optional] 
**prev** | [**GetEmployeesResponseObjectLinksPrev**](GetEmployeesResponseObjectLinksPrev.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.get_employees_response_object_links import GetEmployeesResponseObjectLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmployeesResponseObjectLinks from a JSON string
get_employees_response_object_links_instance = GetEmployeesResponseObjectLinks.from_json(json)
# print the JSON string representation of the object
print(GetEmployeesResponseObjectLinks.to_json())

# convert the object into a dict
get_employees_response_object_links_dict = get_employees_response_object_links_instance.to_dict()
# create an instance of GetEmployeesResponseObjectLinks from a dict
get_employees_response_object_links_from_dict = GetEmployeesResponseObjectLinks.from_dict(get_employees_response_object_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


