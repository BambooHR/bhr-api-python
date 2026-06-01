# CountriesOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal country identifier. Use the same value as the &#x60;countryId&#x60; path parameter for Get States by Country ID (this endpoint returns JSON numbers, not stringified digits). | [optional] 
**name** | **str** | Full display name of the country | [optional] 
**iso_code** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.countries_options_response import CountriesOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CountriesOptionsResponse from a JSON string
countries_options_response_instance = CountriesOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(CountriesOptionsResponse.to_json())

# convert the object into a dict
countries_options_response_dict = countries_options_response_instance.to_dict()
# create an instance of CountriesOptionsResponse from a dict
countries_options_response_from_dict = CountriesOptionsResponse.from_dict(countries_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


