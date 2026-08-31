# TotalRewardsTimeOffPolicyValue

Schema for total rewards time off policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**value** | **str** | Value | [optional] 
**show_disclaimer** | **bool** |  | [optional] 
**show_eligible** | **bool** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_time_off_policy_value import TotalRewardsTimeOffPolicyValue

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsTimeOffPolicyValue from a JSON string
total_rewards_time_off_policy_value_instance = TotalRewardsTimeOffPolicyValue.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsTimeOffPolicyValue.to_json())

# convert the object into a dict
total_rewards_time_off_policy_value_dict = total_rewards_time_off_policy_value_instance.to_dict()
# create an instance of TotalRewardsTimeOffPolicyValue from a dict
total_rewards_time_off_policy_value_from_dict = TotalRewardsTimeOffPolicyValue.from_dict(total_rewards_time_off_policy_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


