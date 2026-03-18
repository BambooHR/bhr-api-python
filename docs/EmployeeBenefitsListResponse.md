# EmployeeBenefitsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_benefits** | [**List[EmployeeBenefitsListResponseEmployeeBenefitsInner]**](EmployeeBenefitsListResponseEmployeeBenefitsInner.md) | List of per-employee benefit enrollment records. | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_benefits_list_response import EmployeeBenefitsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeBenefitsListResponse from a JSON string
employee_benefits_list_response_instance = EmployeeBenefitsListResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeBenefitsListResponse.to_json())

# convert the object into a dict
employee_benefits_list_response_dict = employee_benefits_list_response_instance.to_dict()
# create an instance of EmployeeBenefitsListResponse from a dict
employee_benefits_list_response_from_dict = EmployeeBenefitsListResponse.from_dict(employee_benefits_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


