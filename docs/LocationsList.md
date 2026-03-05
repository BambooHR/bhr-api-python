# LocationsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**Location**](Location.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.locations_list import LocationsList

# TODO update the JSON string below
json = "{}"
# create an instance of LocationsList from a JSON string
locations_list_instance = LocationsList.from_json(json)
# print the JSON string representation of the object
print(LocationsList.to_json())

# convert the object into a dict
locations_list_dict = locations_list_instance.to_dict()
# create an instance of LocationsList from a dict
locations_list_from_dict = LocationsList.from_dict(locations_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


