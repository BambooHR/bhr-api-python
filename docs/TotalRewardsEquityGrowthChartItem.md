# TotalRewardsEquityGrowthChartItem

Schema for total rewards equity growth chart item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label | [optional] 
**estimated_net_value** | **str** | Estimated value | [optional] 
**subvalue** | **str** |  | [optional] 
**vested** | **float** |  | [optional] 
**current** | **float** |  | [optional] 
**unvested** | **float** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_equity_growth_chart_item import TotalRewardsEquityGrowthChartItem

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsEquityGrowthChartItem from a JSON string
total_rewards_equity_growth_chart_item_instance = TotalRewardsEquityGrowthChartItem.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsEquityGrowthChartItem.to_json())

# convert the object into a dict
total_rewards_equity_growth_chart_item_dict = total_rewards_equity_growth_chart_item_instance.to_dict()
# create an instance of TotalRewardsEquityGrowthChartItem from a dict
total_rewards_equity_growth_chart_item_from_dict = TotalRewardsEquityGrowthChartItem.from_dict(total_rewards_equity_growth_chart_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


