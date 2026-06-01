# BankHoliday


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Stable bank holiday identifier | [optional] 
**name** | **str** | Holiday display name | [optional] 
**var_date** | **date** | Holiday date in YYYY-MM-DD form | [optional] 

## Example

```python
from bamboohr_sdk.models.bank_holiday import BankHoliday

# TODO update the JSON string below
json = "{}"
# create an instance of BankHoliday from a JSON string
bank_holiday_instance = BankHoliday.from_json(json)
# print the JSON string representation of the object
print(BankHoliday.to_json())

# convert the object into a dict
bank_holiday_dict = bank_holiday_instance.to_dict()
# create an instance of BankHoliday from a dict
bank_holiday_from_dict = BankHoliday.from_dict(bank_holiday_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


