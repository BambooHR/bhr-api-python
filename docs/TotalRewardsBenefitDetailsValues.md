# TotalRewardsBenefitDetailsValues

Schema for a total rewards benefit details value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**company_contribution_amount** | **str** | Company contribution amount | [optional] 
**company_contribution_subvalue** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**benefit_modal_values_link** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_benefit_details_values import TotalRewardsBenefitDetailsValues

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsBenefitDetailsValues from a JSON string
total_rewards_benefit_details_values_instance = TotalRewardsBenefitDetailsValues.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsBenefitDetailsValues.to_json())

# convert the object into a dict
total_rewards_benefit_details_values_dict = total_rewards_benefit_details_values_instance.to_dict()
# create an instance of TotalRewardsBenefitDetailsValues from a dict
total_rewards_benefit_details_values_from_dict = TotalRewardsBenefitDetailsValues.from_dict(total_rewards_benefit_details_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


