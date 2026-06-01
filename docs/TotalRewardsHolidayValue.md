# TotalRewardsHolidayValue

Schema for total rewards holiday value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**start_date** | **str** | Start date | [optional] 
**end_date** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_holiday_value import TotalRewardsHolidayValue

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsHolidayValue from a JSON string
total_rewards_holiday_value_instance = TotalRewardsHolidayValue.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsHolidayValue.to_json())

# convert the object into a dict
total_rewards_holiday_value_dict = total_rewards_holiday_value_instance.to_dict()
# create an instance of TotalRewardsHolidayValue from a dict
total_rewards_holiday_value_from_dict = TotalRewardsHolidayValue.from_dict(total_rewards_holiday_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


