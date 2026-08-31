# TotalRewardsOnboardingStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the onboarding step | [optional] 
**completed** | **bool** | Whether or not the onboarding step is completed | [optional] 

## Example

```python
from bamboohr_sdk.models.total_rewards_onboarding_step import TotalRewardsOnboardingStep

# TODO update the JSON string below
json = "{}"
# create an instance of TotalRewardsOnboardingStep from a JSON string
total_rewards_onboarding_step_instance = TotalRewardsOnboardingStep.from_json(json)
# print the JSON string representation of the object
print(TotalRewardsOnboardingStep.to_json())

# convert the object into a dict
total_rewards_onboarding_step_dict = total_rewards_onboarding_step_instance.to_dict()
# create an instance of TotalRewardsOnboardingStep from a dict
total_rewards_onboarding_step_from_dict = TotalRewardsOnboardingStep.from_dict(total_rewards_onboarding_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


