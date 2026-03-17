# WhosOutEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The time off request ID or holiday ID. | [optional] 
**type** | **str** | Whether this entry is a time off request or a company holiday. | [optional] 
**employee_id** | **int** | The employee ID. Only present for timeOff entries. | [optional] 
**name** | **str** | The employee name or holiday name. | [optional] 
**start** | **date** | Start date in YYYY-MM-DD format. | [optional] 
**end** | **date** | End date in YYYY-MM-DD format. | [optional] 

## Example

```python
from bamboohr_sdk.models.whos_out_entry import WhosOutEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WhosOutEntry from a JSON string
whos_out_entry_instance = WhosOutEntry.from_json(json)
# print the JSON string representation of the object
print(WhosOutEntry.to_json())

# convert the object into a dict
whos_out_entry_dict = whos_out_entry_instance.to_dict()
# create an instance of WhosOutEntry from a dict
whos_out_entry_from_dict = WhosOutEntry.from_dict(whos_out_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


