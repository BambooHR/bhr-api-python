# CreateLocationRequestAddress

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
from bamboohr_sdk.models.create_location_request_address import CreateLocationRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLocationRequestAddress from a JSON string
create_location_request_address_instance = CreateLocationRequestAddress.from_json(json)
# print the JSON string representation of the object
print(CreateLocationRequestAddress.to_json())

# convert the object into a dict
create_location_request_address_dict = create_location_request_address_instance.to_dict()
# create an instance of CreateLocationRequestAddress from a dict
create_location_request_address_from_dict = CreateLocationRequestAddress.from_dict(create_location_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


