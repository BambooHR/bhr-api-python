# TotalRewardsEquityDetailsValues

Schema for total rewards equity details values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cliff_months** | **int** |  | [optional] 
**estimated_exercise_cost** | **str** |  | [optional] 
**estimated_exercise_cost_subvalue** | **str** |  | [optional] 
**estimated_share_price** | **str** | Estimated share price | [optional] 
**estimated_share_price_subvalue** | **str** |  | [optional] 
**estimated_total_value** | **str** | Estimated total value | [optional] 
**estimated_total_value_subvalue** | **str** |  | [optional] 
**grant_date** | **date** | Grant date | [optional] 
**grant_type** | **str** | Grant type | [optional] 
**grant_name** | **str** |  | [optional] 
**equity_growth_chart_data** | [**List[TotalRewardsEquityGrowthChartItem]**](TotalRewardsEquityGrowthChartItem.md) |  | [optional] 
**num_shares** | **int** | Number of shares | [optional] 
**num_vested_shares** | **int** | Number of vested shares | [optional] 
**percent_vested** | **float** | Percent vested | [optional] 
**strike_price** | **str** |  | [optional] 
**strike_price_subvalue** | **str** |  | [optional] 
**vesting_months** | **int** |  | [optional] 
**vesting_schedule** | **str** | Vesting schedule | [optional] 
**vesting_start_date** | **date** | Vesting start date | [optional] 
**vested_value** | **str** | Vested value | [optional] 
**vested_value_subvalue** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_equity_details_values import TotalRewardsEquityDetailsValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsEquityDetailsValues from a JSON string
total_rewards_equity_details_values_instance = TotalRewardsEquityDetailsValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsEquityDetailsValues.to_json())

# convert the object into a dict
total_rewards_equity_details_values_dict = total_rewards_equity_details_values_instance.to_dict()
# create an instance of TotalRewardsEquityDetailsValues from a dict
total_rewards_equity_details_values_from_dict = TotalRewardsEquityDetailsValues.from_dict(total_rewards_equity_details_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


