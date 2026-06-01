# LocationResponseObject

Transformer for location data with nested address structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the location | [optional] 
**label** | **str** | Display name for the location | [optional] 
**archived** | **bool** | Whether the location is archived | [optional] 
**manageable** | **bool** | Whether the location is manageable | [optional] 
**address** | [**LocationResponseObjectAddress**](LocationResponseObjectAddress.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**archived_at** | **datetime** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.location_response_object import LocationResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of LocationResponseObject from a JSON string
location_response_object_instance = LocationResponseObject.from_json(json)
# print the JSON string representation of the object
print(LocationResponseObject.to_json())

# convert the object into a dict
location_response_object_dict = location_response_object_instance.to_dict()
# create an instance of LocationResponseObject from a dict
location_response_object_from_dict = LocationResponseObject.from_dict(location_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


