# CompanyBenefitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**benefit_vendor_id** | **str** | Benefit vendor ID | [optional] 
**benefit_type** | **str** | Benefit type | [optional] 
**deduction_type_id** | **int** | Deduction type ID | [optional] 
**start_date** | **str** | Benefit start date | [optional] 
**end_date** | **str** | Benefit end date | [optional] 
**description** | **str** | Description | [optional] 
**plan_url** | **str** | Plan url | [optional] 
**sso_login_url** | **str** | SSO login url | [optional] 
**sso_login_url_link_text** | **str** | SSO login link text | [optional] 
**safe_harbor** | **str** | Is a safe harbor | [optional] 
**meet_aca_min** | **str** | Meets ACA minimum requirements | [optional] 
**reimbursement_amount** | **float** | Reimbursement amount | [optional] 
**reimbursement_frequency** | **str** | Reimbursement frequency | [optional] 
**min_essential_coverage** | **str** | Provides minimum essential coverage | [optional] 

## Example

```python
from bamboohr_sdk.models.company_benefit_response import CompanyBenefitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyBenefitResponse from a JSON string
company_benefit_response_instance = CompanyBenefitResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyBenefitResponse.to_json())

# convert the object into a dict
company_benefit_response_dict = company_benefit_response_instance.to_dict()
# create an instance of CompanyBenefitResponse from a dict
company_benefit_response_from_dict = CompanyBenefitResponse.from_dict(company_benefit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


