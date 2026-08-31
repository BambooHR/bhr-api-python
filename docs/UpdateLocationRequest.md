# UpdateLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Updated display name | 
**archived** | **bool** | Whether the location is archived | [optional] [default to False]
**address** | [**UpdateLocationRequestAddress**](UpdateLocationRequestAddress.md) |  | 

## Example

```python
from bamboohr_sdk.models.update_location_request import UpdateLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLocationRequest from a JSON string
update_location_request_instance = UpdateLocationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateLocationRequest.to_json())

# convert the object into a dict
update_location_request_dict = update_location_request_instance.to_dict()
# create an instance of UpdateLocationRequest from a dict
update_location_request_from_dict = UpdateLocationRequest.from_dict(update_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


