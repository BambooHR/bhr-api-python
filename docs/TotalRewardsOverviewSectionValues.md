# TotalRewardsOverviewSectionValues

Schema for total rewards overview section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_total_comp_value** | **str** |  | [optional] 
**paid_per** | **str** |  | [optional] 
**multiplier_value** | **float** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_overview_section_values import TotalRewardsOverviewSectionValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsOverviewSectionValues from a JSON string
total_rewards_overview_section_values_instance = TotalRewardsOverviewSectionValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsOverviewSectionValues.to_json())

# convert the object into a dict
total_rewards_overview_section_values_dict = total_rewards_overview_section_values_instance.to_dict()
# create an instance of TotalRewardsOverviewSectionValues from a dict
total_rewards_overview_section_values_from_dict = TotalRewardsOverviewSectionValues.from_dict(total_rewards_overview_section_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


