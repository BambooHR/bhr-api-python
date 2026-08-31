# ClockInRequestSchema

Schema for clock-in request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 
**start** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**break_id** | **str** |  | [optional] 
**offline** | **bool** | Whether this is an offline punch. When true, bypasses the shift schedule clock-in restriction. Intended for devices that store punches offline and sync later. | [optional] 

## Example

```python
from bamboohr_sdk.models.clock_in_request_schema import ClockInRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ClockInRequestSchema from a JSON string
clock_in_request_schema_instance = ClockInRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ClockInRequestSchema.to_json())

# convert the object into a dict
clock_in_request_schema_dict = clock_in_request_schema_instance.to_dict()
# create an instance of ClockInRequestSchema from a dict
clock_in_request_schema_from_dict = ClockInRequestSchema.from_dict(clock_in_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


