# LocationResponseObjectAddressState

State information. Optional and requested via expand property from the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | State identifier | [optional] 
**name** | **str** | State name | [optional] 
**abbreviation** | **str** | State abbreviation | [optional] 

## Example

```python
from bamboohr_sdk.models.location_response_object_address_state import LocationResponseObjectAddressState

# TODO update the JSON string below
json = "{}"
# create an instance of LocationResponseObjectAddressState from a JSON string
location_response_object_address_state_instance = LocationResponseObjectAddressState.from_json(json)
# print the JSON string representation of the object
print(LocationResponseObjectAddressState.to_json())

# convert the object into a dict
location_response_object_address_state_dict = location_response_object_address_state_instance.to_dict()
# create an instance of LocationResponseObjectAddressState from a dict
location_response_object_address_state_from_dict = LocationResponseObjectAddressState.from_dict(location_response_object_address_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


