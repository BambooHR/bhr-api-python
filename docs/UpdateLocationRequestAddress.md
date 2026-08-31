# UpdateLocationRequestAddress

Address details for the location. When remoteLocation is true, none are required and must be null or omitted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**remote_location** | **bool** |  | 

## Example

```python
from bamboohr_sdk.models.update_location_request_address import UpdateLocationRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLocationRequestAddress from a JSON string
update_location_request_address_instance = UpdateLocationRequestAddress.from_json(json)
# print the JSON string representation of the object
print(UpdateLocationRequestAddress.to_json())

# convert the object into a dict
update_location_request_address_dict = update_location_request_address_instance.to_dict()
# create an instance of UpdateLocationRequestAddress from a dict
update_location_request_address_from_dict = UpdateLocationRequestAddress.from_dict(update_location_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


