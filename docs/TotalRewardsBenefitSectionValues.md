# TotalRewardsBenefitSectionValues

Schema for a total rewards benefit section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comp_summary** | [**TotalRewardsCompSummaryValues**](TotalRewardsCompSummaryValues.md) | Compensation summary | [optional] 
**benefit_details** | [**List[TotalRewardsBenefitDetailsValues]**](TotalRewardsBenefitDetailsValues.md) | Benefit details | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_benefit_section_values import TotalRewardsBenefitSectionValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsBenefitSectionValues from a JSON string
total_rewards_benefit_section_values_instance = TotalRewardsBenefitSectionValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsBenefitSectionValues.to_json())

# convert the object into a dict
total_rewards_benefit_section_values_dict = total_rewards_benefit_section_values_instance.to_dict()
# create an instance of TotalRewardsBenefitSectionValues from a dict
total_rewards_benefit_section_values_from_dict = TotalRewardsBenefitSectionValues.from_dict(total_rewards_benefit_section_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


