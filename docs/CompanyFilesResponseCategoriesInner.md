# CompanyFilesResponseCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category ID. | [optional] 
**name** | **str** | Category display name. | [optional] 
**can_upload_files** | **str** | Whether the requesting user can upload files to this category. | [optional] 
**files** | [**List[CompanyFilesResponseCategoriesInnerFilesInner]**](CompanyFilesResponseCategoriesInnerFilesInner.md) | Files visible to the requesting user in this category. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_files_response_categories_inner import CompanyFilesResponseCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyFilesResponseCategoriesInner from a JSON string
company_files_response_categories_inner_instance = CompanyFilesResponseCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(CompanyFilesResponseCategoriesInner.to_json())

# convert the object into a dict
company_files_response_categories_inner_dict = company_files_response_categories_inner_instance.to_dict()
# create an instance of CompanyFilesResponseCategoriesInner from a dict
company_files_response_categories_inner_from_dict = CompanyFilesResponseCategoriesInner.from_dict(company_files_response_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


