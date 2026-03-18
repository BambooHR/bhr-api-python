# CompanyBenefitsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_benefits** | [**List[CompanyBenefitSummary]**](CompanyBenefitSummary.md) | List of company benefit plan summaries. | [optional] 

## Example

```python
from bamboohr_sdk.models.company_benefits_list_response import CompanyBenefitsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyBenefitsListResponse from a JSON string
company_benefits_list_response_instance = CompanyBenefitsListResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyBenefitsListResponse.to_json())

# convert the object into a dict
company_benefits_list_response_dict = company_benefits_list_response_instance.to_dict()
# create an instance of CompanyBenefitsListResponse from a dict
company_benefits_list_response_from_dict = CompanyBenefitsListResponse.from_dict(company_benefits_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


