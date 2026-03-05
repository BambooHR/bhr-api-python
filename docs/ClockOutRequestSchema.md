# ClockOutRequestSchema

Schema for clock out request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date for the timesheet entry. Must be in YYYY-MM-DD format. | [optional] 
**end** | **str** | The time for the clock out. In 24 hour format HH:MM | [optional] 
**timezone** | **str** | The timezone associated with the clock out. | [optional] 

## Example

```python
from bamboohr_sdk.models.clock_out_request_schema import ClockOutRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ClockOutRequestSchema from a JSON string
clock_out_request_schema_instance = ClockOutRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ClockOutRequestSchema.to_json())

# convert the object into a dict
clock_out_request_schema_dict = clock_out_request_schema_instance.to_dict()
# create an instance of ClockOutRequestSchema from a dict
clock_out_request_schema_from_dict = ClockOutRequestSchema.from_dict(clock_out_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


