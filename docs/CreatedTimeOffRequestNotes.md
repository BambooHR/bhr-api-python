# CreatedTimeOffRequestNotes

Notes from employee and/or manager. The object is always present; the `employee` and `manager` keys are each included only when a non-empty note was provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee** | **str** | Note from the employee. | [optional] 
**manager** | **str** | Note from the manager. | [optional] 

## Example

```python
from bamboohr_sdk.models.created_time_off_request_notes import CreatedTimeOffRequestNotes

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedTimeOffRequestNotes from a JSON string
created_time_off_request_notes_instance = CreatedTimeOffRequestNotes.from_json(json)
# print the JSON string representation of the object
print(CreatedTimeOffRequestNotes.to_json())

# convert the object into a dict
created_time_off_request_notes_dict = created_time_off_request_notes_instance.to_dict()
# create an instance of CreatedTimeOffRequestNotes from a dict
created_time_off_request_notes_from_dict = CreatedTimeOffRequestNotes.from_dict(created_time_off_request_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


