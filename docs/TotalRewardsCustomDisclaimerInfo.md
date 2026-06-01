# TotalRewardsCustomDisclaimerInfo

Schema for a total rewards custom disclaimer info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_viewer_admin** | **bool** | Is admin currently viewing | [optional] 
**custom_disclaimer** | **str** |  | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_custom_disclaimer_info import TotalRewardsCustomDisclaimerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsCustomDisclaimerInfo from a JSON string
total_rewards_custom_disclaimer_info_instance = TotalRewardsCustomDisclaimerInfo.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsCustomDisclaimerInfo.to_json())

# convert the object into a dict
total_rewards_custom_disclaimer_info_dict = total_rewards_custom_disclaimer_info_instance.to_dict()
# create an instance of TotalRewardsCustomDisclaimerInfo from a dict
total_rewards_custom_disclaimer_info_from_dict = TotalRewardsCustomDisclaimerInfo.from_dict(total_rewards_custom_disclaimer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


