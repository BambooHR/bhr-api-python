# HourEntriesRequestSchema

Schema for timesheet hour entries request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | [**List[HourEntrySchema]**](HourEntrySchema.md) | Array of hour entries to add or update | 

## Example

```python
from bamboohr_sdk.models.hour_entries_request_schema import HourEntriesRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HourEntriesRequestSchema from a JSON string
hour_entries_request_schema_instance = HourEntriesRequestSchema.from_json(json)
# print the JSON string representation of the object
print(HourEntriesRequestSchema.to_json())

# convert the object into a dict
hour_entries_request_schema_dict = hour_entries_request_schema_instance.to_dict()
# create an instance of HourEntriesRequestSchema from a dict
hour_entries_request_schema_from_dict = HourEntriesRequestSchema.from_dict(hour_entries_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


