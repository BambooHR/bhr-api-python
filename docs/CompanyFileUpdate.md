# CompanyFileUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new display name for the file. | [optional] 
**category_id** | **str** | The ID of the category (file section) to move the file to. | [optional] 
**share_with_employee** | **str** | Whether the file is shared with employees. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_file_update import CompanyFileUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyFileUpdate from a JSON string
company_file_update_instance = CompanyFileUpdate.from_json(json)
# print the JSON string representation of the object
print(CompanyFileUpdate.to_json())

# convert the object into a dict
company_file_update_dict = company_file_update_instance.to_dict()
# create an instance of CompanyFileUpdate from a dict
company_file_update_from_dict = CompanyFileUpdate.from_dict(company_file_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


