# CompanyFilesResponseCategoriesInnerFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File ID. | [optional] 
**name** | **str** | File display name. | [optional] 
**original_file_name** | **str** | Original uploaded filename including extension. | [optional] 
**size** | **str** | File size in bytes. | [optional] 
**date_created** | **str** | Timestamp of when the file was uploaded, in ISO 8601 format with UTC offset (e.g. &#x60;2025-02-11T22:30:07+0000&#x60;). | [optional] 
**created_by** | **str** | Full name of the user who uploaded the file. | [optional] 
**share_with_employees** | **str** | Whether the file is shared with all employees. | [optional] 
**can_rename_file** | **str** | Whether the requesting user can rename this file. | [optional] 
**can_delete_file** | **str** | Whether the requesting user can delete this file. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_files_response_categories_inner_files_inner import CompanyFilesResponseCategoriesInnerFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyFilesResponseCategoriesInnerFilesInner from a JSON string
company_files_response_categories_inner_files_inner_instance = CompanyFilesResponseCategoriesInnerFilesInner.from_json(json)
# print the JSON string representation of the object
print(CompanyFilesResponseCategoriesInnerFilesInner.to_json())

# convert the object into a dict
company_files_response_categories_inner_files_inner_dict = company_files_response_categories_inner_files_inner_instance.to_dict()
# create an instance of CompanyFilesResponseCategoriesInnerFilesInner from a dict
company_files_response_categories_inner_files_inner_from_dict = CompanyFilesResponseCategoriesInnerFilesInner.from_dict(company_files_response_categories_inner_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


