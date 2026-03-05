# EmployeeBenefit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Employee ID | [optional] 
**company_benefit_id** | **int** | Company benefit ID | [optional] 
**company_benefit_name** | **str** | Company benefit name | [optional] 
**coverage_level** | **str** | Coverage level | [optional] 
**deduction_end_date** | **str** | Deduction end date | [optional] 
**deduction_start_date** | **str** | Deduction start date | [optional] 
**enrollment_status** | **str** | Enrollment status | [optional] 
**effective_date** | **str** | Enrollment status effective date | [optional] 
**currency_code** | **str** | Currency code | [optional] 
**employee_amount** | **float** | Employee amount | [optional] 
**employee_amount_type** | **str** | Employee amount type | [optional] 
**employee_percent_based_on** | **str** | Employee percent based on | [optional] 
**employee_cap_amount** | **float** | Employee cap amount | [optional] 
**employee_cap_amount_type** | **str** | Employee cap amount type | [optional] 
**employee_annual_max** | **float** | Employee annual max | [optional] 
**company_amount** | **float** | Company amount | [optional] 
**company_amount_type** | **str** | Company amount type | [optional] 
**company_percent_based_on** | **str** | Company percent based on | [optional] 
**company_cap_amount** | **float** | Company cap amount | [optional] 
**company_cap_amount_type** | **str** | Company cap amount type | [optional] 
**company_annual_max** | **float** | Company annual max | [optional] 
**benefit_plan_coverage_id** | **float** | Benefit Plan Coverage ID | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_benefit import EmployeeBenefit

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeBenefit from a JSON string
employee_benefit_instance = EmployeeBenefit.from_json(json)
# print the JSON string representation of the object
print(EmployeeBenefit.to_json())

# convert the object into a dict
employee_benefit_dict = employee_benefit_instance.to_dict()
# create an instance of EmployeeBenefit from a dict
employee_benefit_from_dict = EmployeeBenefit.from_dict(employee_benefit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


