# CompanyBenefitSummary

A summary representation of a company benefit plan as returned by the list endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the company benefit plan. | [optional] 
**name** | **str** | The name of the company benefit plan. | [optional] 
**type** | **str** | The benefit category type. | [optional] 
**benefit_vendor_id** | **str** |  | [optional] 
**deduction_type_id** | **str** |  | [optional] 
**company_deduction_id** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**allows_catch_up** | **bool** |  | [optional] 
**allows_super_catch_up** | **bool** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.company_benefit_summary import CompanyBenefitSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyBenefitSummary from a JSON string
company_benefit_summary_instance = CompanyBenefitSummary.from_json(json)
# print the JSON string representation of the object
print(CompanyBenefitSummary.to_json())

# convert the object into a dict
company_benefit_summary_dict = company_benefit_summary_instance.to_dict()
# create an instance of CompanyBenefitSummary from a dict
company_benefit_summary_from_dict = CompanyBenefitSummary.from_dict(company_benefit_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


