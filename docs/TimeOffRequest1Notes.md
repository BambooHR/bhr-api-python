# TimeOffRequest1Notes

Notes from employee and/or manager. Omitted when `excludeNote` is set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee** | **str** | Note from the employee. | [optional] 
**manager** | **str** | Note from the manager. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_request1_notes import TimeOffRequest1Notes

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffRequest1Notes from a JSON string
time_off_request1_notes_instance = TimeOffRequest1Notes.from_json(json)
# print the JSON string representation of the object
print(TimeOffRequest1Notes.to_json())

# convert the object into a dict
time_off_request1_notes_dict = time_off_request1_notes_instance.to_dict()
# create an instance of TimeOffRequest1Notes from a dict
time_off_request1_notes_from_dict = TimeOffRequest1Notes.from_dict(time_off_request1_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


