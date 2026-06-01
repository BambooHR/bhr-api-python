# TotalRewardsCalendarSectionValues

Schema for total rewards calendar section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holidays** | [**List[TotalRewardsHolidayValue]**](TotalRewardsHolidayValue.md) | List of holidays | [optional] 
**time_off_policies** | [**List[TotalRewardsTimeOffPolicyValue]**](TotalRewardsTimeOffPolicyValue.md) | List of time off policies | [optional] 
**hourly_accrual_disclaimer** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_calendar_section_values import TotalRewardsCalendarSectionValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsCalendarSectionValues from a JSON string
total_rewards_calendar_section_values_instance = TotalRewardsCalendarSectionValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsCalendarSectionValues.to_json())

# convert the object into a dict
total_rewards_calendar_section_values_dict = total_rewards_calendar_section_values_instance.to_dict()
# create an instance of TotalRewardsCalendarSectionValues from a dict
total_rewards_calendar_section_values_from_dict = TotalRewardsCalendarSectionValues.from_dict(total_rewards_calendar_section_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


