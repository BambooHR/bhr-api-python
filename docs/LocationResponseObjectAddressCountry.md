# LocationResponseObjectAddressCountry

Country information. Optional and requested via expand property from the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Country identifier | [optional] 
**name** | **str** | Country name | [optional] 
**iso_code** | **str** | Country ISO code | [optional] 

## Example

```python
from bamboohr_sdk.models.location_response_object_address_country import LocationResponseObjectAddressCountry

# TODO update the JSON string below
json = "{}"
# create an instance of LocationResponseObjectAddressCountry from a JSON string
location_response_object_address_country_instance = LocationResponseObjectAddressCountry.from_json(json)
# print the JSON string representation of the object
print(LocationResponseObjectAddressCountry.to_json())

# convert the object into a dict
location_response_object_address_country_dict = location_response_object_address_country_instance.to_dict()
# create an instance of LocationResponseObjectAddressCountry from a dict
location_response_object_address_country_from_dict = LocationResponseObjectAddressCountry.from_dict(location_response_object_address_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


