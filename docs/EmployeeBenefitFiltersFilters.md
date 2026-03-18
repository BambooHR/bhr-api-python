# EmployeeBenefitFiltersFilters

Scope filters for the request. At least one of employeeId, companyBenefitId, or enrollmentStatusEffectiveDate must be provided; omitting all three returns a 400 validation error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Return benefit enrollments for a specific employee identified by their numeric ID. | [optional] 
**company_benefit_id** | **int** | Return benefit enrollments for a specific company benefit plan identified by its numeric ID. | [optional] 
**enrollment_status_effective_date** | **date** | Return benefit enrollments whose enrollment status became effective on this date. Must be in YYYY-MM-DD format. | [optional] 

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


