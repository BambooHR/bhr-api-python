# LocationResponseObjectAddress

Address information for the location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**state** | [**LocationResponseObjectAddressState**](LocationResponseObjectAddressState.md) |  | [optional] 
**zipcode** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country** | [**LocationResponseObjectAddressCountry**](LocationResponseObjectAddressCountry.md) |  | [optional] 
**timezone** | **str** |  | [optional] 
**remote_location** | **bool** | Whether this is a remote location | [optional] 

## Example

```python
from bamboohr_sdk.models.location_response_object_address import LocationResponseObjectAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LocationResponseObjectAddress from a JSON string
location_response_object_address_instance = LocationResponseObjectAddress.from_json(json)
# print the JSON string representation of the object
print(LocationResponseObjectAddress.to_json())

# convert the object into a dict
location_response_object_address_dict = location_response_object_address_instance.to_dict()
# create an instance of LocationResponseObjectAddress from a dict
location_response_object_address_from_dict = LocationResponseObjectAddress.from_dict(location_response_object_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


