# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the location | [optional] 
**name** | **str** | Name of the location | [optional] 
**description** | **str** | Description of the location | [optional] 
**city** | **str** | City of the location | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**zipcode** | **str** | The ZIP or postal code of the location | [optional] 
**address_line1** | **str** | The first address line of the location | [optional] 
**address_line2** | **str** | The second address line of the location | [optional] 
**phone** | **str** | The phone number of the location | [optional] 

## Example

```python
from bamboohr_sdk.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


