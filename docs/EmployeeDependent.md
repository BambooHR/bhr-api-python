# EmployeeDependent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**relationship** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**ssn** | **str** |  | [optional] 
**date_of_birth** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**home_phone** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**is_us_citizen** | **str** |  | [optional] 
**is_student** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.employee_dependent import EmployeeDependent

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeDependent from a JSON string
employee_dependent_instance = EmployeeDependent.from_json(json)
# print the JSON string representation of the object
print(EmployeeDependent.to_json())

# convert the object into a dict
employee_dependent_dict = employee_dependent_instance.to_dict()
# create an instance of EmployeeDependent from a dict
employee_dependent_from_dict = EmployeeDependent.from_dict(employee_dependent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


