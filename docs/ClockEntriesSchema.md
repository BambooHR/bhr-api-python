# ClockEntriesSchema

Request body schema for operations involving multiple clock entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ClockEntrySchema]**](ClockEntrySchema.md) | Array of clock entries | 

## Example

```python
from bamboohr_sdk.models.clock_entries_schema import ClockEntriesSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ClockEntriesSchema from a JSON string
clock_entries_schema_instance = ClockEntriesSchema.from_json(json)
# print the JSON string representation of the object
print(ClockEntriesSchema.to_json())

# convert the object into a dict
clock_entries_schema_dict = clock_entries_schema_instance.to_dict()
# create an instance of ClockEntriesSchema from a dict
clock_entries_schema_from_dict = ClockEntriesSchema.from_dict(clock_entries_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


