# TotalRewardsEquitySectionValues

Schema for total rewards equity section values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comp_summary** | [**TotalRewardsCompSummaryValues**](TotalRewardsCompSummaryValues.md) | Compensation summary values for equity | [optional] 
**conditions** | **str** |  | [optional] 
**disclaimers** | **str** |  | [optional] 
**equity_details** | [**List[TotalRewardsEquityDetailsValues]**](TotalRewardsEquityDetailsValues.md) | Equity details | [optional] 
**equity_estimated_valuation** | [**TotalRewardsEquityEstimatedValuationValues**](TotalRewardsEquityEstimatedValuationValues.md) | Total rewards equity estimated valuation object | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_equity_section_values import TotalRewardsEquitySectionValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsEquitySectionValues from a JSON string
total_rewards_equity_section_values_instance = TotalRewardsEquitySectionValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsEquitySectionValues.to_json())

# convert the object into a dict
total_rewards_equity_section_values_dict = total_rewards_equity_section_values_instance.to_dict()
# create an instance of TotalRewardsEquitySectionValues from a dict
total_rewards_equity_section_values_from_dict = TotalRewardsEquitySectionValues.from_dict(total_rewards_equity_section_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


