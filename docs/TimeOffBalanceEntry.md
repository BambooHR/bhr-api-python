# TimeOffBalanceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_off_type** | **str** | The ID of the time off type. | [optional] 
**name** | **str** | The name of the time off type. | [optional] 
**units** | **str** | The unit of measurement for the balance (e.g. &#39;hours&#39; or &#39;days&#39;). | [optional] 
**balance** | **str** | The calculated time off balance as of the specified date. | [optional] 
**end** | **date** | The date the balance was calculated as of, in YYYY-MM-DD format. | [optional] 
**policy_type** | **str** | The type of time off policy assigned to the employee for this time off type. | [optional] 
**used_year_to_date** | **str** | The amount of time off used year-to-date as of the specified date. | [optional] 

## Example

```python
from bamboohr_sdk.models.time_off_balance_entry import TimeOffBalanceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOffBalanceEntry from a JSON string
time_off_balance_entry_instance = TimeOffBalanceEntry.from_json(json)
# print the JSON string representation of the object
print(TimeOffBalanceEntry.to_json())

# convert the object into a dict
time_off_balance_entry_dict = time_off_balance_entry_instance.to_dict()
# create an instance of TimeOffBalanceEntry from a dict
time_off_balance_entry_from_dict = TimeOffBalanceEntry.from_dict(time_off_balance_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


