# StateProvinceSchema

One state or province (subdivision) row. The same field meanings as each element of `StateProvinceResponseSchema.options` from `GET /api/v1/meta/provinces/{countryId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | State/province ID | [optional] 
**label** | **str** | Subdivision abbreviation (e.g. \&quot;UT\&quot; for Utah). This is the short code used in &#x60;options[].label&#x60;, not the full name (see &#x60;name&#x60;). | [optional] 
**iso** | **str** | ISO 3166-2 subdivision code (e.g. \&quot;US-UT\&quot; for Utah). | [optional] 
**name** | **str** | Full subdivision name (e.g. \&quot;Utah\&quot;), distinct from the abbreviation in &#x60;label&#x60;. | [optional] 

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


