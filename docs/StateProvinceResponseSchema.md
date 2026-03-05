# StateProvinceResponseSchema

Schema for states/provinces response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**List[StateProvinceSchema]**](StateProvinceSchema.md) | Array of state/province options | [optional] 

## Example

```python
from bamboohr_sdk.models.state_province_response_schema import StateProvinceResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StateProvinceResponseSchema from a JSON string
state_province_response_schema_instance = StateProvinceResponseSchema.from_json(json)
# print the JSON string representation of the object
print(StateProvinceResponseSchema.to_json())

# convert the object into a dict
state_province_response_schema_dict = state_province_response_schema_instance.to_dict()
# create an instance of StateProvinceResponseSchema from a dict
state_province_response_schema_from_dict = StateProvinceResponseSchema.from_dict(state_province_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


