# EmployeeBenefitsListResponseEmployeeBenefitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | The ID of the employee. | [optional] 
**pay_frequency** | **str** | The employee&#39;s current pay frequency (e.g., &#39;semi-monthly&#39;, &#39;biweekly&#39;), or null if no pay schedule is set. | [optional] 
**employee_benefit** | [**List[EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner]**](EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner.md) | The employee&#39;s benefit plan enrollments, including both current and future scheduled changes. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_benefits_list_response_employee_benefits_inner import EmployeeBenefitsListResponseEmployeeBenefitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeBenefitsListResponseEmployeeBenefitsInner from a JSON string
employee_benefits_list_response_employee_benefits_inner_instance = EmployeeBenefitsListResponseEmployeeBenefitsInner.from_json(json)
# print the JSON string representation of the object
print(EmployeeBenefitsListResponseEmployeeBenefitsInner.to_json())

# convert the object into a dict
employee_benefits_list_response_employee_benefits_inner_dict = employee_benefits_list_response_employee_benefits_inner_instance.to_dict()
# create an instance of EmployeeBenefitsListResponseEmployeeBenefitsInner from a dict
employee_benefits_list_response_employee_benefits_inner_from_dict = EmployeeBenefitsListResponseEmployeeBenefitsInner.from_dict(employee_benefits_list_response_employee_benefits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


