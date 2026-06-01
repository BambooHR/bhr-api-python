# TotalRewardsCompSummaryValues

Schema for total rewards compensation summary values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**subtitle** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**subvalue** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_comp_summary_values import TotalRewardsCompSummaryValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsCompSummaryValues from a JSON string
total_rewards_comp_summary_values_instance = TotalRewardsCompSummaryValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsCompSummaryValues.to_json())

# convert the object into a dict
total_rewards_comp_summary_values_dict = total_rewards_comp_summary_values_instance.to_dict()
# create an instance of TotalRewardsCompSummaryValues from a dict
total_rewards_comp_summary_values_from_dict = TotalRewardsCompSummaryValues.from_dict(total_rewards_comp_summary_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


