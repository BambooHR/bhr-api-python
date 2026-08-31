# CreateLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Display name for the location | 
**archived** | **bool** | Whether the location is archived | [optional] [default to False]
**address** | [**CreateLocationRequestAddress**](CreateLocationRequestAddress.md) |  | 

## Example

```python
from bamboohr_sdk.models.create_location_request import CreateLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLocationRequest from a JSON string
create_location_request_instance = CreateLocationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateLocationRequest.to_json())

# convert the object into a dict
create_location_request_dict = create_location_request_instance.to_dict()
# create an instance of CreateLocationRequest from a dict
create_location_request_from_dict = CreateLocationRequest.from_dict(create_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


