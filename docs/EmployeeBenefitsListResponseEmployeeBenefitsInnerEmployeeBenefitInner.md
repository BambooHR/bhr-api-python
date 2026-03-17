# EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_benefit_id** | **str** | The ID of the company benefit plan. | [optional] 
**company_benefit_name** | **str** | The name of the company benefit plan. | [optional] 
**coverage_level** | **str** | The coverage level for this enrollment, or null if not applicable. | [optional] 
**deduction_start_date** | **date** | The date deductions begin for this enrollment (YYYY-MM-DD), or null. | [optional] 
**deduction_end_date** | **date** | The date deductions end for this enrollment (YYYY-MM-DD), or null. | [optional] 
**enrollment_status** | **str** | The current or scheduled enrollment status. | [optional] 
**enrollment_status_effective_date** | **date** | The date the enrollment status takes effect (YYYY-MM-DD). | [optional] 
**currency_code** | **str** | ISO 4217 currency code for deduction amounts, or null if not applicable. | [optional] 
**employee_amount** | **float** | The employee-paid deduction amount. | [optional] 
**employee_amount_type** | **str** | The unit for employeeAmount (e.g., &#39;%&#39;, &#39;$&#39;). | [optional] 
**employee_percent_based_on** | **str** | The basis for percent-based employee deductions (e.g., &#39;Gross&#39;), or null. | [optional] 
**employee_cap_amount** | **float** | The cap on employee deductions, or null if none. | [optional] 
**employee_cap_amount_type** | **str** | The unit for employeeCapAmount, or null. | [optional] 
**employee_annual_max** | **float** | The annual maximum employee contribution, or null if none. | [optional] 
**company_amount** | **float** | The employer-paid contribution amount. | [optional] 
**company_amount_type** | **str** | The unit for companyAmount (e.g., &#39;%&#39;, &#39;$&#39;). | [optional] 
**company_percent_based_on** | **str** | The basis for percent-based employer contributions (e.g., &#39;Gross&#39;), or null. | [optional] 
**company_cap_amount** | **float** | The cap on employer contributions, or null if none. | [optional] 
**company_cap_amount_type** | **str** | The unit for companyCapAmount, or null. | [optional] 
**company_annual_max** | **float** | The annual maximum employer contribution, or null if none. | [optional] 
**occurrences_per_year** | **int** | The number of deduction occurrences per year based on the employee&#39;s pay schedule. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_benefits_list_response_employee_benefits_inner_employee_benefit_inner import EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner from a JSON string
employee_benefits_list_response_employee_benefits_inner_employee_benefit_inner_instance = EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner.from_json(json)
# print the JSON string representation of the object
print(EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner.to_json())

# convert the object into a dict
employee_benefits_list_response_employee_benefits_inner_employee_benefit_inner_dict = employee_benefits_list_response_employee_benefits_inner_employee_benefit_inner_instance.to_dict()
# create an instance of EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner from a dict
employee_benefits_list_response_employee_benefits_inner_employee_benefit_inner_from_dict = EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner.from_dict(employee_benefits_list_response_employee_benefits_inner_employee_benefit_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


