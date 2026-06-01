# PutCompanyIndustryCodesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industry_ids** | **List[Optional[int]]** | List of industry IDs associated with the company. Currently limited to a single entry. | 

## Example

```python
from bamboohr_sdk.models.put_company_industry_codes_request import PutCompanyIndustryCodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutCompanyIndustryCodesRequest from a JSON string
put_company_industry_codes_request_instance = PutCompanyIndustryCodesRequest.from_json(json)
# print the JSON string representation of the object
print(PutCompanyIndustryCodesRequest.to_json())

# convert the object into a dict
put_company_industry_codes_request_dict = put_company_industry_codes_request_instance.to_dict()
# create an instance of PutCompanyIndustryCodesRequest from a dict
put_company_industry_codes_request_from_dict = PutCompanyIndustryCodesRequest.from_dict(put_company_industry_codes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


