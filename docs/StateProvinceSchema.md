# StateProvinceSchema

Schema for state/province data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | State/province ID | [optional] 
**label** | **str** | State/province abbreviation | [optional] 
**iso** | **str** | ISO code for the state/province | [optional] 
**name** | **str** | Full name of the state/province | [optional] 

## Example

```python
from bamboohr_sdk.models.state_province_schema import StateProvinceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StateProvinceSchema from a JSON string
state_province_schema_instance = StateProvinceSchema.from_json(json)
# print the JSON string representation of the object
print(StateProvinceSchema.to_json())

# convert the object into a dict
state_province_schema_dict = state_province_schema_instance.to_dict()
# create an instance of StateProvinceSchema from a dict
state_province_schema_from_dict = StateProvinceSchema.from_dict(state_province_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


