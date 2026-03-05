# EmployeeBenefitFiltersFilters

At least one filter is required

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Employee Id | [optional] 
**company_benefit_id** | **int** | Company Benefit Id | [optional] 
**enrollment_status_effective_date** | **str** | Enrollment Status Effective Date | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_benefit_filters_filters import EmployeeBenefitFiltersFilters

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeBenefitFiltersFilters from a JSON string
employee_benefit_filters_filters_instance = EmployeeBenefitFiltersFilters.from_json(json)
# print the JSON string representation of the object
print(EmployeeBenefitFiltersFilters.to_json())

# convert the object into a dict
employee_benefit_filters_filters_dict = employee_benefit_filters_filters_instance.to_dict()
# create an instance of EmployeeBenefitFiltersFilters from a dict
employee_benefit_filters_filters_from_dict = EmployeeBenefitFiltersFilters.from_dict(employee_benefit_filters_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


