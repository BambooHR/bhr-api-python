# HourEntryIdsSchema

Request body schema for operations involving multiple hour entry IDs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour_entry_ids** | **List[int]** | Array of hour entry IDs to process | 

## Example

```python
from bamboohr_sdk.models.hour_entry_ids_schema import HourEntryIdsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HourEntryIdsSchema from a JSON string
hour_entry_ids_schema_instance = HourEntryIdsSchema.from_json(json)
# print the JSON string representation of the object
print(HourEntryIdsSchema.to_json())

# convert the object into a dict
hour_entry_ids_schema_dict = hour_entry_ids_schema_instance.to_dict()
# create an instance of HourEntryIdsSchema from a dict
hour_entry_ids_schema_from_dict = HourEntryIdsSchema.from_dict(hour_entry_ids_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


