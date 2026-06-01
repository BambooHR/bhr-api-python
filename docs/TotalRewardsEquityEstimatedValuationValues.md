# TotalRewardsEquityEstimatedValuationValues

Schema for total rewards equity growth valuation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equity_growth_estimation_items** | [**List[TotalRewardsEquityGrowthEstimation]**](TotalRewardsEquityGrowthEstimation.md) | Equity estimated growth items | [optional] 
**number_of_vested_shares** | **int** | Number of vested shares | [optional] 
**number_of_total_shares** | **int** | Number of total shares | [optional] 
**equity_growth_slider_max** | **int** |  | [optional] 
**equity_growth_slider_min** | **int** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_equity_estimated_valuation_values import TotalRewardsEquityEstimatedValuationValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsEquityEstimatedValuationValues from a JSON string
total_rewards_equity_estimated_valuation_values_instance = TotalRewardsEquityEstimatedValuationValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsEquityEstimatedValuationValues.to_json())

# convert the object into a dict
total_rewards_equity_estimated_valuation_values_dict = total_rewards_equity_estimated_valuation_values_instance.to_dict()
# create an instance of TotalRewardsEquityEstimatedValuationValues from a dict
total_rewards_equity_estimated_valuation_values_from_dict = TotalRewardsEquityEstimatedValuationValues.from_dict(total_rewards_equity_estimated_valuation_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


