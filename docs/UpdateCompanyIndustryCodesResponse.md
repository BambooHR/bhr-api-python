# UpdateCompanyIndustryCodesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_industries** | [**List[CompanyIndustryDataObject]**](CompanyIndustryDataObject.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.update_company_industry_codes_response import UpdateCompanyIndustryCodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompanyIndustryCodesResponse from a JSON string
update_company_industry_codes_response_instance = UpdateCompanyIndustryCodesResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCompanyIndustryCodesResponse.to_json())

# convert the object into a dict
update_company_industry_codes_response_dict = update_company_industry_codes_response_instance.to_dict()
# create an instance of UpdateCompanyIndustryCodesResponse from a dict
update_company_industry_codes_response_from_dict = UpdateCompanyIndustryCodesResponse.from_dict(update_company_industry_codes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


