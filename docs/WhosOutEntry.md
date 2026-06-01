# WhosOutEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The time off request ID or holiday ID. | [optional] 
**type** | **str** | Whether this entry is a time off request or a company holiday. Entries have two shapes depending on &#x60;type&#x60;: &#x60;timeOff&#x60; entries include &#x60;employeeId&#x60; and &#x60;name&#x60; (the employee&#39;s name); &#x60;holiday&#x60; entries include only &#x60;name&#x60; (the holiday name) and omit &#x60;employeeId&#x60;. Always check &#x60;type&#x60; before accessing &#x60;employeeId&#x60;. | [optional] 
**employee_id** | **int** | The employee ID. Only present for &#x60;timeOff&#x60; entries; omitted for &#x60;holiday&#x60; entries. | [optional] 
**name** | **str** | For &#x60;timeOff&#x60; entries, the employee&#39;s name. For &#x60;holiday&#x60; entries, the holiday&#39;s name. | [optional] 
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


