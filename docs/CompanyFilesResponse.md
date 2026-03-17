# CompanyFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[CompanyFilesResponseCategoriesInner]**](CompanyFilesResponseCategoriesInner.md) | List of company file categories. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_files_response import CompanyFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyFilesResponse from a JSON string
company_files_response_instance = CompanyFilesResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyFilesResponse.to_json())

# convert the object into a dict
company_files_response_dict = company_files_response_instance.to_dict()
# create an instance of CompanyFilesResponse from a dict
company_files_response_from_dict = CompanyFilesResponse.from_dict(company_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


