# InlineObject2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emp_dep_first_name** | **str** |  | [optional] 
**emp_dep_last_name** | **str** |  | [optional] 
**emp_dep_middlename** | **str** |  | [optional] 
**emp_dep_add1** | **str** |  | [optional] 
**emp_dep_add2** | **str** |  | [optional] 
**emp_dep_city** | **str** |  | [optional] 
**emp_dep_relationship** | **str** |  | [optional] 
**employee_dependent_ssn** | **str** |  | [optional] 
**employee_dependent_sin** | **str** |  | [optional] 
**emp_dep_state** | **str** |  | [optional] 
**emp_dep_zip_code** | **str** |  | [optional] 
**emp_dep_gender** | **str** |  | [optional] 
**emp_dep_birthday** | **str** |  | [optional] 
**emp_dep_ft_student** | **str** |  | [optional] 
**emp_dep_us_citizen** | **str** |  | [optional] 
**emp_dep_home_phone** | **str** |  | [optional] 
**emp_dep_country** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.inline_object2 import InlineObject2

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject2 from a JSON string
inline_object2_instance = InlineObject2.from_json(json)
# print the JSON string representation of the object
print(InlineObject2.to_json())

# convert the object into a dict
inline_object2_dict = inline_object2_instance.to_dict()
# create an instance of InlineObject2 from a dict
inline_object2_from_dict = InlineObject2.from_dict(inline_object2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


