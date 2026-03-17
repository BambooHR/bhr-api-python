# EmployeeBenefitFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**EmployeeBenefitFiltersFilters**](EmployeeBenefitFiltersFilters.md) |  | 

## Example

```python
from bamboohr_sdk.models.employee_benefit_filters import EmployeeBenefitFilters

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeBenefitFilters from a JSON string
employee_benefit_filters_instance = EmployeeBenefitFilters.from_json(json)
# print the JSON string representation of the object
print(EmployeeBenefitFilters.to_json())

# convert the object into a dict
employee_benefit_filters_dict = employee_benefit_filters_instance.to_dict()
# create an instance of EmployeeBenefitFilters from a dict
employee_benefit_filters_from_dict = EmployeeBenefitFilters.from_dict(employee_benefit_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


