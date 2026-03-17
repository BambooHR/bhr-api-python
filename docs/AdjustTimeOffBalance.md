# AdjustTimeOffBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date the adjustment should be added in history. Should be in ISO8601 date format (YYYY-MM-DD). | 
**time_off_type_id** | **int** | The ID of the time off type to add a balance adjustment for. | 
**amount** | **float** | The number of hours/days to adjust the balance by. | 
**note** | **str** | This is an optional note to show in history. | [optional] 

## Example

```python
from bamboohr_sdk.models.adjust_time_off_balance import AdjustTimeOffBalance

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustTimeOffBalance from a JSON string
adjust_time_off_balance_instance = AdjustTimeOffBalance.from_json(json)
# print the JSON string representation of the object
print(AdjustTimeOffBalance.to_json())

# convert the object into a dict
adjust_time_off_balance_dict = adjust_time_off_balance_instance.to_dict()
# create an instance of AdjustTimeOffBalance from a dict
adjust_time_off_balance_from_dict = AdjustTimeOffBalance.from_dict(adjust_time_off_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


