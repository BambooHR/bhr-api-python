# TotalRewardsExtraPayDetailsValues

Schema for total rewards extra pay details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**amount** | **str** | Amount | [optional] 
**amount_subvalue** | **str** |  | [optional] 
**frequency** | **str** | Frequency | [optional] 
**formatted_date_string** | **date** | Extra pay formatted date | [optional] 
**annualized_amount** | **str** | Annualized amount | [optional] 
**annualized_subvalue** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_extra_pay_details_values import TotalRewardsExtraPayDetailsValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsExtraPayDetailsValues from a JSON string
total_rewards_extra_pay_details_values_instance = TotalRewardsExtraPayDetailsValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsExtraPayDetailsValues.to_json())

# convert the object into a dict
total_rewards_extra_pay_details_values_dict = total_rewards_extra_pay_details_values_instance.to_dict()
# create an instance of TotalRewardsExtraPayDetailsValues from a dict
total_rewards_extra_pay_details_values_from_dict = TotalRewardsExtraPayDetailsValues.from_dict(total_rewards_extra_pay_details_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


