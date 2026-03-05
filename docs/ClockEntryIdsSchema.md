# ClockEntryIdsSchema

Request body schema for operations involving multiple clock entry IDs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clock_entry_ids** | **List[int]** | Array of clock entry IDs to process | 

## Example

```python
from bamboohr_sdk.models.clock_entry_ids_schema import ClockEntryIdsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ClockEntryIdsSchema from a JSON string
clock_entry_ids_schema_instance = ClockEntryIdsSchema.from_json(json)
# print the JSON string representation of the object
print(ClockEntryIdsSchema.to_json())

# convert the object into a dict
clock_entry_ids_schema_dict = clock_entry_ids_schema_instance.to_dict()
# create an instance of ClockEntryIdsSchema from a dict
clock_entry_ids_schema_from_dict = ClockEntryIdsSchema.from_dict(clock_entry_ids_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


