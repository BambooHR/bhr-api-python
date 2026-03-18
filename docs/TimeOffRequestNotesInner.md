# TimeOffRequestNotesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Who the note is from. | [optional] 
**note** | **str** | The note text. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request_notes_inner import TimeOffRequestNotesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequestNotesInner from a JSON string
time_off_request_notes_inner_instance = TimeOffRequestNotesInner.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequestNotesInner.to_json())

# convert the object into a dict
time_off_request_notes_inner_dict = time_off_request_notes_inner_instance.to_dict()
# create an instance of TimeOffRequestNotesInner from a dict
time_off_request_notes_inner_from_dict = TimeOffRequestNotesInner.from_dict(time_off_request_notes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


