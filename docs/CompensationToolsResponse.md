# CompensationToolsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**tools** | [**CompensationToolsDataObject**](CompensationToolsDataObject.md) |  | [optional] 
**upsell** | [**CompensationUpsellData**](CompensationUpsellData.md) |  | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_tools_response import CompensationToolsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationToolsResponse from a JSON string
compensation_tools_response_instance = CompensationToolsResponse.from_json(json)
# print the JSON string representation of the object
print(CompensationToolsResponse.to_json())

# convert the object into a dict
compensation_tools_response_dict = compensation_tools_response_instance.to_dict()
# create an instance of CompensationToolsResponse from a dict
compensation_tools_response_from_dict = CompensationToolsResponse.from_dict(compensation_tools_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


