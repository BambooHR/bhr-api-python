# CompensationToolsDataObject

Schema for the compensation tools list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**levels_and_bands** | **bool** | Has access to Levels &amp; Bands tool | [optional] 
**compensation_benchmarking** | **bool** | Has access to Compensation Benchmarking tool | [optional] 
**compensation_planning** | **bool** | Has access to Compensation Planning tool | [optional] 
**total_rewards** | **bool** | Has access to Total Rewards tool | [optional] 

## Example

```python
from bamboohr_sdk.models.compensation_tools_data_object import CompensationToolsDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of CompensationToolsDataObject from a JSON string
compensation_tools_data_object_instance = CompensationToolsDataObject.from_json(json)
# print the JSON string representation of the object
print(CompensationToolsDataObject.to_json())

# convert the object into a dict
compensation_tools_data_object_dict = compensation_tools_data_object_instance.to_dict()
# create an instance of CompensationToolsDataObject from a dict
compensation_tools_data_object_from_dict = CompensationToolsDataObject.from_dict(compensation_tools_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


