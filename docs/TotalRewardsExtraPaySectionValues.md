# TotalRewardsExtraPaySectionValues

Schema for total rewards extra pay section values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**comp_summary** | [**TotalRewardsCompSummaryValues**](TotalRewardsCompSummaryValues.md) | Compensation summary values for extra pay | [optional] 
**extra_pay_details** | [**List[TotalRewardsExtraPayDetailsValues]**](TotalRewardsExtraPayDetailsValues.md) | Extra pay details | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_extra_pay_section_values import TotalRewardsExtraPaySectionValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsExtraPaySectionValues from a JSON string
total_rewards_extra_pay_section_values_instance = TotalRewardsExtraPaySectionValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsExtraPaySectionValues.to_json())

# convert the object into a dict
total_rewards_extra_pay_section_values_dict = total_rewards_extra_pay_section_values_instance.to_dict()
# create an instance of TotalRewardsExtraPaySectionValues from a dict
total_rewards_extra_pay_section_values_from_dict = TotalRewardsExtraPaySectionValues.from_dict(total_rewards_extra_pay_section_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


