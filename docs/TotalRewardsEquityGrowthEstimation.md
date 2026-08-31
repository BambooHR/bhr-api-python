# TotalRewardsEquityGrowthEstimation

Schema for total rewards equity growth estimation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stop** | **int** | Stop | [optional] 
**company_valuation** | **str** | Company valuation | [optional] 
**company_valuation_subvalue** | **str** |  | [optional] 
**total_value** | **str** | Total value | [optional] 
**total_value_subvalue** | **str** |  | [optional] 
**vested_value** | **str** | Vested amount value | [optional] 
**vested_value_subvalue** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_equity_growth_estimation import TotalRewardsEquityGrowthEstimation

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsEquityGrowthEstimation from a JSON string
total_rewards_equity_growth_estimation_instance = TotalRewardsEquityGrowthEstimation.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsEquityGrowthEstimation.to_json())

# convert the object into a dict
total_rewards_equity_growth_estimation_dict = total_rewards_equity_growth_estimation_instance.to_dict()
# create an instance of TotalRewardsEquityGrowthEstimation from a dict
total_rewards_equity_growth_estimation_from_dict = TotalRewardsEquityGrowthEstimation.from_dict(total_rewards_equity_growth_estimation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


