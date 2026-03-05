# CountrySchema

Schema for country data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the country | [optional] 
**name** | **str** | Full name of the country | [optional] 
**iso_code** | **str** | ISO code for the country | [optional] 

## Example

```python
from bamboohr_sdk.models.country_schema import CountrySchema

# TODO update the JSON string below
json = "{}"
# create an instance of CountrySchema from a JSON string
country_schema_instance = CountrySchema.from_json(json)
# print the JSON string representation of the object
print(CountrySchema.to_json())

# convert the object into a dict
country_schema_dict = country_schema_instance.to_dict()
# create an instance of CountrySchema from a dict
country_schema_from_dict = CountrySchema.from_dict(country_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


